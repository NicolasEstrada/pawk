# Use an official Python runtime as a base image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copying rest of files into app folder
ADD . /app

# Run app.py
CMD ["python", "app.py"]
