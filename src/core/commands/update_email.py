class UpdateEmailCommand:
    def __init__(self, user, new_email, confirm_email):
        self.user = user
        self.new_email = new_email
        self.confirm_email = confirm_email
        self.error = ""

    def execute(self):
        if self.new_email != self.confirm_email:
            self.error = "New email and confirmation do not match."
            return False

        self.user.email = self.new_email
        self.user.save()
        return True
