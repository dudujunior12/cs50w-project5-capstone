# CS50W Project5 Capstone

## Linux Configuration

### Install Git

    sudo apt install git

### Clone Project

    git clone https://github.com/dudujunior12/cs50w-project5-capstone

### Change directory

    cd cs50w-project5-capstone

### Install and Configure Virtual Environment

    sudo apt-get python3-virtualenv
    python3 -m venv venv
    source venv/bin/activate

### Download dependencies

    pip install -r requirements.txt

Set .env file

    touch .env

#### With your favorite editor edit the file and include the line below

    SECRET_KEY=*GENERATE A SECRET KEY*

ex: https://djecrety.ir/

### Migrate django models

    python3 manage.py makemigrations manga
    python3 manage.py migrate

### Run server

    python3 manage.py runserver
