from user import User
class Database:
    def __init__(self):
        self.users = []

    def save_user(self, user: User) -> None:
        self.users.append(user)
        print(f"User {user.name} saved to database.")

    def change_user_email(self, user: User, new_email: str) -> None:
        user.email = new_email
        print(f"User {user.name}'s email changed to {new_email} in database.")
