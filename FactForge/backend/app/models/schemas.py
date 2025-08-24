
from pydantic import BaseModel, Field
from typing import List, Optional, Literal

class AnalyzeRequest(BaseModel):
    input: str = Field(..., description="Raw text or URL")
    mode: Literal["text", "url"] = "text"
    lang: str = "en"

class Claim(BaseModel):
    text: str

class Verdict(BaseModel):
    claim: str
    label: Literal["true","false","needs_review"]
    confidence: float = 0.5

class Source(BaseModel):
    title: str
    url: str
    publisher: Optional[str] = None

class Explanation(BaseModel):
    type: Literal["short","long"] = "short"
    text: str

class AnalyzeResponse(BaseModel):
    claims: List[Claim]
    verdicts: List[Verdict]
    explanations: List[Explanation]
    sources: List[Source]
    shareable: Optional[dict] = None
