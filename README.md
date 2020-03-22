# health-monitor-team7
health-monitor-team7 created by GitHub Classroom

## Directions for set-up (Mac), for Windows: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

### get a virtual environment
 
        python3 -m venv env

### activate it

        source env/bin/activate

### install requirements

        pip install -r requirements.txt

### run

        python3 flaskApp.py

### Also, if you install anything in your virtual environment, make sure after you pip install to:

        pip freeze >> requirements.txt

    this will store your requirements so everyone won't have any module installation problems.