from fastapi import APIRouter, Depends, HTTPException, Header
from typing import Optional
from sqlmodel import Session, select
from ..models import AnalyzeRequest, AnalyzeResponse, Analysis, User
from ..database import get_session
from ..services.claim_extraction import extract_claims
from ..services.verification import verify_claims
from ..services.generation import generate_explanations
from ..utils.auth_utils import decode_token

router = APIRouter()

def get_user_from_auth(authorization: Optional[str], session: Session):
    if not authorization: return None
    parts = authorization.split()
    if len(parts) != 2: return None
    token = parts[1]
    sub = decode_token(token)
    if not sub: return None
    user = session.exec(select(User).where(User.email==sub)).first()
    return user

@router.post('/analyze', response_model=AnalyzeResponse)
def analyze(req: AnalyzeRequest, authorization: Optional[str] = Header(None), session: Session = Depends(get_session)):
    if not req.input:
        raise HTTPException(status_code=400, detail='Empty input')
    claims = extract_claims(req.input)
    verdicts, sources = verify_claims([c.text for c in claims], lang=req.lang)
    explanations, shareable = generate_explanations(claims, verdicts, sources)
    # save analysis if user present
    user = get_user_from_auth(authorization, session)
    if user:
        a = Analysis(user_id=user.id, input_text=req.input, result_json={'claims':[c.text for c in claims],'verdicts':[v.dict() for v in verdicts]})
        session.add(a); session.commit()
    return AnalyzeResponse(claims=claims, verdicts=verdicts, explanations=explanations, sources=sources, shareable=shareable)
