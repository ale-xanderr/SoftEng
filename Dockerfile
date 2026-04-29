# Use a lightweight official Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy ONLY the requirements file first. 
# This is a best practice for Docker layer caching.
COPY requirements.txt requirements.txt

# Install the dependencies
RUN pip install -r requirements.txt

# Now copy the rest of your application code
COPY . .

# Document that the app runs on port 5000
EXPOSE 5000

# Tell Docker how to run your application
CMD ["python", "app.py"]