from django.contrib.auth.models import User
for u in User.objects.filter(is_superuser=True):
    print(u.username, u.email)
