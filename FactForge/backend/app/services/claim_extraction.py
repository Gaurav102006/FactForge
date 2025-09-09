from typing import List
from ..models import Claim
import re

def extract_claims(text: str) -> List[Claim]:
    text = re.sub('\\s+', ' ', text.strip())
    sentences = [s.strip() for s in re.split(r'[.?!]\s*', text) if s.strip()]
    claims = []
    for s in sentences:
        # heuristics: sentences with 'cause', 'cure', 'percent', 'increase', 'decrease', numbers, 'is', 'are'
        if len(s.split()) >= 4 and any(k in s.lower() for k in ['cause','cure','percent','increase','decrease','leads to','is','are','will']):
            claims.append(Claim(text=s))
    if not claims and sentences:
        claims.append(Claim(text=sentences[0]))
    return claims
