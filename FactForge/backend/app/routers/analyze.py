from fastapi import APIRouter, HTTPException
from ..models.schemas import AnalyzeRequest, AnalyzeResponse
from ..services import claim_extraction, verification, generation

router = APIRouter()

@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze(req: AnalyzeRequest):
    if not req.input:
        raise HTTPException(status_code=400, detail="Input text is required")

    claims = claim_extraction.extract_claims(req.input)
    verdicts, sources = verification.verify_claims([c.text for c in claims], lang=req.lang)
    explanations, shareable = generation.generate_explanations(claims, verdicts, sources)

    return AnalyzeResponse(
        claims=claims,
        verdicts=verdicts,
        explanations=explanations,
        sources=sources,
        shareable=shareable
    )
