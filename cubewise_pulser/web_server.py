import logging

from cubewise_pulser.config import init_config
from cubewise_pulser.route import base, sample
from cubewise_pulser.utils import resource_path
from cubewise_pulser.utils.constants import APP_NAME, APP_VERSION
from fastapi import FastAPI, Request, status
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles


def create_app(debug=False):
    app = FastAPI(debug=debug, title=APP_NAME, version=APP_VERSION, docs_url=None, redoc_url=None)
    app.cw_config = init_config()
    app.mount('/static', StaticFiles(directory=resource_path('static')), name='static')

    @app.middleware("http")
    async def catch_exceptions_middleware(request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as e:
            # Log the exception with details
            logging.exception(f"Unhandled exception: {e}", exc_info=True)

            # Return a custom error message to the client
            return JSONResponse(status_code=status.HTTP_501_NOT_IMPLEMENTED,
                                content={"message": "An unexpected error occurred. Please try again later."})

    # Routers api
    app.include_router(base.router)
    app.include_router(sample.router)

    @app.get('/docs', include_in_schema=False)
    async def custom_swagger_ui_html():
        return get_swagger_ui_html(
            openapi_url=app.openapi_url,
            title=app.title + ' - Swagger UI',
            oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
            swagger_js_url='/static/swagger/swagger-ui-bundle.js',
            swagger_css_url='/static/swagger/swagger-ui.css',
        )

    @app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
    async def swagger_ui_redirect():
        return get_swagger_ui_oauth2_redirect_html()

    @app.get('/redoc', include_in_schema=False)
    async def redoc_html():
        return get_redoc_html(
            openapi_url=app.openapi_url,
            title=f'{app.title} - ReDoc',
            redoc_js_url='/static/swagger/redoc.standalone.js',
        )

    return app
