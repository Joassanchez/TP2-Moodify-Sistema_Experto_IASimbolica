# Imagen con Python, SWI-Prolog (PySwip) y dependencias para Moodify POC.
FROM python:3.12-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# SWI-Prolog sin GUI (motor que usa pyswip)
RUN apt-get update && apt-get install -y --no-install-recommends \
    swi-prolog-nox \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py reglas.pl ./
COPY logic ./logic
COPY ui ./ui

EXPOSE 8501

# Streamlit accesible desde fuera del contenedor
CMD ["streamlit", "run", "app.py", \
     "--server.address=0.0.0.0", \
     "--server.port=8501", \
     "--server.headless=true", \
     "--browser.gatherUsageStats=false"]
