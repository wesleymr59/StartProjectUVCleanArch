from fastapi import FastAPI
from fastapi import Depends

from app.controllers.healthyCheck import healthy_check

app = FastAPI() 

app.include_router(healthy_check.router)