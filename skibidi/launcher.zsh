mysql -u root -p < "db_instance_creator.sql"
rm -rf backend/migrations
rm -rf website/migrations
python3 manage.py makemigrations backend
python3 manage.py makemigrations website
python3 manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'test@example.com', 'admin')" | python3 manage.py shell
python3 manage.py shell < filler.py
python3 manage.py runserver
