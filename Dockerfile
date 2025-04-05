# Base Python image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy project files
COPY . /app

# Install system dependencies
RUN apt-get update && apt-get install -y     build-essential     libpoppler-cpp-dev     pkg-config     python3-dev     && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Download spaCy language model
RUN python -m spacy download en_core_web_sm

# Expose the port
EXPOSE 8000

# Start the app
CMD ["bash", "start.sh"]