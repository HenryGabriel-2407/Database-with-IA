use teste;
create table dados_aereo(
	nome_empresa varchar(20),
    numero_voo char(4),
    tipo_voo varchar(20),
    voo_origem varchar(30),
    voo_destino varchar(30),
    data_partida datetime,
    nome_passageiro varchar(40),
    cpf_passageiro char(17),
    numero_bilhete char(10),
    idade_passageiro date,
    classe_passageiro varchar(15),
    valor_passageiro float
);
