class Dog(object):
	"""docstring for Dog"""
	def __init__(self, name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender

# in this example we will access the class attributes
dog = Dog("fido", 5, "Male")
print(dog.name)
print(dog.age)
print(dog.gender)
		