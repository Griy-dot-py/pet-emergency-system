from fastapi import FastAPI

from .routers import router_list

app = FastAPI()
for router in router_list:
    app.include_router(router.fastapi_router)
