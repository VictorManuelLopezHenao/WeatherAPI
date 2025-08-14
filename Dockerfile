# Usa una imagen base oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requerimientos e instala dependencias
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copia el código del proyecto
COPY . .

# Expone el puerto que usa Uvicorn
EXPOSE 8000

# Comando para arrancar la API con recarga (útil en desarrollo)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
