from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from core.utils.factories import create_user_with_role

class RegisterUserCommand:
    def __init__(self, request):
        self.request = request
        self.username = request.POST.get("username")
        self.email = request.POST.get("email")
        self.password = request.POST.get("password")
        self.confirm_password = request.POST.get("confirm_password")
        self.user_type = request.POST.get("user_type")
        self.error = None
        self.user = None

    def execute(self):
        if User.objects.filter(username=self.username).exists():
            self.error = "Username already exists"
            return False

        if self.password != self.confirm_password:
            self.error = "Passwords do not match"
            return False

        self.user = create_user_with_role(
            username=self.username,
            email=self.email,
            password=self.password,
            role=self.user_type
        )

        auth_user = authenticate(self.request, username=self.username, password=self.password)
        if auth_user:
            login(self.request, auth_user)
            return True
        else:
            self.error = "Authentication failed"
            return False
