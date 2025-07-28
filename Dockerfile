# Use minimal Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies (optional, remove if unnecessary)
RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy and install Python requirements
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy your full app
COPY . .

# Run your Flask app
CMD ["python", "app.py"]
