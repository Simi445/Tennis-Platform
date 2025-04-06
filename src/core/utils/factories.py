from django.contrib.auth.models import User
from core.models import UserProfile

def create_user_with_role(username, password, email, role):
    user = User.objects.create_user(username=username, password=password, email=email)
    UserProfile.objects.create(user=user, role=role)
    return user
