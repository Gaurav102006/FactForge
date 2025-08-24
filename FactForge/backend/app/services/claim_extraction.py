from typing import List
from ..models.schemas import Claim

# For hackathon: simple heuristic first, can be swapped with GPT.
def extract_claims(text: str) -> List[Claim]:
    sentences = [s.strip() for s in text.replace('\n', ' ').split('.') if s.strip()]
    claims = []

    for s in sentences:
        if len(s.split()) > 3:  # ignore too-short phrases
            claims.append(Claim(text=s))

    # fallback
    if not claims and sentences:
        claims.append(Claim(text=sentences[0]))

    return claims
