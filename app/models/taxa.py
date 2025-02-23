import os

taxa_base =  float(os.getenv("TAXA_BASE", 0.05))
taxa_por_ano = float(os.getenv("TAXA_POR_ANO", 0.005))
taxa_por_valor = float(os.getenv("TAXA_POR_VALOR", 0.005))
ajuste_gis = float(os.getenv("AJUSTE_GIS", 0.0))
taxa_valor_calculo = float(os.getenv("TAXA_VALOR_CALCULO", 10000))

class Taxa:
    def __init__(self, idade_carro, valor_carro, ajuste_gis=ajuste_gis):
        self.idade_carro = idade_carro
        self.valor_carro = valor_carro
        self.taxa_base = taxa_base
        self.taxa_por_ano = taxa_por_ano
        self.taxa_por_valor = taxa_por_valor
        self.ajuste_gis = ajuste_gis

    def calcular(self) -> float:
        taxa_idade = self.idade_carro * self.taxa_por_ano
        taxa_valor = (self.valor_carro // taxa_valor_calculo) * self.taxa_por_valor
        return round(self.taxa_base + taxa_idade + taxa_valor + self.ajuste_gis, 4)

