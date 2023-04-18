# `python:3.11-slim` image is a lightweight, production-ready Python environment for running Python applications
# in a Docker container. The slim variant of the Python image is smaller than the stretch variant and is optimized for
# production use cases where a smaller image size is preferred.

# Using this image as the base allows you to build a containerized version of your Flask app with the necessary Python
# dependencies without having to install and manage those dependencies on the host machine instead of using the a OS and
# configuring it using a set of instructions in the Dockerfile see the
FROM python:3.11-slim

# Create app directory
WORKDIR /app

# Install app dependencies
# Make sure you have the `requirements.txt` file in the root directory of the project with the required dependencies.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# OPTIONAL as the `-p` flag is used while running the container
EXPOSE 5000

CMD ["python", "app.py"]