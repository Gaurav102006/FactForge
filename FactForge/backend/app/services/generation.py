from typing import List, Tuple, Dict
from ..models.schemas import Claim, Verdict, Source, Explanation

def generate_explanations(claims: List[Claim], verdicts: List[Verdict], sources: List[Source]) -> Tuple[List[Explanation], Dict]:
    exps: List[Explanation] = []

    for v in verdicts:
        if v.label == "false":
            exps.append(Explanation(
                type="short",
                text=f"❌ False: '{v.claim}'. Trusted sources disagree."
            ))
            exps.append(Explanation(
                type="long",
                text=f"The claim '{v.claim}' is not supported by scientific evidence. Refer to sources: "
                     + ", ".join([s.title for s in sources])
            ))
        elif v.label == "true":
            exps.append(Explanation(type="short", text=f"✅ True: '{v.claim}'"))
        else:
            exps.append(Explanation(type="short", text=f"⚠️ Needs Review: '{v.claim}'. More evidence required."))

    shareable = {
        "tweet": f"🔎 Checked with #FactForge: {verdicts[0].claim[:60]}... → {verdicts[0].label.upper()}",
        "headline": "FactForge helps you spot misinformation instantly."
    }

    return exps, shareable
