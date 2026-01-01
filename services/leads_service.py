from connectors import zoho
from models.lead import Lead


class LeadsService:

    @staticmethod
    async def get_leads():
        return await zoho.get_leads()

    @staticmethod
    async def create_lead(lead: Lead):
        return await zoho.create_lead(lead)

    @staticmethod
    async def update_lead(lead_id, lead: Lead):
        return await zoho.update_lead(lead_id, lead)

    @staticmethod
    async def delete_lead(lead_id):
        return await zoho.delete_lead(lead_id)
    
    @staticmethod
    async def get_lead_summaries():
        leads = await zoho.get_leads()

        summaries = []

        for lead in leads["data"]:
            summaries.append({
                "id": lead.get("id"),
                "name": lead.get("Full_Name") or f"{lead.get('First_Name','')} {lead.get('Last_Name','')}".strip(),
                "email": lead.get("Email"),
                "company": lead.get("Company")
            })

        return summaries
