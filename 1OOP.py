class User:
    def __init__(self, first_name, last_name, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}")

    def greeting_user(self):
        print(f"Hello {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        print(f"{self.login_attempts + 1}")

    def reset_login_attempts(self):
        print(f"{self.login_attempts * 0}")


user_1 = User("Jack", "Sparrow")
user_1.describe_user()
user_1.greeting_user()

user_2 = User("Sherlock", "Holmes")
user_2.describe_user()
user_2.greeting_user()

user_3 = User("Ronnie", "Coleman")
user_3.describe_user()
user_3.greeting_user()

user_1.increment_login_attempts()
user_3.reset_login_attempts()

user_4 = User("Lionel", "Messi", 5)
user_4.increment_login_attempts()
user_4.reset_login_attempts()


class Admin(User):
    def __init__(self, first_name, last_name, login_attempts=0,
                 privileges=["Allowed to add message", "Allowed to delete users", "Allowed to ban users"]):
        super().__init__(first_name, last_name, login_attempts)
        self.privileges = privileges
        # self.priv = priv

    def show_privileges(self):
        print(f"Admin {self.first_name} {self.last_name} has privileges: {self.privileges}")


admin_1 = Admin("Cristiano", "Ronaldo")
admin_1.show_privileges()


class Privileges(Admin):
    def __init__(self, privileges):
        super().__init__(privileges)

    def show_privileges(self):
        super().show_privileges()


priv_1 = Admin()
priv_1.show_privileges()
