# Basis-Image mit Python
FROM python:3.11-slim

# Installiere Systempakete einschließlich wkhtmltopdf
RUN apt-get update && apt-get install -y \
    wkhtmltopdf \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die Python-Abhängigkeiten
COPY requirements.txt .

# Installiere Python-Abhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den restlichen Code in das Arbeitsverzeichnis
COPY . .

# Exponiere den Port 8000
EXPOSE 8000

# Starte die Anwendung mit Gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]
