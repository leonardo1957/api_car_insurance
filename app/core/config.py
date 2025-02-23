import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost/postgres")
TAXA_BASE=os.getenv("TAXA_BASE", "")
TAXA_POR_ANO=os.getenv("TAXA_POR_ANO", "")
TAXA_POR_VALOR=os.getenv("TAXA_POR_VALOR", "")
AJUSTE_GIS=os.getenv("AJUSTE_GIS", "")
TAXA_VALOR_CALCULO=os.getenv("TAXA_VALOR_CALCULO", "")