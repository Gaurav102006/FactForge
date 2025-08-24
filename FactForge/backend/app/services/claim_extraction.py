
from typing import List
from ..models.schemas import Claim

# Simple, deterministic stub for hackathon kickoff.
# Member 2 will swap with an LLM prompt that extracts factual assertions.
def extract_claims(text: str) -> List[Claim]:
    # Naive split by '.' and filter short sentences
    sentences = [s.strip() for s in text.replace('\n',' ').split('.') if s.strip()]
    claims = []
    for s in sentences:
        if any(k in s.lower() for k in ["cause", "cure", "increase", "decrease", "percent", "leads to", "is"]):
            claims.append(Claim(text=s))
    if not claims and sentences:
        # fallback: take first sentence as a "claim"
        claims.append(Claim(text=sentences[0]))
    return claims
