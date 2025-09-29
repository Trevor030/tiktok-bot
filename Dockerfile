FROM python:3.11

# Imposta directory
WORKDIR /app

# Installa dipendenze di sistema per Playwright (TikTokApi le richiede)
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    gnupg \
    unzip \
    libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1 \
    libxss1 \
    libasound2 \
    libxtst6 \
    libx11-xcb1 \
    libgtk-3-0 \
    libdrm2 \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Copia i file
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia il resto del codice
COPY . .

# Installa Playwright (serve per TikTokApi)
RUN playwright install

# Comando principale
CMD ["python", "main.py"]
