from django.contrib.auth import authenticate, login

class LoginUserCommand:
    def __init__(self, request):
        self.request = request
        self.username = request.POST.get("username")
        self.password = request.POST.get("password")
        self.user = None
        self.error = None

    def execute(self):
        self.user = authenticate(self.request, username=self.username, password=self.password)
        if self.user:
            login(self.request, self.user)
            return True
        else:
            self.error = "Invalid credentials"
            return False
