
# FactForge — AI-Powered Misinformation Detector & Explainer

Make truth as viral as the lie. FactForge extracts claims from text/URLs, checks them against trusted sources, and generates clear, shareable, human-friendly explanations.

## ✨ USP
**FactForge not only detects misinformation in real time but also generates clear, persuasive explanations and shareable counter-content — making truth as viral as the lie.**

---

## 🧱 Tech Stack

**Frontend**
- React + Vite + TypeScript
- Axios for API calls
- Tailwind-ready CSS (plain CSS in starter, easy to swap)

**Backend**
- FastAPI (Python)
- Pydantic for schemas
- FAISS (or in-memory) for semantic search (stubbed in starter)
- Requests/httpx for external lookups (Google Fact Check, Wikipedia) — stubbed adapters
- OpenAI-compatible LLM client (abstracted behind `generation.py`)

**Infra/Dev**
- uvicorn for local server
- Vite dev server for frontend
- `.env` config for API keys (OpenAI, Google Fact Check)
- Pytest for smoke tests

---

## 🗂 Project Structure

```
FactForge/
├─ backend/
│  ├─ app/
│  │  ├─ main.py
│  │  ├─ config.py
│  │  ├─ __init__.py
│  │  ├─ routers/
│  │  │  ├─ health.py
│  │  │  └─ analyze.py
│  │  ├─ models/
│  │  │  └─ schemas.py
│  │  ├─ services/
│  │  │  ├─ claim_extraction.py
│  │  │  ├─ verification.py
│  │  │  ├─ generation.py
│  │  │  ├─ embeddings.py
│  │  │  └─ sources/
│  │  │     ├─ google_factcheck.py
│  │  │     └─ wikipedia.py
│  │  ├─ utils/
│  │  │  └─ logging.py
│  │  └─ tests/
│  │     └─ test_smoke.py
│  ├─ requirements.txt
│  └─ .env.example
├─ frontend/
│  ├─ package.json
│  ├─ index.html
│  ├─ tsconfig.json
│  ├─ vite.config.ts
│  └─ src/
│     ├─ main.tsx
│     ├─ App.tsx
│     ├─ styles.css
│     ├─ pages/Home.tsx
│     ├─ components/
│     │  ├─ ClaimInput.tsx
│     │  ├─ ResultCard.tsx
│     │  ├─ SourceBadge.tsx
│     │  └─ Loader.tsx
│     └─ services/api.ts
├─ data/
│  ├─ factchecks_sample.json
│  └─ sample_claims.json
├─ scripts/
│  └─ seed_factchecks.py
└─ README.md
```

---

## 👥 Team Roles

- **Member 1 — Backend + APIs (fact-check retrieval)**  
  - Implement `routers/analyze.py` endpoints  
  - Implement `services/verification.py` with adapters to:  
    - `sources/google_factcheck.py`  
    - `sources/wikipedia.py`  
  - Manage `config.py`, environment variables, and API keys  
  - Add caching + basic rate-limit protections

- **Member 2 — NLP pipeline + LLM prompt engineering**  
  - Implement `services/claim_extraction.py` (LLM-backed extraction prompt)  
  - Implement `services/generation.py` (concise verdict + narrative + counter-post)  
  - Implement `services/embeddings.py` (semantic similarity; stub → FAISS later)  
  - Define prompt templates, safety filters, and output format

- **Member 3 — Frontend UI + Demo polish**  
  - Build sleek UI/UX (Home page, input, results, badges, loaders)  
  - Integrate with backend API via `services/api.ts`  
  - Add demo presets and a clean pitch-ready flow  
  - Optional: Chrome extension shell to overlay results

---

## 🚀 Getting Started

### 1) Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Copy env and fill keys
cp app/.env.example app/.env

# Run
uvicorn app.main:app --reload --port 8000
```

### 2) Frontend
```bash
cd frontend
npm install
npm run dev
# visit http://localhost:5173
```

---

## 🔑 Environment Variables (`backend/app/.env.example`)
```
OPENAI_API_KEY=sk-...
GOOGLE_FACTCHECK_API_KEY=...
WIKIPEDIA_USER_AGENT=FactForge/1.0 (contact@example.com)
MODEL_NAME=gpt-4o-mini
```

---

## 🔄 API Contract (Draft)

**POST** `/api/analyze`  
Request:
```json
{
  "input": "Drinking hot water cures COVID",
  "mode": "text",
  "lang": "en"
}
```
Response:
```json
{
  "claims": [{"text":"Drinking hot water cures COVID"}],
  "verdicts": [{"claim":"Drinking hot water cures COVID","label":"false","confidence":0.92}],
  "explanations": [{"type":"short","text":"No evidence supports this. WHO guidance contradicts the claim."}],
  "sources": [{"title":"WHO Mythbusters","url":"https://...","publisher":"WHO"}],
  "shareable": {"tweet":"Myth: hot water cures COVID. Fact: no evidence. Learn more: ..."}
}
```

**GET** `/health`
```json
{"status":"ok"}
```

---

## 🧪 Testing
```bash
cd backend
pytest -q
```

---

## 🧭 Roadmap (Hackathon)
- M1: Claim extraction + health endpoint + mock verification (Day 1)
- M2: Wikipedia + FactCheck adapters (Day 2)
- M3: LLM narrative generation + UX polish (Day 3)
- Stretch: Browser extension, multilingual support, trust score

---

## ⚠️ Safety Notes
- Classify sensitive domains (health, elections); route to cautious prompts
- Always show sources; never claim certainty without citations
- Provide “Needs Review” fallback when low confidence

---

## 📜 License
MIT (feel free to adapt for hackathon use)
