import os
from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials

def verify_token(credentials: HTTPAuthorizationCredentials):
    valid_token = os.getenv("SECRET_TOKEN", "")
    if credentials.credentials != valid_token:
        raise HTTPException(status_code=403, detail="Invalid or missing token")
