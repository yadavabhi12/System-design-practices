class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    

    def display_user_info(self) -> None:
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")

    def change_password(self, new_password: str) -> None:
        self.password = new_password
    

    def save_to_database(self) -> None:
        # Code to save user info to database
        print("Saving user info to database...")
        # Simulate database save with a print statement
        print(f"User {self.name} saved to database.")
    

    def change_database_info(self, new_email: str) -> None:
        # Code to change user info in database
        print("Changing user info in database...")
        # Simulate database update with a print statement
        print(f"User {self.name}'s email changed to {new_email} in database.")





User = User("Alice", "alice@example.com", "password123")
User.display_user_info()
User.change_password("newpassword456")
User.save_to_database()
User.change_database_info("alice_new@example.com")
