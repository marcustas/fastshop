from fastapi import FastAPI
from sqladmin import Admin

from admin.admin_views import register_admin_views

from base_settings import base_settings
from general.databases.postgres import postgres
from general.views import router as status_router
from routes import BaseRoutesPrefixes


def include_routes(application: FastAPI) -> None:
    application.include_router(
        router=status_router,
    )


def get_application() -> FastAPI:
    application = FastAPI(
        debug=base_settings.debug,
        docs_url=BaseRoutesPrefixes.swagger if base_settings.debug else None,
        redoc_url=BaseRoutesPrefixes.redoc if base_settings.debug else None,
        openapi_url=BaseRoutesPrefixes.openapi if base_settings.debug else None,
    )

    @application.on_event('startup')
    def startup():
        postgres.connect(base_settings.postgres.url)
        engine = postgres.get_engine()
        admin = Admin(app=application, engine=engine)
        register_admin_views(admin)

    @application.on_event('shutdown')
    async def shutdown():
        await postgres.disconnect()

    include_routes(application)

    return application


app = get_application()
