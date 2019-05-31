"""
api_fastapi.py
"""
import fastapi

from ml.api.__route import ROUTER as router_info

from ml.app_config import \
    api_name, api_desc, api_version, \
    api_debug, \
    api_docs_url, \
    api_redoc_url, \
    api_spec
from ml.utils.logger import get_logger

LOGGER = get_logger(__name__)

# Deployment Note:
# PYTHONPATH=. gunicorn -c ouroboros/config_uvicorn.py ml.app_fastapi:app
app = fastapi.FastAPI(
    title=api_name,
    description=api_desc,
    version=api_version,
    docs_url='/{}'.format(api_docs_url),
    redoc_url='/{}'.format(api_redoc_url),
    openapi_url='/{}'.format(api_spec),
    debug=api_debug)

# Note: router_info should be added at the last.
app.include_router(router_info)
