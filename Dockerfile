FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# 🛠 Install system packages needed for OpenCV
RUN apt-get update && apt-get install -y libgl1

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port if needed
EXPOSE 8000

# Run the app
CMD ["python", "app/main.py"]
