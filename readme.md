# Support desk

To install:

1. 
```
virtualenv venv
```

2. 
```
cd venv/scripts
activate
```

3. 
```
pip install -r requirements.txt
```

4. 
```
pip install django-crispy-forms
```

5. 
```
python manage.py migrate
```

6. 
```
python manage.py collectstatic
```

7. 
```
python manage.py runserver
```