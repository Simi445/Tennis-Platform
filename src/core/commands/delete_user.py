from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class DeleteUserCommand:
    def __init__(self, user_id):
        self.user_id = user_id

    def execute(self):
        user = get_object_or_404(User, id=self.user_id)
        user.delete()
