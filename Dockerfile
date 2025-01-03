# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install necessary system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

    # Install necessary Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Create the output_files directory inside the container
RUN mkdir -p /app/output_files

# Copy the application code into the container
COPY . /app/
COPY story.txt /app/ 

# Expose the port (if required for APIs or applications)
EXPOSE 8000

# Run the application
CMD ["python", "app.py"]