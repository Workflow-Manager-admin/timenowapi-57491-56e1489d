from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timezone
from pydantic import BaseModel, Field


app = FastAPI(
    title="Time API Backend",
    description="Backend service providing an API endpoint to return the current server time in ISO 8601 format.",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "Time",
            "description": "Endpoints for retrieving current server time.",
        }
    ]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CurrentTimeResponse(BaseModel):
    """Response model for current time endpoint."""
    current_time: str = Field(
        ...,
        description="The current server time "
                    "in ISO 8601 format."
    )





@app.get("/", include_in_schema=False)
def health_check():
    """Health check endpoint (not shown in API docs)."""
    return {"message": "Healthy"}

# PUBLIC_INTERFACE
@app.get(
    "/current-time",
    response_model=CurrentTimeResponse,
    summary="Get server current time",
    description="Returns the server's current time in ISO 8601 format (UTC).",
    tags=["Time"],
    response_model_exclude_unset=True,
    responses={
        200: {
            "description": "Current server time in ISO 8601 format.",
            "content": {
                "application/json": {
                    "example": {"current_time": "2024-09-20T14:12:10.120Z"}
                }
            }
        }
    }
)
def get_current_time():
    """
    Returns the server's current time in ISO 8601 format (UTC).
    """
    now_utc = datetime.now(timezone.utc).replace(microsecond=0)
    return CurrentTimeResponse(current_time=now_utc.isoformat())
