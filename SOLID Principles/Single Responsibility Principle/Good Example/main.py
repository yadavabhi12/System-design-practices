from user import User
from database import Database


user = User("Abhishek", "alice@example.com", "password123")
database = Database()

user.display_user_info()

database.save_user(user)
database.change_user_email(user, "alice_new@example.com")
