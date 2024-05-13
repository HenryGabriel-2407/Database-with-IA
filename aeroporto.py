from dados import DadosAereo
import mysql.connector
import google.generativeai as genai
from typing import Type
import pandas as pd

#Definindo a IA:
genai.configure(api_key="API_KEY")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]

system_instruction = "Aja como uma assistente de uma companhia aérea. \nAnalise, se possível, os dados do aeroporto, com foco na identificação de padrões, tendências, idade média dos passageiros, rotas mais populares, e insights acionáveis para auxiliar na tomada de decisões. Caso não for possível, apenas descreva esses dados."

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              system_instruction=system_instruction,
                              safety_settings=safety_settings)

#BANCO DE DADOS

conexao = mysql.connector.connect(host="localhost", user="root", passwd="senha", database="teste")
cursor = conexao.cursor()

class Registrar():
  def add_passagem(self, dados: Type[DadosAereo]) -> None:
    sql = f"SELECT numero_bilhete, numero_voo FROM dados_aereo WHERE numero_bilhete ='{dados.numero_bilhete}' AND numero_voo = '{dados.numero_voo}'"
    cursor.execute(sql)
    if cursor.fetchone():
      print("Passagem registrada!")
      return
    try:
      sql = f"INSERT INTO `dados_aereo` (`nome_empresa`, `numero_voo`, `tipo_voo`, `voo_origem`, `voo_destino`, `data_partida`, `nome_passageiro`, `cpf_passageiro`, `numero_bilhete`, `idade_passageiro`, `classe_passageiro`, `valor_passageiro`) VALUES ('{dados.nome_empresa}', '{dados.numero_voo}', '{dados.tipo_voo}', '{dados.voo_origem}', '{dados.voo_destino}', '{dados.data_partida}', '{dados.nome_passageiro}', '{dados.cpf}', '{dados.numero_bilhete}', '{dados.idade_passageiro}', '{dados.classe_passageiro}', '{dados.valor_passageiro}')"
      cursor.execute(sql)
      conexao.commit()
    except:
      print("Erro! Tente inserir dados corretamente.")
    finally:
      print("#"*40)
  

  def remover_passagem(self):
    numero_bilhete = str(input("Digite o número do bilhete do passageiro: "))
    numero_voo = str(input("Digite o número do voo: "))
    try:
      sql = f"DELETE FROM dados_aereo WHERE numero_bilhete = '{numero_bilhete}' AND numero_voo = '{numero_voo}'"
      cursor.execute(sql)
      print("Passagem excluído com sucesso!")
      conexao.commit()
    except:
      print("A passagem não existe")
    finally:
      print("#" * 40)

  def alterar_passagem(self):
    numero_bilhete_pesquisar = str(input("Digite o número do bilhete do passageiro: "))
    numero_voo_pesquisar = str(input("Digite o número do voo: "))
    sql = f"SELECT * FROM dados_aereo WHERE numero_bilhete = '{numero_bilhete_pesquisar}' AND numero_voo = '{numero_voo_pesquisar}'"
    try:
      cursor.execute(sql)
      resultado = cursor.fetchone()
      if resultado:
        print("-"*40)
        nome_empresa = str(input("Digite o nome da companhia aérea: "))
        numero_voo = str(input("Digite o número do voo: "))
        tipo_voo = str(input("Digite o tipo do voo (nacional ou internacional): "))
        voo_origem = str(input("Digite a cidade de origem: "))
        voo_destino = str(input("Digite a cidade destino: "))
        data_partida = str(input("Digite a data do voo(AAAA-MM-DD): "))
        nome_passageiro = str(input("Digite o nome do passageiro: "))
        cpf = str(input("Digite o CPF do passageiro [XXX.XXX.XXX-XX]: "))
        numero_bilhete = str(input("Digite o número do bilhete: "))
        idade_passageiro = str(input("Digite a data de nascimento do passageiro [AAAA-MM-DD]: "))
        classe_passageiro = str(input("Digite a classe do passageiro (econômico, executivo, etc): "))
        valor_passageiro = float(input("Digite o valor pago: "))
    
        try:
          sql = f"UPDATE dados_aereo SET `nome_empresa` = '{nome_empresa}', `numero_voo` = '{numero_voo}', `tipo_voo` = '{tipo_voo}', `voo_origem` = '{voo_origem}', `voo_destino` = '{voo_destino}', `data_partida` = '{data_partida}', `nome_passageiro` = '{nome_passageiro}', `cpf_passageiro` = '{cpf}', `numero_bilhete` = '{numero_bilhete}', `idade_passageiro` = '{idade_passageiro}', `classe_passageiro` = '{classe_passageiro}', `valor_passageiro` = '{valor_passageiro}' WHERE numero_bilhete = '{numero_bilhete_pesquisar}' AND numero_voo = '{numero_voo_pesquisar}'"
          cursor.execute(sql)
          print("Dados modificados com sucesso!")
          conexao.commit()
        except Exception as e:
          print(f"Erro, tente novamente... Erro: {e}")
    except Exception as e:
      print(f"Erro: {e}")
    print("#"*40)

  def pesquisar_dados(self):
    sql = "SELECT * FROM dados_aereo"
    cursor.execute(sql)
    analise = []
    for (nome_empresa, numero_voo, tipo_voo, voo_origem, voo_destino, data_partida, nome_passageiro, cpf, numero_bilhete, idade_passageiro, classe_passageiro, valor_passageiro) in cursor:
      analise.append([nome_empresa, numero_voo, tipo_voo, voo_origem, voo_destino, data_partida, nome_passageiro, cpf, numero_bilhete, idade_passageiro, classe_passageiro, valor_passageiro])
    df = pd.DataFrame(analise, columns=["Nome Empresa", "Número Voo", "Tipo Voo", "Origem", "Destino", "Data Partida", "Nome Passageiro", "CPF", "Número Bilhete", "Idade Passageiro", "Classe Passageiro", "Valor Passagem"])
    print(df)
    print("#"*40)


  def analisar_ia(self):
    sql = "SELECT * FROM dados_aereo"
    cursor.execute(sql)
    analise = []
    for (nome_empresa, numero_voo, tipo_voo, voo_origem, voo_destino, data_partida, nome_passageiro, cpf, numero_bilhete, idade_passageiro, classe_passageiro, valor_passageiro) in cursor:
      analise.append([nome_empresa, numero_voo, tipo_voo, voo_origem, voo_destino, data_partida, nome_passageiro, cpf, numero_bilhete, idade_passageiro, classe_passageiro, valor_passageiro])

    df = pd.DataFrame(analise, columns=["Nome Empresa", "Número Voo", "Tipo Voo", "Origem", "Destino", "Data Partida", "Nome Passageiro", "CPF", "Número Bilhete", "Idade Passageiro", "Classe Passageiro", "Valor Passagem"])    
    pedido = f"{df}"
    convo = model.start_chat(history=[
    {
        "role": "user",
        "parts": [pedido]
    },
    {
        "role": "model",
        "parts": ["​"]
    },
    ])
    convo.send_message("YOUR_USER_INPUT")
    print("Assistente: " + convo.last.text)
    print("="*40)