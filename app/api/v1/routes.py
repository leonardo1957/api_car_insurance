from fastapi import APIRouter
from app.models.carro import Carro
from app.models.franquia import Franquia
from app.services.calculo import CalculadoraDeSeguro

router = APIRouter()

@router.post("/calculate")
def calcular_premio(marca: str, modelo: str, ano: int, valor: float, porcentagem_dedutivel: float, taxa_do_corretor: float, local_de_registro: str = None):
    carro = Carro(marca=marca, modelo=modelo, ano=ano, valor=valor, local_de_registro=local_de_registro)
    franquia = Franquia(porcentagem=porcentagem_dedutivel)
    return CalculadoraDeSeguro.calcular_premio(carro, franquia, taxa_do_corretor)