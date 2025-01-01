# Mathify 😀
Mathify is a full-stack application developed using Python Django to help users collaborate on math problems and access built-in calculators for various math topics, including calculus and linear algebra. Users can log in, participate in discussions, and leverage powerful tools to enhance their understanding of mathematics.

## Features:
* User authentication (sign up, log in, and log out).
* Discussion forums for math topics.
* Built-in calculators for problems in calculus, linear algebra, and more.
* Responsive and user-friendly interface.


## Table of Contents
1. [Setup](#setup)
2. [How to Run the Project](#how-to-run-the-project)
3. [Usage](#usage)
4. [Future Enhancements](#future-enhancements)
5. [Contributing](#contributing)
6. [Contact](#contact)

## Setup: 
* The first thing to do is create a folder.
* Then clone the repository into that folder:
* $ git clone https://github.com/Ryan11c/mathify.git 

## Create a virtual environment to install dependencies in and activate it:
* On Windows: 🪟
* $ python -m venv venv
* $ . venv/Scripts/activate
* Notice the virtual environment is in the root directory of the folder, not inside mathify.

## Then install the dependencies:
* (venv)$ cd mathify 
* (venv)$ pip install -r requirements.txt 
* Note the (venv) in front of the prompt. This indicates that this terminal session operates in a virtual environment.

## Create your own secret key:
* Create a .env file in myProject directory
* Inside, put SECRET_KEY=*******
* replace ******* with your secret key

## Once pip has finished downloading the dependencies: 
* (venv)$ python manage.py makemigrations
* (venv)$ python manage.py migrate
* (venv)$ python manage.py runserver

## This project was very fun to make! I hope you guys enjoy it too 👍