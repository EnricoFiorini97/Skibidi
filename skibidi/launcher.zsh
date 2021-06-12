mysql -u root -p < "db_instance_creator.sql"
rm -rf backend/migrations
python3 manage.py makemigrations backend
python3 manage.py migrate
python3 manage.py shell < filler.py
python3 manage.py runserver
