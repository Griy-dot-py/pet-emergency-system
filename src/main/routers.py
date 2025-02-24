from .ens import ens
import routers
from fastapi import APIRouter

group = routers.GroupRouter(core=ens, fastapi_router=APIRouter(prefix="/group"))
group.compile()

notification = routers.NotificationRouter(core=ens, fastapi_router=APIRouter(prefix="/notify"))
notification.compile()

user_bulk = routers.UserBulkRouter(core=ens, fastapi_router=APIRouter(prefix="/user/bulk"))
user_bulk.compile()


router_list = [group, notification, user_bulk]
