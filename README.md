# Install requirement libraries
pip install -r ./requirements.txt

## Run database 
python manage.py makemigrations
python manage.py migrate

## Run app
python manage.py runserver

## Admin account
```
lathequyen
123456
```