from aeroporto import Registrar
from dados import DadosAereo

aviao = Registrar()

print("="*10 + "AEROPORTO DE ITAPEMA"+ "="*10)

while True:
    escolha = int(input("[1] adicionar passagem\n[2] remover passagem\n[3] listar passagens \n[4] análise da assistente virtual \n[5] sair \n->"))
    if escolha == 1:
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

        dados_novos = DadosAereo(nome_empresa, numero_voo, tipo_voo, voo_origem, voo_destino, data_partida, nome_passageiro, cpf, numero_bilhete, idade_passageiro, classe_passageiro, valor_passageiro)
        aviao.add_passagem(dados_novos)
    
    elif escolha == 2:
        aviao.remover_passagem()
    elif escolha == 3:
        aviao.pesquisar_dados()
    elif escolha == 4:
        aviao.analisar_ia()
    elif escolha == 5:
        break
    else:
        continue