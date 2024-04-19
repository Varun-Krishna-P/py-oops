# default arguments

class Dog:

	def __init__(self, name, age, gender="Male"):
		self.name = name
		self.age = age
		self.gender = gender


dog = Dog("fido", 5)
print(dog.name)
print(dog.age)
print(dog.gender)
