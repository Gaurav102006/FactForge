from typing import List, Tuple
from ..models.schemas import Verdict, Source
from .sources import google_factcheck, wikipedia

def verify_claims(claim_texts: List[str], lang: str = "en") -> Tuple[List[Verdict], List[Source]]:
    verdicts: List[Verdict] = []
    sources: List[Source] = []

    for ct in claim_texts:
        # Try FactCheck API
        fact_res = google_factcheck.search_fact_checks(ct)
        if fact_res:
            verdicts.append(Verdict(claim=ct, label=fact_res["label"], confidence=fact_res["confidence"]))
            sources.append(Source(title=fact_res["title"], url=fact_res["url"], publisher=fact_res["publisher"]))
            continue

        # Try Wikipedia
        wiki_res = wikipedia.search_wikipedia(ct)
        if wiki_res:
            verdicts.append(Verdict(claim=ct, label="needs_review", confidence=0.6))
            sources.append(Source(title=wiki_res["title"], url=wiki_res["url"], publisher="Wikipedia"))
            continue

        # Default fallback
        verdicts.append(Verdict(claim=ct, label="needs_review", confidence=0.5))
        sources.append(Source(title="General reference", url="https://en.wikipedia.org", publisher="Wikipedia"))

    # Deduplicate
    uniq = {s.url: s for s in sources}
    return verdicts, list(uniq.values())
