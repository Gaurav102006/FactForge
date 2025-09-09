from typing import List, Tuple
from ..models import Verdict, Source
from .sources import local_factstore, wikipedia
import difflib

def verify_claims(claim_texts: List[str], lang: str = 'en') -> Tuple[List[Verdict], List[Source]]:
    verdicts = []
    sources = []
    for ct in claim_texts:
        # local store exact/substring match
        matches = local_factstore.query_local(ct)
        if matches:
            m = matches[0]
            verdicts.append(Verdict(claim=ct, label=m['label'], confidence=0.92))
            sources.append(Source(title=m['source'], url=m['url'], publisher=m['source']))
            continue
        # fuzzy: check if any known claim is similar (ratio > 0.7)
        for f in local_factstore.FACTS:
            r = difflib.SequenceMatcher(a=f['claim'].lower(), b=ct.lower()).ratio()
            if r > 0.7:
                verdicts.append(Verdict(claim=ct, label=f['label'], confidence=0.7))
                sources.append(Source(title=f['source'], url=f['url'], publisher=f['source']))
                break
        else:
            # fallback: try wikipedia summary to provide context
            wp = wikipedia.wiki_search(ct.split(' ')[0:6][0]) if ct else None
            if wp:
                sources.append(Source(title=wp['title'] or 'Wikipedia', url=wp['url'] or 'https://en.wikipedia.org', publisher='Wikipedia'))
            verdicts.append(Verdict(claim=ct, label='needs_review', confidence=0.55))
    uniq = {s.url: s for s in sources if s.url}
    return verdicts, list(uniq.values())
