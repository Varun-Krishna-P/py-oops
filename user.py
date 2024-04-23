# Write your code below:
# example for class attributes
class User:
    default_language = "English"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age


user1 = User("asdf", 13)
print(f"name: {user1.name}, age: {user1.age}, default language: {User.default_language}")