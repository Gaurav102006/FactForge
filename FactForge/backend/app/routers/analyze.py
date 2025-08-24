
from fastapi import APIRouter, HTTPException
from ..models.schemas import AnalyzeRequest, AnalyzeResponse, Claim, Verdict, Source, Explanation
from ..services.claim_extraction import extract_claims
from ..services.verification import verify_claims
from ..services.generation import generate_explanations

router = APIRouter()

@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze(req: AnalyzeRequest):
    text = req.input
    if not text:
        raise HTTPException(status_code=400, detail="Empty input")
    claims = extract_claims(text)
    if not claims:
        return AnalyzeResponse(claims=[], verdicts=[], explanations=[], sources=[], shareable={})
    verdicts, sources = verify_claims([c.text for c in claims], lang=req.lang)
    explanations, shareable = generate_explanations(claims, verdicts, sources)
    return AnalyzeResponse(
        claims=claims,
        verdicts=verdicts,
        explanations=explanations,
        sources=sources,
        shareable=shareable
    )
