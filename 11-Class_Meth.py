class User:
    total_users = 0

    def __init__(self, username):
        self.username = username
        User.increment_user_count()

    @classmethod
    def increment_user_count(cls):
        cls.total_users += 1

    @classmethod
    def show_total_users(cls):
        print(f"Total registered users: {cls.total_users}")


u1 = User("Asif")
u2 = User("Ali")
u3 = User("Sara")

User.show_total_users()
