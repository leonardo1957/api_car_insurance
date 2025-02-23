from fastapi import FastAPI
from app.api.v1.routes import router
from app.db.base import init_db

app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()

app.include_router(router, prefix="/api/v1")
