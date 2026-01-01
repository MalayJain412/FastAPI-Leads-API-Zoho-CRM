from fastapi import FastAPI, Request
from routers import leads, oauth

app = FastAPI(
    title="Zoho CRM Lead API",
    version="1.0.0"
)

app.include_router(leads.router)
app.include_router(oauth.router)

@app.get("/")
async def root():
    return {"message": "Zoho CRM Lead API running"}

@app.get("/oauth/callback")
async def oauth_callback(request: Request):
    code = request.query_params.get("code")
    return {"message": "OAuth Callback Received", "code": code}