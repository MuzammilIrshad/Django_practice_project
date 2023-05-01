
# DJANGO PRACTICE 

## STEPS TO INSTALL DJANGO

1. Install Python [python 3](https://www.python.org/downloads/)
2. Install Django: **pip install Django**
3. Install Few Other dependencies to make Django Work: **pip install pytz sqlparse**

## STEPS TO START THE PROJECT:

1. Clone the Repo
2. Run cmd: "py manage.py runserver"
3. navigate to "http://127.0.0.1:8000/"

## STEPS TO CONNECT WITH SQLITE DB

1. Create Model in "models.py"
2. Connect project in "setting.py"
3. Run cmd: **py manage.py makemigrations**
4. Run cmd: **py manage.py migrate**
5. Run cmd: **py manage.py createsuperuser**
6. Navigate to [db url](http://127.0.0.1:8000/admin) 
7. Enter your credentials created in "step 5"