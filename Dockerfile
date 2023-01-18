# Use the official Python runtime as the base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the required libraries
RUN pip install -r requirements.txt

# Copy the application code
COPY app /app

# Expose the port the app will run on
EXPOSE 5000

# Start the app
CMD ["python", "app.py"]