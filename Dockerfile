# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy all project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (if needed)
EXPOSE 8000

# Run the app
CMD ["python", "main.py"]
