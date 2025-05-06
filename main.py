from fastapi import FastAPI, HTTPException, status
from weather_service import fetch_weather

app = FastAPI()

@app.get("/weather/{city}")
async def get_weather(city : str):

    weather_data = await fetch_weather(city) # Llamamos a la función fetch_weather para obtener los datos

    if "error" in weather_data:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Ciudad no encontrada")
    
    return weather_data

