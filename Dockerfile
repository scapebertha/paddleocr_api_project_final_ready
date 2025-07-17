FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install OS-level dependencies for OpenCV (cv2)
RUN apt-get update && apt-get install -y libgl1 libglib2.0-0 libhdf5-dev

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "app/main.py"]
