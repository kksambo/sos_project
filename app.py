from twilio.rest import Client
import uvicorn
import fastapi
import os
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = fastapi.FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Location(BaseModel):
    latitude: float
    longitude: float
    
@app.get("/contact")
async def sos_alert():
    latitude = location.latitude
    longitude = location.longitude
    location_url = f"https://www.google.com/maps?q={latitude},{longitude}"
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")

    if not account_sid or not auth_token:
        return {"error": "Twilio credentials not set"}

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=f'hi refilwe you have an emergency alert  Location: {location_url}',
        to='whatsapp:+27672531917'
    )

    return {"message_sid": message.sid}
