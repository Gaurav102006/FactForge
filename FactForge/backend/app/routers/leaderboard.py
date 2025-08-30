from fastapi import APIRouter, Depends
from sqlmodel import select, func
from ..database import get_session
from ..models import User, Analysis

router = APIRouter()

@router.get('/top')
def top(session = Depends(get_session)):
    stmt = select(User.email, func.count(Analysis.id).label('cnt')).join(Analysis, Analysis.user_id==User.id).group_by(User.id).order_by(func.count(Analysis.id).desc()).limit(10)
    rows = session.exec(stmt).all()
    return [{'user':r[0],'count':r[1]} for r in rows]
