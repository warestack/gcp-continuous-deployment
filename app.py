from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, this is the version `1.0.0` of your flask app'


# When you containerize your Flask app using Docker and expose it to the outside world, you need to specify the host
# parameter in the app.run() function to make the app accessible from outside the container.

# When you run a Flask app inside a Docker container, the default host value localhost refers only to the local
# container, not to the outside world. To make a Flask app accessible from outside the container, you need to set the
# host parameter to 0.0.0.0 so that it listens on all network interfaces.

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
