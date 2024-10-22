#!/bin/sh

if [ "$DATABASE" = "db" ]; then
    echo "Waiting for database..."

    while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
      sleep 0.1
    done

    echo "Database started"
fi

# Make migrations and migrate the database.
echo "Making migrations and migrating the database. "
python manage.py makemigrations  --noinput 
python manage.py migrate --noinput 

if [ "$DATABASE" ];
echo "Database up"
then
    echo "from django.contrib.auth.models import User" > createadmin.py
    echo "User.objects.create_superuser('neyruba', 'admin@neyruba.fr', 'neyruba123')" >> createadmin.py
    python manage.py shell < createadmin.py
fi
python manage.py collectstatic --noinput
exec "$@"