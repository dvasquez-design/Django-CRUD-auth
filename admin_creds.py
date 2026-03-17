from django.contrib.auth.models import User

User.objects.create_superuser('admin', 'admin@email.com', '123456789')
