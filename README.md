# Example Flask app

This is an example Flask application that you will use to explore the CI/CD pipeline.

## Init your development environment (on local computer)

Create a simple python application in your Visual Studio IDE and create a python script with the following code.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world! (v1)'

app.run(host='0.0.0.0', port=5000)
```

In this example, we create a Web Application using the Flask framework in Python. The script creates a server and
demonstrates how to print a simple message on the browser.

> Flask is a micro web framework written in Python. It is classified as a microframework because it does not require
particular tools or libraries. It has no database abstraction layer, form validation, or any other components where
pre-existing third-party libraries provide common functions.

### Run the app

To run the script in your computer, you will need to install Flask:

`pip install flask`

Then, you can run it using the following command:

`python3 app.py`

### How to containerise the app?

Before you continue, you must install Git on your local computer. Follow the guide below to download and install Git,
then return to this tutorial.

* [Installation guide for Windows, Mac and Linux users](https://github.com/git-guides/install-git)

> **<u>For Windows users</u>, please use the following step-by-step guide: https://phoenixnap.com/kb/how-to-install-git-windows** 
>
> Install **git bash** and then restart your Visual Studio IDE.

Create a private repository and push it to GitHub following the commands below:

1. Init an empty Git repository.

```bash
$ git init
```

2. Add a new remote to your repo (this should be in one single line).

```bash
$ git remote add origin https://YOUR_GIT_USERNAME:YOUR_GIT_TOKEN@YOUR_GIT_REPO
```

* Add all files and folders.

```bash
$ git add . 
```

3. Commit the changes to the repo.

```bash
$ git commit -m "Create a sample web app"
```

4. Upload local repository content to a remote repository.

```bash
$ git push -f origin master
```

> At this point, refresh your GitHub page; your files/folders should be there now!
>
> Now, go to your VM in GCP!

#### Deploy the web application on your GCP VM

1. Open a terminal connection to the GCP VM. You can connect from VSC or using the SSH button (in GCP).
2. In the VM, make sure you are already logged in as docker-user (from Lab 5.1). 
3. Let's clone our GitHub repo.

```bash
$ git clone --branch main https://YOUR_GIT_USERNAME:YOUR_GIT_TOKEN@YOUR_GIT_REPO
```

4. Your repo should now be in your VM; run `ls` to check it out.

```bash
$ ls

flask-app
```

5. Change the current working directory (move to the folder which contains the content of your repo).

```bash
$ cd flask-app
```

6. Package your python scripts into a docker image following the set of  if the Dockerfile.

The Dockerfile is used for specifying a set of instructions to follow in order to assemble an image.

_**Note: before building the image review the set of instructions in the Dockerfile using a text editor (e.g. `pico`)**_

```bash
# press ctrl+x to exit the editor
pico Dockerfile
```

Build the image now!
```bash
$  docker build -t flask .
```

13. Run the container using the newly created image abd expose it to the port 5000.

```bash
$ docker run -d -p 5000:5000 flask
```

> `-d` run process in the background. 

14. Try to access your service in the browser; you just created your first containerised app!:checkered_flag: Well done! 
