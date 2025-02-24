from .routers import router_list
from fastapi import FastAPI


api = FastAPI()
for router in router_list:
    api.include_router(router)
