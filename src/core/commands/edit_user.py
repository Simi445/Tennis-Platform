from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class EditUserCommand:
    def __init__(self, data):
        self.data = data

    def execute(self):
        user = get_object_or_404(User, id=self.data.get("user_id"))
        user.username = self.data.get("username")
        user.email = self.data.get("email")

        password = self.data.get("password")
        if password:
            user.set_password(password)

        user.save()
        return user  # Optional
