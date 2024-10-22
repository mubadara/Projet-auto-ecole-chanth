from django.contrib.auth.models import User
User.objects.create_superuser('neyruba', 'admin@neyruba.fr', 'neyruba123')
