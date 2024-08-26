from fastapi import FastAPI
from db.session import engine
from db.base_class import Base
from core.config import settings


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    create_tables()
    return app


app = start_application()


# Path or route for the Api
@app.get("/")
def hello():
    return {"msg": "Hello FastAPI 🚀"}
