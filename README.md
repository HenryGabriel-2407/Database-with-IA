# Database with IA

## Introdução
Dae, galera! Tudo bem? :smile: :v:

Esse é um projeto de um sistema de passagens aéreas e neste readme estão algumas notações de como funciona este projeto.

## passagem_banco_de_dados.py
Antes de tudo, declarei no MySQL quais são os dados e seus tipos na tabela "dados_aereos" que vou trabalhar. Temos na tabela:
* o nome da companhia aérea (nome_empresa);
* número do voo (numero_voo);
* o tipo do voo sendo nacional ou internacional (tipo_voo);
* cidade de origem (voo_origem);
* cidade de destino (voo_destino),
* data de partida (data_partida),
* nome do passageiro (nome_passageiro);
* Cadastro de Pessoa Física - CPF (cpf_passageiro);
* número do bilhete ou código da passagem (numero_bilhete);
* a data de nascimento (idade_passageiro);
* classe da passagem (classe_passageiro); e
* valor da passagem (valor_passgeiro).

![image](https://github.com/HenryGabriel-2407/Database-with-IA/assets/63942305/272b34a1-7a7e-4042-8f69-4c59921392e7)


## dados.py
Criei uma classe "DadosAereo" com apenas um "__init__" para declara os atributos que eu vou usar para adicionar a passagem no banco de dados.

![image](https://github.com/HenryGabriel-2407/Database-with-IA/assets/63942305/6bd3a4b9-eb15-441b-9e03-be484a6ffa73)


## aeroporto.py
Começando importando as bibliotecas e o arquivo dados.py que eu vou usar, temos a classe "DadosAereo" do arquivo dados.py mencionado anteriormente, a biblioteca mysql.connector para fazer conexão com o SGBD, a biblioteca google.generativeai para utilizar a IA do Google para fazer análise e/ou descrever os dados, o Type (é mais prefêrencia minha para quando adicionar a passagem aceitar a classe "DadosAereo" como paramêntro nesta função, e por fim (e o que menos esperava em usar pela primeira vez no projeto kkkk) Pandas!
Após declarar as bibliotecas, modelo as configurações da IA do Google (e utilizando a API KEY para acessar a IA): 
 * generation_config: basicamente é a "criatividade" e escolha de palavras para formar o conteúdo do nosso prompt.
 * safety_setting: é o controle de conteúdo da IA, é bastante útil para detecção de discurso de ódio e etc., no caso do projeto coloquei todos em "BLOCK_NONE" por preferência minha mesmo.
 * system_instruction: é o comportamento, a "personalidade" e o jeito  que a IA vai interagir com o usuário. Agora temos todas as peças para montar a IA.
 * model: é o conjunto das configurações mencionados, é o "corpo" inteiro da IA.

![image](https://github.com/HenryGabriel-2407/Database-with-IA/assets/63942305/31b0b71d-2478-42dc-bc8c-8d00d93cc817)
![image](https://github.com/HenryGabriel-2407/Database-with-IA/assets/63942305/4e22ddd3-b3a2-4e3f-9181-d8ed44c63455)


Com a IA pronta fiz a conexão do programa com o SGBD e declarando a classe Registrar que terão metódos "add_passagem", "remover_passagem", "alterar_passagem", "pesquisar_dados" e "analisar_ia".
### Classe Registrar
É a classe responsável das operações do sistema. 
1. "add_passagem": esse metódo receberá a classe "DadosAereo" em si (os atributos da classe) que primeiro vai conferir se o número do bilhete em relação do número do voo já existente (imagina a confusão quando o Pedro e Joana receber em seus bilhetes, do mesmo voo, o mesmo código). Se não não existir, será adicionado na tabela.
2. "remover_passagem": esse metódo vai pedir o número do bilhete e o número do voo para conferir se existe (se não existir é mesma coisa que um careca cortar o cabelo). Se exisitr, será removido.
3. "alterar_passagem": esse metódo vai pedir o número do bilhete e o número do voo para conferir se existe também (imagina alterar a cor de um coelho sendo que não existe coelho!). Se a passagem existe, o metódo vai pedir os dados para serem atualizados.
4. "pesquisar_dados": esse metódo vai retornar todos os dados da tabela e organizar a tabela com a biblioteca pandas (imagina.... já chega kkkk).
5. "analisar_ia": e por fim, este metódo vai pegar todos os dados da tabela e organizar com o pandas para a IA entender, processar e retornar a sua resposta dos dados da forma mais eficiente possível.

![image](https://github.com/HenryGabriel-2407/Database-with-IA/assets/63942305/fb1df41c-ac6d-41af-b28a-2b2d9df074df)
![image](https://github.com/HenryGabriel-2407/Database-with-IA/assets/63942305/0a984f04-0839-4822-a8a8-e6952ba837fb)
![image](https://github.com/HenryGabriel-2407/Database-with-IA/assets/63942305/cad974cf-7659-4a22-a983-12b076f7c3cc)


## main.py
É aqui que o usuário vai interagir com o sistema. Começando com as importações das classes "DadosAereo" e "Registrar" e instanciando o objeto "aviao".
Em seguida temos o menu de opção, é apresentado ao usuário em um loop infinito (while True). As opções incluem adicionar uma passagem (add_passagem da classe Registrar), remover uma passagem (remover_passagem), listar passagens (pesquisar_dados), modificar uma passagem (alterar_passagem), a assistente virtual (IA) analisar os dados (analisar_ia) e sair do programa (break).

![image](https://github.com/HenryGabriel-2407/Database-with-IA/assets/63942305/9a4dc43e-6988-464f-9304-1b6e52c95b12)


## Conclusão
E chegamos ao fim da explicação deste projeto! Eu percerbi, principalmente ao longo que fiquei escrevendo este readme, que ainda tem algumas falhas e muitas coisas que preciso atualizar e corrigir, mas já será corrigido!
