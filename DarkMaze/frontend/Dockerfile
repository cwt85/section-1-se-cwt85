# Use official Python image
FROM python:3.11

# Set working directory inside the container
WORKDIR /app

# Copy dependencies file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Expose port for external access
EXPOSE 8088

# Run FastAPI app with Uvicorn
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8088", "--reload"]
