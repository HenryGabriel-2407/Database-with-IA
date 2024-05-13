class DadosAereo:
    def __init__(self, nome_empresa: str, numero_voo: str, tipo_voo: str, voo_origem: str, voo_destino: str, data_partida: str, nome_passageiro: str, cpf: str, numero_bilhete: str, idade_passageiro: str, classe_passageiro: str, valor_passageiro: float) -> None:
        self.nome_empresa = nome_empresa
        self.numero_voo = numero_voo
        self.tipo_voo = tipo_voo
        self.voo_origem = voo_origem
        self.voo_destino = voo_destino
        self.data_partida = data_partida
        self.nome_passageiro = nome_passageiro
        self.cpf = cpf
        self.numero_bilhete = numero_bilhete
        self.idade_passageiro = idade_passageiro
        self.classe_passageiro = classe_passageiro
        self.valor_passageiro = valor_passageiro