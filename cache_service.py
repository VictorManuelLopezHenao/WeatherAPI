import redis
import json
from config import settings

#conexion a Redis
redis_client = redis.Redis(
    host=settings.redis_host,
    port=settings.redis_port,
    db=settings.redis_db,
    decode_responses=True #-> convierte los datos de bytes a strings 
    ) 

#busca redis con clave y si los encuentra lo convierte de JSON a dict
async def get_cache(key : str):
    value = redis_client.get(key)
    if value:
        return json.loads(value)  #convierte de json a diccionario
    return None 

#guarda un dict como JSON string y lo expira despues del ttl definido
async def set_cache(key: str, data:dict, ttl: int = 3600):   #ttl = tiempo de expiracion en segundos
    redis_client.setex(key, ttl, json.dumps(data))  #convierte nuevamente a JSON string 