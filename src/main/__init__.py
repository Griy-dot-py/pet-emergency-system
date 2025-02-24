from fastapi import FastAPI

from .routers import router_list

api = FastAPI()
for router in router_list:
    api.include_router(router.fastapi_router)
