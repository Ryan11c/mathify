# Mathify 😀
Mathify is a full-stack application developed using Python Django to help users collaborate on math problems and access built-in calculators for various math topics, including calculus and linear algebra. Users can log in, participate in discussions, and leverage powerful tools to enhance their understanding of mathematics. The tools I used were Python Django, HTML, CSS, and JavaScript.

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

## 1. Setup
### Clone the Repository
1. Create a folder for the project.
2. Clone the repository into the folder:
   ```bash
   git clone https://github.com/Ryan11c/mathify.git
   ```

### Create a Virtual Environment
1. Navigate to the folder.
2. Create and activate a virtual environment: Make sure to use python version 3.12.3 when creating this virtual environment. This ensures all packages will work.

   **On Windows:**
   ```bash
   python -m venv venv
   . venv/Scripts/activate
   ```
   **On macOS/Linux:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Notice the virtual environment is in the root directory of the folder, not inside mathify.

### Install Dependencies
1. Navigate into the `mathify` folder:
   ```bash
   cd mathify
   ```
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Configure the Project
1. Set up postgres database with your chosen host.
2. Create a `.env` file in the `myProject` directory inside `mathify`.
3. Add the following line, replacing `*******` with your own data:
   ```
    SECRET_KEY=*******
    DB_NAME_PG=*******
    DB_USER_PG=*******
    DB_HOST_PG=*******
    DB_PORT_PG=*******
    DB_PASSWORD_PG=*******
   ```

## 2. How to Run the Project
1. Apply migrations:
   ```bash
   python manage.py migrate
   ```
2. Create new superuser:
   ```bash
   python manage.py createsuperuser
   ```
   * Follow directions and create the user!
3. Start the development server:
   ```bash
   python manage.py runserver
   ```
4. Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to explore the application.
5. Tip: The superuser will be the admin, meaning you can log into the admin section of Django.

## 3. Usage
1. Log in or sign up to start using Mathify.
2. Access the discussion forums to collaborate on math problems.
3. Use the built-in calculators for solving problems related to calculus, linear algebra, and more.

## 4. Future Enhancements
1. Better authentication such as google or email/phone validator
2. APIs!!

## This project was very fun to make! I hope you guys enjoy it too 👍😎