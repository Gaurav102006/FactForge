from typing import List, Tuple, Dict
from ..models import Claim, Verdict, Source, Explanation
from ..config import OPENAI_API_KEY, MODEL_NAME

try:
    import openai
    openai.api_key = OPENAI_API_KEY or None
except Exception:
    openai = None

def generate_explanations(claims: List[Claim], verdicts: List[Verdict], sources: List[Source]) -> Tuple[List[Explanation], Dict]:
    exps = []
    for v in verdicts:
        if v.label == 'false':
            short = f"❌ False: '{v.claim}'. Reliable sources contradict this."
            long = f"The claim '{v.claim}' is not supported by available evidence. See: " + ", ".join([s.title for s in sources]) if sources else "No immediate authoritative source found."
        elif v.label == 'true':
            short = f"✅ True: '{v.claim}'."
            long = f"The claim '{v.claim}' aligns with authoritative sources: " + ", ".join([s.title for s in sources]) if sources else "Confirmed by multiple sources."
        else:
            short = f"⚠️ Needs Review: '{v.claim}'."
            long = f"We couldn't find strong corroborating evidence. Consider consulting reliable sources listed below."

        # If OpenAI available, produce a crisp human-friendly summary
        if openai and OPENAI_API_KEY:
            try:
                prompt = (f"You are a concise fact-check assistant.\nClaim: {v.claim}\nVerdict: {v.label}\nProvide a 1-line summary and a 2-3 sentence explanation citing sources if present.")
                resp = openai.ChatCompletion.create(model=MODEL_NAME, messages=[{"role":"user","content":prompt}], max_tokens=200)
                text = resp['choices'][0]['message']['content'].strip()
                short = text.split('\n')[0] if '\n' in text else text
                long = '\n'.join(text.split('\n')[1:]) if '\n' in text else long
            except Exception:
                pass

        exps.append(Explanation(type='short', text=short))
        exps.append(Explanation(type='long', text=long))

    shareable = {'tweet': f"Checked with #FactForge: {verdicts[0].claim[:80]} -> {verdicts[0].label.upper()}" if verdicts else {}}
    return exps, shareable
