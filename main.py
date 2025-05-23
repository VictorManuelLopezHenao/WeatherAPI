from fastapi import FastAPI, HTTPException, status
from weather_service import fetch_weather
from cache_service import get_cache, set_cache

app = FastAPI()

@app.get("/weather/{city}")
async def get_weather(city : str):
    cache_key = f"weather:{city.lower()}"

    #Buscar en Redis
    cached_data = await get_cache(cache_key)
    if cached_data:
        return {
            "data": cached_data,
            "source":"cache"
        } 
    
    #Si no hay en cache, buscar en la API externa
    weather_data = await fetch_weather(city) # Llamamos a la función fetch_weather para obtener los datos

    if "error" in weather_data:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Ciudad no encontrada")
    
    
    #Guardar en cache
    await set_cache(cache_key, weather_data)

    return{
        "data": weather_data, 
        "source": "API"
    }



