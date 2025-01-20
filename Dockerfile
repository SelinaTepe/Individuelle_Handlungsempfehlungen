# Basis-Image mit Python
FROM python:3.11-slim

# Installiere wkhtmltopdf und andere Systempakete
RUN apt-get update && apt-get install -y \
    wkhtmltopdf \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die Abhängigkeiten
COPY requirements.txt requirements.txt

# Installiere Python-Abhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den Rest des Codes
COPY . .

# Exponiere Port 8000 für die Anwendung
EXPOSE 8000

# Startbefehl für die Anwendung
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]
