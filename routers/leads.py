from fastapi import APIRouter
from models.lead import Lead
from services.leads_service import LeadsService

router = APIRouter(prefix="/zoho", tags=["Zoho Leads"])


@router.get("/leads")
async def fetch_leads():
    return await LeadsService.get_leads()


@router.post("/leads")
async def add_lead(lead: Lead):
    return await LeadsService.create_lead(lead)


@router.put("/leads/{lead_id}")
async def update_lead(lead_id: str, lead: Lead):
    return await LeadsService.update_lead(lead_id, lead)

@router.delete("/leads/{lead_id}")
async def delete_lead(lead_id: str):
    return await LeadsService.delete_lead(lead_id)


@router.get("/leads/summary")
async def fetch_lead_summaries():
    return await LeadsService.get_lead_summaries()
