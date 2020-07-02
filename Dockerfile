# Install base image
FROM python:3.7-slim-buster

RUN pip install Flask

# Copy source code to container
ADD . /app

# Set working directory to /app
WORKDIR /app

# Install required dependencies
RUN pip install -r requirements.txt

# Declare environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Expose the port for Flask
EXPOSE 5000

# Run Flask!
CMD ["flask", "run", "--host=0.0.0.0"]
