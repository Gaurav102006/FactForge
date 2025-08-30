from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from fastapi.security import OAuth2PasswordRequestForm
from ..database import get_session
from ..models import User, UserCreate, Token
from ..utils.auth_utils import hash_password, verify_password, create_token

router = APIRouter()

@router.post('/register', response_model=dict)
def register(body: UserCreate, session: Session = Depends(get_session)):
    existing = session.exec(select(User).where(User.email == body.email)).first()
    if existing:
        raise HTTPException(status_code=400, detail='Email exists')
    user = User(email=body.email, password_hash=hash_password(body.password))
    session.add(user); session.commit(); session.refresh(user)
    return {'id': user.id, 'email': user.email}

@router.post('/login', response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.email == form_data.username)).first()
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=400, detail='Incorrect credentials')
    t = create_token(user.email)
    return Token(access_token=t['access_token'], expires_in=t['expires_in'])
