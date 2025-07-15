import re
from fastapi import HTTPException

def validate_sector(sector: str) -> str:
    if not re.match(r'^[a-zA-Z]+$', sector):
        raise HTTPException(status_code=400, detail="Invalid sector name.")
    return sector.lower()