# Use theofficial Python slim image
FROM python:3.9.6
# Set the working directory inside the container
WORKDIR /app
# Copy only requirements first to leverage caching
COPY requirements.txt .
# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt|
# Copy the rest of the application inside the contain
COPY • •
# Expose the FastAPI port
EXPOSE 8080
# Run the FastAPI application with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]