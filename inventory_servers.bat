@echo off
echo Starting Redis Server...
start "E:\Blooprint Consulting\inventory-app-api\Redis-x64-3.0\redis-server.exe"
timeout 5  :: Wait for 5 seconds to ensure Redis starts properly

echo Starting Django Development Server...
cd "E:\Blooprint Consulting\inventory-app-api\inventory_system"  :: Change to the Django project directory

:: Activate the virtual environment
call "E:\Blooprint Consulting\inventory-app-api\env\Scripts\activate.bat"  :: Update the name if your virtual environment is named differently

:: Start the Django development server
start cmd /k "python manage.py runserver"
