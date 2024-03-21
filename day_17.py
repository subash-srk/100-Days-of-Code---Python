class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


class Car:
    def __init__(self):
        pass


user1 = User("001", "Subash K")
print(user1.name)

user2 = User("002", "Ariana")

user1.follow(user2)
print(user1.following)
print(user1.followers)
print(user2.following)
print(user2.followers)
