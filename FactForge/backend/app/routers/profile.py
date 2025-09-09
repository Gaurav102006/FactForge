from fastapi import APIRouter, Header, HTTPException, Depends
from sqlmodel import select
from ..database import get_session
from ..models import User, Analysis
from ..utils.auth_utils import decode_token

router = APIRouter()

def get_user_from_auth(authorization: str, session):
    if not authorization: return None
    parts = authorization.split()
    if len(parts)!=2: return None
    token = parts[1]
    sub = decode_token(token)
    if not sub: return None
    user = session.exec(select(User).where(User.email==sub)).first()
    return user

@router.get('/me/analyses')
def analyses(authorization: str = Header(None), session = Depends(get_session)):
    user = get_user_from_auth(authorization, session)
    if not user:
        raise HTTPException(status_code=401, detail='Unauthorized')
    res = session.exec(select(Analysis).where(Analysis.user_id==user.id).order_by(Analysis.created_at.desc())).all()
    return [{'id':r.id,'input':r.input_text,'result':r.result_json,'created_at':str(r.created_at)} for r in res]
