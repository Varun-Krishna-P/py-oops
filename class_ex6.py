# updating the instance attribute
class Dog(object):
	"""docstring for Dog"""
	def __init__(self, name, age, gender='male'):
		self.name = name
		self.age = age
		self.gender = gender


# updating the instance attributes

dog = Dog("Fiddo", 5)
print(f"name: {dog.name}, age: {dog.age}, gender: {dog.gender}")
print("updating the name attribute")
dog.name = "Fido"
print(f"name: {dog.name}, age: {dog.age}, gender: {dog.gender}")

