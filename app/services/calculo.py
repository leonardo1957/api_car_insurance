from app.models.taxa import Taxa
from app.models.franquia import Franquia
from datetime import datetime
import os

ajuste_gis = float(os.getenv("AJUSTE_GIS", 0.0))

class CalculadoraDeSeguro:
    @staticmethod
    def calcular_premio(carro, franquia, taxa_do_corretor, ajuste_gis=ajuste_gis):
        idade_carro = datetime.now().year - carro.ano
        taxa = Taxa(idade_carro, carro.valor, ajuste_gis)
        taxa_aplicada = taxa.calcular()

        premio_base = carro.valor * taxa_aplicada
        desconto_franquia = premio_base * franquia.porcentagem
        premio_final = premio_base - desconto_franquia + taxa_do_corretor

        limite_apolice = carro.valor
        valor_franquia = limite_apolice * franquia.porcentagem
        limite_apolice_final = limite_apolice - valor_franquia

        return {
            "taxa_aplicada": taxa_aplicada,
            "premio_final": premio_final,
            "limite_apolice_final": limite_apolice_final,
            "valor_franquia": valor_franquia,
        }