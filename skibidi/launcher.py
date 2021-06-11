import os

os.system("rm db.sqlite3")
os.system("rm -rf backend/migrations")
os.system("python3 manage.py makemigrations backend")
os.system("python3 manage.py migrate")
os.system("python3 manage.py shell < filler.py")
os.system("python3 manage.py runserver")