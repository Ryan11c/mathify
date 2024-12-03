# Mathify
Full-stack application using Python Django. Users can log in and discuss various math problems and use the built-in calculators provided by our website.

<<<<<<< HEAD
# Setup: 
The first thing to do is to clone the repository:
$ git clone https://github.com/Ryan11c/mathify.git 
$ cd mathify 

# Create a virtual environment to install dependencies in and activate it:
$ virtualenv2 --no-site-packages env 
$ source env/bin/activate 

# Then install the dependencies:
(env)$ pip install -r requirements.txt 
* Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.

# Once pip has finished downloading the dependencies: 
(env)$ cd project (env)$ python manage.py runserver