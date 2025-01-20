# Basis-Image mit Python 3.11
FROM python:3.11-slim

# Installiere Systemabhängigkeiten, einschließlich wkhtmltopdf
RUN apt-get update && apt-get install -y \
    wkhtmltopdf \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die requirements.txt und installiere Abhängigkeiten
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den gesamten Code ins Arbeitsverzeichnis
COPY . .

# Exponiere den Standard-Port (optional, abhängig von Render-Konfiguration)
EXPOSE 8000

# Startbefehl für die Flask-App mit Gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]
