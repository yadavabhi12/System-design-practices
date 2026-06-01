class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def display_user_info(self) -> None:
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")

   