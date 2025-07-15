from fastapi import FastAPI
from fastapi.security import HTTPBearer
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from dotenv import load_dotenv
from app.routes import router as analyze_router

load_dotenv()

# Define app with security scheme for Swagger UI
app = FastAPI(
    title="Trade Opportunities API",
    description="Analyzes Indian market sectors and provides markdown trade reports.",
    version="1.0.0",
    swagger_ui_init_oauth={},
    openapi_tags=[{
        "name": "Analysis",
        "description": "Provides market analysis for Indian sectors"
    }],
    openapi_url="/openapi.json"
)

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.include_router(analyze_router)
