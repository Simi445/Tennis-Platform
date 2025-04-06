from django.contrib.auth import update_session_auth_hash

class UpdatePasswordCommand:
    def __init__(self, user, current_password, new_password, confirm_password):
        self.user = user
        self.current_password = current_password
        self.new_password = new_password
        self.confirm_password = confirm_password
        self.error = ""

    def execute(self, request):
        if not self.user.check_password(self.current_password):
            self.error = "Current password is incorrect."
            return False
        if self.new_password != self.confirm_password:
            self.error = "New password and confirmation do not match."
            return False
        if len(self.new_password) < 8:
            self.error = "Password must be at least 8 characters long."
            return False

        self.user.set_password(self.new_password)
        self.user.save()
        update_session_auth_hash(request, self.user)
        return True
