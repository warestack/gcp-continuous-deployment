FROM ubuntu

# Create app directory
WORKDIR /app

# Install app dependencies
RUN apt update
RUN apt install python3-pip -y
RUN pip3 install Flask

COPY . .

# OPTIONAL as the `-p` flag is used while running the container
EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
