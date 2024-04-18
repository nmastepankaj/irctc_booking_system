# IRCTC Booking System (WorkIndia Assignment)
I have completed this interesting assignmend given by Workindia. Worked well on each required statement of the assignment.

- Implement JWT Authentication for User Authentication
- API key Authentication for the Admin Site (Add header `X-IRCTC-API-KEY-SECRET` in the All admin API's)
- Handles race conditions while booking
    - If more than 1 users simultaneously try to book seats, only either one of the users should be able to book (By adding database lock)
- Focused on code quality and vaidation

## Assumptions

- Train is running only between source and destination


## Tech Stack Used

- Python
- Django
- MySQL

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

To access the Admin API you need to create token ( using function `generate_api_key` present in `utils/token.py`) and add to the db `AdminSecret` manually.
To access the user API you need to register then login where you get the access token. Then you this token for user api which starts with `/api/user/`


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

- Login User
![Screenshot (1008)](https://github.com/nmastepankaj/irctc_booking_system/assets/68346633/2f775b68-4d11-4c1e-b8d3-38901d2407de)

- Register User
![Screenshot (1007)](https://github.com/nmastepankaj/irctc_booking_system/assets/68346633/40a1b32c-7dc4-4946-b8a7-089125d2ab33)

- Book Ticket API
![Screenshot (1009)](https://github.com/nmastepankaj/irctc_booking_system/assets/68346633/d5c2640a-364f-4fcf-817f-3deaad5c5cca)

- Get train between source and destination
![Screenshot (1010)](https://github.com/nmastepankaj/irctc_booking_system/assets/68346633/8494633e-2be0-405f-b073-6633163c4d36)

- Get Booking Details
![Screenshot (1011)](https://github.com/nmastepankaj/irctc_booking_system/assets/68346633/eecdf245-e9cd-4fd9-b99a-2b18850ac202)

- Add Train
![Screenshot (1012)](https://github.com/nmastepankaj/irctc_booking_system/assets/68346633/e9a8f553-7dfd-413c-a92a-0c43add39493)

- Add Train Schedule
![Screenshot (1013)](https://github.com/nmastepankaj/irctc_booking_system/assets/68346633/e7496fb5-027c-4149-b6f2-a9c5768dea2d)

- Update Train Schedule
![Screenshot (1014)](https://github.com/nmastepankaj/irctc_booking_system/assets/68346633/3adb1754-7709-4142-86ac-abb707b30d96)
