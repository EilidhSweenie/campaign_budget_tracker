Create a Python Virtual Environment
```
python -m venv backend_env
backend_env\Scripts\activate
```

Install Requirements
```
python -m pip install -r requirements.txt
```

Deactivate Virtual Environemnt 
```
deactivate
```

Run Local Server
*Ensure in src/ directory*
```
py manage.py runserver
```

Migrate Database
```
python manage.py migrate
```