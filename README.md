# Example Flask app

This is an example Flask application that you will use to explore the CI/CD pipeline.

To run the script in your computer, you will need to install Flask:

`pip install flask`

Then, you can run it using the following command:

`python3 app.py`

# How to containerise the app?

#### On your local computer

1. Open visual studio code and create a simple node.js application. Follow the video to create a new application that looks like this:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world! (v1)'

app.run(host='0.0.0.0', port=5000)
```

2. In this example, we used a Node js server for demonstration reasons. The script creates an express server and demonstrates how to print a simple message on the browser.
3. Node.js is an open-source, cross-platform, back-end runtime environment that enables developers to run JavaScript code outside a web browser. It is built on the V8 JavaScript engine used in Google Chrome, and it allows developers to use JavaScript to write server-side code, as well as command-line tools and scripts.

4. Before you continue, you must install GitHub on your local computer. Follow the following guide to download and install GitHub, then return to this tutorial.

* [Installation guide for Windows, Mac and Linux users](https://github.com/git-guides/install-git)

> **<u>For Windows users</u>, please use the following step-by-step guide: https://phoenixnap.com/kb/how-to-install-git-windows** 
>
> * Install **git bash** and then restart your visual studio code.
>
> Then you can start a new GitBash to run the git commands as follows.
>
> ![vsc-win](/Users/steliossotiriadis/Dropbox/AA-Birkbeck/A-Cloud-Workhop/Session2-Containers/images/vsc-win.png)

* It might worth to revise [Lab3.2-Pushing-code-to-GitHub.md](https://github.com/steliosot/cc/blob/master/Class-3/Lab3.2-Pushing-code-to-GitHub.md)

5. We will create a new Private repo in this tutorial, so make sure you follow the steps as presented in the video. The commands include:

* See git version.

```bash
$ git --version
```

* Initialise a git in your folder.

```bash
$ git init
```

* Add remote repo from git (this should be in one single line).

```bash
$ git remote add origin https://YOUR_GIT_USERNAME:YOUR_GIT_TOKEN@YOUR_GIT_REPO
```

* Add all files and folders.

```bash
$ git add . 
```

* Commit the changes to the repo

```bash
$ git commit -m "Pushing my app files"
```

* Upload the files in the repo

```bash
$ git push -f origin master
```

> At this moment, refresh your GitHub page; your files/folders should be there now!
>
> Now go to your VM!

#### On your GCP VM or in your Google shell

6. Open a terminal connection to the GCP VM. You can connect from VSC or using the SSH button (in GCP).
7. In the VM, make sure you are already logged in as docker-user (from Lab 5.1). 
8. Let's clone our GitHub repo.

```bash
$ git clone --branch master https://github.com/steliosot/flask-app
```

9. Your repo should now be in your VM; run `ls` to check it out.

```bash
$ ls

flask-app
```

10. Enter in the repo folder.

```bash
$ cd flask-app
```

11. Create a new Dockerfile as follows (e.g. using `pico`)

`sudo pico Dockerfile`

```dockerfile
FROM ubuntu

RUN apt update
RUN apt install python3-pip -y
RUN pip3 install Flask

WORKDIR /app

COPY . .

CMD ["python3","-m","flask","run","--host=0.0.0.0"]
```

> Save and exit (ctrl+s and then ctrl+x).

12. Build the image.

```bash
$  docker build -t flask .
```

13. Run the container.

```bash
$ docker run -d -p 5000:5000 flask
```

> `-d` run process in the background. 

14. Try to access your service in the browser; you just created your first containerised app!:checkered_flag: Well done! 
