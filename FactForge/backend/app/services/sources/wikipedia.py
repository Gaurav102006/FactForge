import requests
from ..config import WIKIPEDIA_USER_AGENT

def wiki_search(query: str):
    try:
        url = 'https://en.wikipedia.org/api/rest_v1/page/summary/' + requests.utils.requote_uri(query.replace(' ', '_'))
        headers = {'User-Agent': WIKIPEDIA_USER_AGENT}
        r = requests.get(url, headers=headers, timeout=5)
        if r.status_code == 200:
            data = r.json()
            return {'title': data.get('title'), 'url': data.get('content_urls', {}).get('desktop', {}).get('page'), 'extract': data.get('extract')}
    except Exception:
        return None
    return None
