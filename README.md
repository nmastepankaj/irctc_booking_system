# IRCTC Booking System (WorkIndia Assignment)
I have completed this interesting assignmend given by Workindia, 

## Steps To Setup Project

First clone the github repository

```bash
  git clone https://github.com/nmastepankaj/irctc_booking_system.git
```

Open the repository folder in any code editor (VS code) or open any terminal.

You need to create virtual environment for the project. If you don't have virtualenv the install it using the below command :-

```bash
  virtualenv venv
```

Now, activate the virtual environment using the below command.
If you're window user :-

```bash
  ./venv/Scripts/activate
```


If you're linux user :-

```bash
  source venv/bin/activate
```

install all the project requirements

```bash
  pip install -r requirement.txt
```


Now, you need to create migrations and migrate all the migrations

```bash
  python manage.py makemigrations
  python manage.py migrate
```

Create super user for your project

```bash
  python manage.py createsuperuser
```

Run your project

```bash
  python manage.py runserver
```

Now your application is ready to use. First register a user and login with the provided credentials.


## API Endpoints


The app defines following CRUD APIs.

    POST /api/public/account/register
    
    POST /api/public/account/login
    
    POST /api/user/booking/book_ticket
    
    GET /api/user/booking/get_trains
    
    GET /api/user/booking/get_booking/{booking_uuid}

    POST /api/admin/booking/add_train

    POST /api/admin/booking/add_train_schedule

    PATCH /api/admin/booking/update_train_schedule/{schedule_id}


## Screenshots of the working API
