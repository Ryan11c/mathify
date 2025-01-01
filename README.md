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

## Setup
### Clone the Repository
1. Create a folder for the project.
2. Clone the repository into the folder:
   ```bash
   git clone https://github.com/Ryan11c/mathify.git
   ```

### Create a Virtual Environment
1. Navigate to the folder.
2. Create and activate a virtual environment:
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
1. Create a `.env` file in the `myProject` directory inside `mathify`.
2. Add the following line, replacing `*******` with your own data:
   ```
    SECRET_KEY=*******
    DB_NAME_PG=*******
    DB_USER_PG=*******
    DB_HOST_PG=*******
    DB_PORT_PG=*******
    DB_PASSWORD_PG=*******
   ```
---

## How to Run the Project
1. Apply migrations:
   ```bash
   python manage.py migrate
   ```
2. Start the development server:
   ```bash
   python manage.py runserver
   ```
3. Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to explore the application.
---


## This project was very fun to make! I hope you guys enjoy it too 👍