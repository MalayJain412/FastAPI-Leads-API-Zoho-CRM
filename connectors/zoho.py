import httpx
from core.config import settings
from connectors.zoho_auth import get_access_token


async def get_leads():
    token = await get_access_token()

    headers = {
        "Authorization": f"Zoho-oauthtoken {token}"
    }

    async with httpx.AsyncClient() as client:
        res = await client.get(
            f"{settings.ZOHO_BASE_URL}/Leads",
            headers=headers
        )
        res.raise_for_status()
        return res.json()


async def create_lead(lead):
    token = await get_access_token()

    headers = {
        "Authorization": f"Zoho-oauthtoken {token}"
    }

    body = {
        "data": [
            {
                "First_Name": lead.first_name,
                "Last_Name": lead.last_name,
                "Email": lead.email,
                "Phone": lead.phone,
                "Company": lead.company,
                "Lead_Source": lead.lead_source,
                "Lead_Status": lead.lead_status,
                "Industry": lead.industry,
                "Annual_Revenue": lead.annual_revenue,
                "Website": lead.website,
                "Description": lead.description,
                "Street": lead.street,
                "City": lead.city,
                "State": lead.state,
                "Zip_Code": lead.zip_code,
                "Country": lead.country,
            }
        ]
    }

    async with httpx.AsyncClient() as client:
        res = await client.post(
            f"{settings.ZOHO_BASE_URL}/Leads",
            json=body,
            headers=headers
        )
        res.raise_for_status()
        return res.json()


async def update_lead(lead_id, lead):
    token = await get_access_token()

    headers = {
        "Authorization": f"Zoho-oauthtoken {token}"
    }

    body = {
        "data": [
            {
                "First_Name": lead.first_name,
                "Last_Name": lead.last_name,
                "Email": lead.email,
                "Phone": lead.phone,
                "Company": lead.company,
                "Lead_Source": lead.lead_source,
                "Lead_Status": lead.lead_status,
                "Industry": lead.industry,
                "Annual_Revenue": lead.annual_revenue,
                "Website": lead.website,
                "Description": lead.description,
                "Street": lead.street,
                "City": lead.city,
                "State": lead.state,
                "Zip_Code": lead.zip_code,
                "Country": lead.country,
            }
        ]
    }

    async with httpx.AsyncClient() as client:
        res = await client.put(
            f"{settings.ZOHO_BASE_URL}/Leads/{lead_id}",
            json=body,
            headers=headers
        )
        res.raise_for_status()
        return res.json()


async def delete_lead(lead_id):
    token = await get_access_token()

    headers = {
        "Authorization": f"Zoho-oauthtoken {token}"
    }

    async with httpx.AsyncClient() as client:
        res = await client.delete(
            f"{settings.ZOHO_BASE_URL}/Leads/{lead_id}",
            headers=headers
        )
        res.raise_for_status()
        return res.json()
