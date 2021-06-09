import os

os.system("rm db.sqlite3")
os.system("rm -rf backend/migrations")
os.system("python manage.py makemigrations backend")
os.system("python manage.py migrate")
os.system("python manage.py shell < filler.py")