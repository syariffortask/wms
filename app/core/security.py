from fastapi import HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlmodel import Session, select
import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from app.models import User
from app.core.database import get_session
from app.core.config import settings

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

security = HTTPBearer()


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expires = datetime.now() + (
        expires_delta or timedelta(hours=settings.ACCESS_TOKEN_EXPIRE_HOURS)
    )
    to_encode.update({"exp": expires})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def decode_access_token(token: str):
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    except jwt.ExpiredSignatureError:
        return None  # Token sudah expired
    except jwt.InvalidTokenError:
        return None  # Token tidak valid


# get current user untuk proteksi route


def get_current_user(required_role: str = None):
    def dependency(
        credential: HTTPAuthorizationCredentials = Depends(security),
        session: Session = Depends(get_session),
    ):
        token = credential.credentials
        payload = decode_access_token(token)
        if payload is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        nik = payload.get("sub")
        stmt = select(User).where(User.nik == nik)
        user = session.exec(stmt).first()

        if not user:
            raise HTTPException(status_code=401, detail="User not found")

        if required_role and user.role != required_role:
            raise HTTPException(status_code=403, detail="Forbidden")

        return user

    return dependency
