python3 manage.py makemigrations --no-input
sleep 10
python3 manage.py migrate --no-input
sleep 10
python3 manage.py runserver 0.0.0.0:8000