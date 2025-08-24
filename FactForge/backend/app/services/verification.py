
from typing import List, Tuple
from ..models.schemas import Verdict, Source

# Member 1: wire to Google FactCheck + Wikipedia adapters.
def verify_claims(claim_texts: List[str], lang: str = "en") -> Tuple[List[Verdict], List[Source]]:
    verdicts: List[Verdict] = []
    sources: List[Source] = []
    for ct in claim_texts:
        # Stub logic: if 'cure' in claim -> mark false; if 'increase' -> needs_review; else needs_review
        label = "needs_review"
        conf = 0.55
        if "cure" in ct.lower():
            label = "false"
            conf = 0.9
            sources.append(Source(title="WHO Mythbusters", url="https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public/myth-busters", publisher="WHO"))
        elif "percent" in ct.lower() or "increase" in ct.lower():
            label = "needs_review"
            conf = 0.6
            sources.append(Source(title="Wikipedia (general reference)", url="https://en.wikipedia.org/wiki/Main_Page", publisher="Wikipedia"))
        else:
            sources.append(Source(title="General reference", url="https://en.wikipedia.org/", publisher="Wikipedia"))
        verdicts.append(Verdict(claim=ct, label=label, confidence=conf))
    # Deduplicate sources (simple unique by url)
    uniq = {}
    for s in sources:
        uniq[s.url] = s
    sources = list(uniq.values())
    return verdicts, sources
