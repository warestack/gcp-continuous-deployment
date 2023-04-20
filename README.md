# gcp-continuous-deployment

This is an example Flask application that you will use to explore the Continuous Deployment pipeline on GCP compute
instances using Docker and GitHub workflows.

## Prerequisites

GCP instance and VPC network need to be configured to allow HTTP(S) traffic on both the pre-defined port (5000) for
exposing the container and the instance itself for getting access to it using the `gcloud compute ssh` command.

You can use this Terraform [repository](https://github.com/warestack/terraform-gcp-compute-instance) to provision the
minimum resources in GCP or create a compute instance and its VPC network and firewall rules using the Google cloud
console.

## Init your development environment (on local machine)

Create a simple python application in your Visual Studio IDE and create a python script with the following code.

```python
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
```

In this example, we create a Web Application using the Flask framework in Python. The script creates a server and
demonstrates how to print a simple message on the browser.

> Flask is a micro web framework written in Python. It is classified as a microframework because it does not require
particular tools or libraries. It has no database abstraction layer, form validation, or any other components where
pre-existing third-party libraries provide common functions.

### Test the app

To run the script on your machine, you will need to install Flask:

```bash
pip install flask
```

Then, you can run it using the following command:

```bash
python3 app.py
```

### Init your Git repository

Before you continue, you must install Git on your local machine. Follow the guide below to download and install Git,
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
$ git push -f origin main
```

> At this point, refresh your GitHub page; your files/folders should be there now!
>
> Now, go to your VM in GCP!

## Deploy the web application on your GCP VM (manually)

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

6. Package your python scripts into a docker image.

The Dockerfile is used for specifying a set of instructions to follow in order to assemble an image.

_**Note: before building the image review the set of instructions in the Dockerfile using a text editor (e.g. `pico`)**_

```bash
# press ctrl+x to exit the editor
pico Dockerfile
```

It's to build the image now!
```bash
$  docker build -t flask .
```

13. Run the container using the newly created image abd expose it to the port 5000.

```bash
$ docker run -d -p 5000:5000 flask
```

> `-d` run process in the background. 

14. Try to access your service in the browser; you just created your first containerised app!:checkered_flag: Well done! 

## Continuous Deployment of the web application on your GCP VM (using the GitHub workflow)

1. Enable GitHub workflows, navigate to the **Actions** page of the repository and enable the main workflow.
2. Encode the content of the Terraform service account JSON file in `BASE64` format and store it as a secret named
   `GCP_TF_SA_CREDS_BASE64` on GitHub, in a new GitHub environment with protection rules is preferred. See the following
   [link](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment)
   for setting a new GitHub environment. If you do so, make sure that the right environment is defined in the 
   `build_and_deploy.yaml` workflow. You can find instructions on how to create the service account 
   [here](https://github.com/warestack/terraform-gcp-compute-instance#google-apis-and-iam-roles).

    ```yaml
    name: Setup, Build, Deploy and Publish
    on:
      push:
        branches:
          - 'main'
      release:
        types: [created]
    
    jobs:
      setup-build-deploy-publish:
        name: Setup, Build, Deploy and Publish
        runs-on: ubuntu-latest
        environment: <your_new_environment>
        env:
          PROJECT_ID: ${{ secrets.GCP_PROJECT_ID }}
          GCP_ZONE: ${{ secrets.GCP_ZONE }}
          INSTANCE_NAME: ${{ secrets.INSTANCE_NAME }}
          IMAGE_NAME: docker-image
          CONTAINER_NAME: docker-container
          WORKING_DIR: app
          GITHUB_REPO_URL: ${{ secrets.REPO_URL }}
        steps:
          # ...workflow-specific steps
    ```
   
4. Create the `GCP_PROJECT_ID`, `GCP_ZONE`, `INSTANCE_NAME` and `REPO_URL` on GitHub or set the env variables directly
   in the `build_and_deploy.yaml` workflow as these variables are not confidential.
5. Push the main branch (`force push` if you have not applied any change) to trigger the workflow. You can use the 
   GitHub workflow status page to monitor the progress of the workflow.

## For any questions, suggestions, or feature requests

Get in touch with us:

- Email [dimitris@waresatck.io](mailto:dimitris@warestack.io?subject=[GitHub]%20Source%20Han%20Sans),
  [stelios@waresatck.io](mailto:stelios@warestack.io?subject=[GitHub]%20Source%20Han%20Sans)
- [LinkedIn account](https://www.linkedin.com/in/dimitris-kargatzis-1385a2101/)

## License

License under the MIT License (MIT)

Copyright © 2022 [Warestack, ltd](https://github.com/warestack)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.

IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
