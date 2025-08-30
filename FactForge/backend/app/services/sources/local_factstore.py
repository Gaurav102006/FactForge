# A local lightweight fact-check store for demo.
FACTS = [
    {'claim':'Drinking hot water cures COVID', 'label':'false', 'source':'WHO', 'url':'https://www.who.int'},
    {'claim':'Vaccines cause autism', 'label':'false', 'source':'CDC', 'url':'https://www.cdc.gov'},
    {'claim':'Earth orbits the Sun', 'label':'true', 'source':'NASA', 'url':'https://solarsystem.nasa.gov'},
    {'claim':'5G towers cause COVID', 'label':'false', 'source':'WHO', 'url':'https://www.who.int'}
]
def query_local(claim: str):
    q = claim.lower()
    matches = []
    for f in FACTS:
        if f['claim'].lower() in q or q in f['claim'].lower():
            matches.append(f)
    return matches
