from datetime import datetime
from typing import Optional, List, Literal
from sqlmodel import SQLModel, Field, Column, JSON
from pydantic import BaseModel

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, nullable=False)
    password_hash: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Analysis(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(index=True)
    input_text: str
    result_json: Optional[dict] = Field(default=None, sa_column=Column(JSON))
    created_at: datetime = Field(default_factory=datetime.utcnow)

# Pydantic schemas
class UserCreate(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int

class TokenData(BaseModel):
    sub: str

class Claim(BaseModel):
    text: str

class Verdict(BaseModel):
    claim: str
    label: Literal['true','false','needs_review']
    confidence: float = 0.5

class Source(BaseModel):
    title: str
    url: str
    publisher: Optional[str] = None

class Explanation(BaseModel):
    type: Literal['short','long'] = 'short'
    text: str

class AnalyzeRequest(BaseModel):
    input: str
    mode: str = 'text'
    lang: str = 'en'

class AnalyzeResponse(BaseModel):
    claims: List[Claim]
    verdicts: List[Verdict]
    explanations: List[Explanation]
    sources: List[Source]
    shareable: Optional[dict] = None
