from user import User
from database import Database


user = User("Abhishek", "alice@example.com", "password123")
database = Database()

user.display_user_info()
 
database.save_user(user)
user.change_password("newpassword456")
