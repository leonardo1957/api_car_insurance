# Simulador de Prêmio de Seguro de Carro

## 1. Instalar dependências
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 2. Criar banco de dados
Crie um banco de dados local PostgreSQL com as seguintes credenciais:

- **Host:** localhost
- **Port:** 5432
- **User:** postgres
- **Password:** postgres
- **Database:** postgres

Variáveis de ambiente:
```py
DATABASE_URL= postgresql://postgres:postgres@localhost/postgres
TAXA_BASE=0.05
TAXA_POR_ANO=0.005
TAXA_POR_VALOR=0.005
AJUSTE_GIS=0.0
TAXA_VALOR_CALCULO=10000
```

## 3. Rodar o projeto com Docker
```sh
docker-compose up --build
```

## 4. Gerar tabelas
```sh
alembic revision --autogenerate -m "Criando tabelas"
alembic upgrade head
```

## 5. Rodar API
```sh
uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
```

## 6. Testar API no navegador ou Postman
Acesse: `http://localhost:8000/docs`

## 7. Rotas da API

### 7.1. Calcular Prêmio do Seguro
- **Endpoint:** `POST /calculate`
- **Descrição:** Calcula o prêmio do seguro baseado nas informações do carro e franquia.
- **Payload de Envio:**
  ```json
  {
    "marca": "Toyota",
    "modelo": "Corolla",
    "ano": 2020,
    "valor": 90000,
    "porcentagem_dedutivel": 0.1,
    "taxa_do_corretor": 500.0,
    "local_de_registro": "São Paulo"
  }
  ```
- **Retorno:**
  ```json
        {
          "taxa_aplicada": ,
          "premio_final": ,
          "limite_apolice_final": ,
          "valor_franquia": ,
        }
  ```

