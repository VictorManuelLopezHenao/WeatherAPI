import httpx  #realizar solicitudes http - consumir APIS
from config import settings
import os

async def fetch_weather(city : str):
    BASE_URL = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}"
   
    params = {
        "key": os.getenv("API_KEY"),  #variables de entorno
        "unitGroup":"metric",
        "elements":"temp,precip,humidity",
        "include":"days"
    }

    async with httpx.AsyncClient() as client:  #abre una sesión asíncrona para hacer solicitudes HTTP
        response = await client.get(BASE_URL, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return{
            "error":"No se pudo obtener los datos"
        }


