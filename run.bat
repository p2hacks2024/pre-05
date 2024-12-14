:: filepath: run_and_open.bat
@echo off
start cmd /k "python manage.py runserver"
timeout /t 1
start "" "http://127.0.0.1:8000/myapp/hakodate_restaurant/"