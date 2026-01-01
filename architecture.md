# Zoho CRM Lead API - Architecture and Flow

## Overview

This FastAPI application provides an integration with Zoho CRM for managing leads. It includes OAuth 2.0 authentication flow and CRUD operations for leads.

## Architecture

The application follows a layered architecture with clear separation of concerns:

```mermaid
graph TB
    A[FastAPI App] --> B[Routers Layer]
    B --> C[Services Layer]
    C --> D[Connectors Layer]
    D --> E[Zoho CRM API]

    B --> F[Models Layer]
    C --> F
    D --> G[Config Layer]

    H[OAuth Flow] --> B
    H --> I[External Browser]
```

### Layers Description

- **Routers Layer**: Handles HTTP requests and responses, defines API endpoints
- **Services Layer**: Business logic and data processing
- **Connectors Layer**: External API integrations and authentication
- **Models Layer**: Data models and validation using Pydantic
- **Config Layer**: Environment configuration and settings

## OAuth 2.0 Flow

The application implements Zoho's OAuth 2.0 authorization code flow:

```mermaid
sequenceDiagram
    participant U as User
    participant A as FastAPI App
    participant Z as Zoho CRM
    participant B as Browser

    U->>A: GET /zoho/oauth/url
    A-->>U: Authorization URL
    U->>B: Navigate to URL
    B->>Z: Authorization Request
    Z-->>B: Login & Consent
    B->>A: Redirect /oauth/callback?code=xyz
    A-->>U: Callback Response
    U->>A: POST /zoho/oauth/token {code: xyz}
    A->>Z: Exchange code for tokens
    Z-->>A: Access & Refresh Tokens
    A-->>U: Tokens Response
```

## API Flow

Once authenticated, users can perform lead operations:

```mermaid
sequenceDiagram
    participant U as User
    participant A as FastAPI App
    participant S as LeadsService
    participant C as ZohoConnector
    participant Z as Zoho CRM

    U->>A: GET /zoho/leads
    A->>S: get_leads()
    S->>C: get_access_token()
    C->>Z: GET Leads API
    Z-->>C: Leads Data
    C-->>S: Leads
    S-->>A: Leads
    A-->>U: Leads JSON

    U->>A: POST /zoho/leads {lead data}
    A->>S: create_lead(lead)
    S->>C: create_lead(lead)
    C->>Z: POST Leads API
    Z-->>C: Created Lead
    C-->>S: Response
    S-->>A: Response
    A-->>U: Success Response
```

## File Structure

```
├── main.py                 # FastAPI application entry point
├── routers/
│   ├── leads.py           # Lead-related endpoints
│   └── oauth.py           # OAuth-related endpoints
├── services/
│   └── leads_service.py   # Lead business logic
├── connectors/
│   ├── zoho.py           # Zoho CRM API client
│   └── zoho_auth.py      # OAuth token management
├── models/
│   ├── lead.py           # Lead data model
│   └── oauth.py          # OAuth data models
├── core/
│   └── config.py         # Application configuration
├── requirements.txt       # Python dependencies
└── postman_collection.json # API testing collection
```

## Key Components

### Authentication
- Uses Zoho OAuth 2.0 with authorization code grant
- Stores refresh tokens for automatic token renewal
- Handles token expiration and refresh

### API Endpoints
- `GET /` - Health check
- `GET /oauth/callback` - OAuth callback handler
- `GET /zoho/oauth/url` - Get authorization URL
- `POST /zoho/oauth/token` - Exchange code for tokens
- `GET /zoho/leads` - Retrieve leads from Zoho CRM
- `POST /zoho/leads` - Create new lead in Zoho CRM

### Data Models
- **Lead**: first_name, last_name, email, phone (optional)
- **AuthCode**: code (for OAuth token exchange)

### Configuration
Environment variables required:
- `CLIENT_ID` - Zoho OAuth client ID
- `CLIENT_SECRET` - Zoho OAuth client secret
- `REFRESH_TOKEN` - Zoho refresh token
- `ZOHO_BASE_URL` - Zoho CRM API base URL
- `REDIRECT_URI` - OAuth redirect URI
- `OAUTH_AUTH_URL` - Zoho authorization URL
- `OAUTH_TOKEN_URL` - Zoho token exchange URL

## Error Handling

The application includes proper error handling:
- HTTP exceptions for API errors
- Validation errors for malformed requests
- External API error propagation
- Logging for debugging

## Security Considerations

- OAuth 2.0 for secure authentication
- Environment variables for sensitive data
- Input validation using Pydantic models
- HTTPS recommended for production
- Token refresh handling