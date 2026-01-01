from pydantic import BaseModel
from typing import Optional


class Lead(BaseModel):
    first_name: Optional[str] = None
    last_name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    company: Optional[str] = None
    lead_source: Optional[str] = None
    lead_status: Optional[str] = None
    industry: Optional[str] = None
    annual_revenue: Optional[float] = None
    website: Optional[str] = None
    description: Optional[str] = None
    street: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None
    country: Optional[str] = None

class LeadSummary(BaseModel):
    id: str
    name: Optional[str]
    email: Optional[str]
    company: Optional[str]