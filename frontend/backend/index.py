from flask import Flask
import subprocess

app = Flask(__name__)


@app.route('/test')
def hello():
    return "Hello World!"

@app.route('/create_container')
def run_docker_container():
    # get a python file
    # store it there
    # create a docker build
    file_name = ""
    # docker-compose run python file_name
    subprocess.Popen(['docker-compose', 'build', '.'])
    subprocess.Popen(['docker-compose', 'run', 'python_service', 'python3', file_name])

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
