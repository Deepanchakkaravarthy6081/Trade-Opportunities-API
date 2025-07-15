from fastapi import APIRouter, Depends, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.utils.auth import verify_token
from app.utils.validator import validate_sector
from app.services.analyzer import fetch_market_data, analyze_with_gemini, generate_markdown_report

router = APIRouter()
security_scheme = HTTPBearer(auto_error=True)

@router.get(
    "/analyze/{sector}",
    tags=["Analysis"],
    summary="Analyze a sector",
    description="Returns a markdown market report for the given Indian sector.",
)
async def analyze_sector(
    sector: str,
    credentials: HTTPAuthorizationCredentials = Security(security_scheme)
):
    verify_token(credentials)
    sector = validate_sector(sector)
    try:
        search_results = await fetch_market_data(sector)
        insights = await analyze_with_gemini(search_results)
        report = generate_markdown_report(sector, search_results, insights)
        return {"report": report}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
