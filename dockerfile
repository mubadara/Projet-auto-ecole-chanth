# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project into the container
COPY . /app/

WORKDIR /app/mysite/


# Make entrypoint.sh executable
RUN chmod +x /app/entry-point.sh

# Specify the entrypoint script
ENTRYPOINT ["/app/entry-point.sh"]

# Default command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
