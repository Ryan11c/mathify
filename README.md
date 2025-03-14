# Mathify - Full Stack Django Web Application
#### Live version of this project: [Live Server](https://mathify-app-330e6c4b0431.herokuapp.com/)
Mathify is a full-stack application developed using Python Django to help users collaborate on math problems. Users can log in, participate in discussions, and use various math calculators to enhance their understanding of mathematics. The tools I used were Python Django, HTML, CSS, and JavaScript.

## Features:
* User authentication (sign up, log in, and log out).
* Discussion forums for math topics.
* Built-in calculators.
* Responsive and user-friendly interface.

## Development vs. Production

| Feature          | Local Development         | Production                    |
| ---------------- | ------------------------- | ----------------------------- |
| **Static Files** | Served locally (static/)  | Stored on S3                  |
| **Media Files**  | Served locally (media/)   | Stored on S3                  |
| **Database**     | Local SQLite/PostgreSQL database  | Managed PostgreSQL on Heroku |

This repository is designed for **local development** purposes, where the application utilizes static files for serving assets like CSS, JavaScript, and images. The production version of this application is on a private repository and hosted on **Heroku**. I also integrated **Amazon S3 storage** for handling static and media files. 

## Table of Contents
1. [Setup](#setup)
2. [How to Run the Project](#how-to-run-the-project)
3. [Usage](#usage)
4. [Future Improvements](#future-improvements)

## Setup
#### Clone the Repository
1. Create a folder for the project.
2. Clone the repository into the folder:

   ```bash
   git clone https://github.com/Ryan11c/mathify.git
   ```

#### Create a Virtual Environment
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

#### Install Dependencies
1. Navigate into the `mathify` folder:

   ```bash
   cd mathify
   ```
2. Install required packages:

   ```bash
   pip install -r requirements.txt
   ```

#### Configure the Project for SQLite
1. In the `settings.py` file in `mathify/myProject/settings.py`, ensure the DATABASES section is configured for SQLite3 as the default database.
2. Also make sure to create your secret key and put it in the `.env` file in`mathify/myProject/.env`:
   ```
   SECRET_KEY=*******
   ```
3. If you intend to switch to a PostgreSQL database, you can uncomment the PostgreSQL configuration and replace the placeholder values with your actual credentials. The PostgreSQL configuration is already commented out in the default Django settings file for convenience:
   ```bash
   DATABASES = {
      'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
         # 'ENGINE': 'django.db.backends.postgresql',
         # 'NAME': os.environ.get('DB_NAME_PG'),
         # 'USER': os.environ.get('DB_USER_PG'),
         # 'PASSWORD': os.environ.get('DB_PASSWORD_PG'),
         # 'HOST': os.environ.get('DB_HOST_PG'),
         # 'PORT': os.environ.get('DB_PORT_PG'),
      }
   }
   ```
4. For PostgreSQL database, you put the following variables in the `.env` file, replacing `*******` with your own data:

   ```
   DB_NAME_PG=*******
   DB_USER_PG=*******
   DB_HOST_PG=*******
   DB_PORT_PG=*******
   DB_PASSWORD_PG=*******
   ```

## How to Run the Project
1. Apply migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
2. Create new superuser:

   ```bash
   python manage.py createsuperuser
   Username: admin
   Email address: admin@example.com
   Password: **********
   Password (again): *********
   Superuser created successfully.
   ```
3. Start the development server:

   ```bash
   python manage.py runserver
   ```
4. Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to explore the application.
5. Tip: The superuser will be the admin, meaning you can log into the admin section of Django.

## Usage
* Log in or sign up to start using Mathify:
<img src="https://github.com/user-attachments/assets/be3ac184-cf10-4914-9821-e266455b5b47" width=1050>

---

* Access the discussion forums to collaborate on math problems:
<img src="https://github.com/user-attachments/assets/26b93543-061e-4c4a-a499-c56a2cfaf897">

---

* Comment feature:
<img src="https://github.com/user-attachments/assets/42a91a34-9b96-4431-88cb-e73295a70f1a">

---

* Built-in calculators:
<img src="https://github.com/user-attachments/assets/0e7b88db-bea7-4555-9cfc-5a007262f3a8">

## Future Improvements
* Better authentication such as google or email/phone validator. The issue right now is that any email can be used. In future versions, I hope to implement a email or phone validator so the email used is legitimate. 
* More calculators such as matrix multiplication, inverse, determinant, and more. Can also include other math subjects such as discrete math, algebra, and geometry.
* Better comment section. In this current version, the comment section is pretty simple only being able to reply to a dicussion post. Some improvements can be comment likes/replies and filtration system.

### This project was very fun to make! I hope you guys enjoy it too 
