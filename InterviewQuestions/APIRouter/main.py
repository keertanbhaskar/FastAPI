from fastapi import FastAPI, APIRouter
from Student import router

app = FastAPI()


app.include_router(router)
