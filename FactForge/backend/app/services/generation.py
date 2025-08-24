
from typing import List, Tuple, Dict
from ..models.schemas import Claim, Verdict, Source, Explanation

# Member 2: replace with calls to an LLM (OpenAI/Anthropic) with carefully engineered prompts.
def generate_explanations(claims: List[Claim], verdicts: List[Verdict], sources: List[Source]) -> Tuple[List[Explanation], Dict]:
    exps: List[Explanation] = []
    for v in verdicts:
        if v.label == "false":
            exps.append(Explanation(type="short", text=f"❌ False: '{v.claim}'. Trusted sources contradict this claim."))
        elif v.label == "true":
            exps.append(Explanation(type="short", text=f"✅ True: '{v.claim}'. This aligns with available evidence."))
        else:
            exps.append(Explanation(type="short", text=f"⚠️ Needs Review: '{v.claim}'. Insufficient evidence for a firm verdict."))
    shareable = {
        "tweet": "Myth busted with #FactForge. Check claims with sources before sharing.",
        "headline": "FactForge: Instant claim checks with clear, shareable explanations."
    }
    return exps, shareable
