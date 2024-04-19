# itetrating over the instances
class Dog(object):
	"""docstring for Dog"""
	def __init__(self, name, age, gender="male"):
		self.name = name
		self.age = age
		self.gender = gender


dog1 = Dog("fido", 5)
dog2 = Dog("Puppy", 10, "female")

#itetrating over the instances

dogs_list = [dog1, dog2]

for dog in dogs_list:
	print(f"name: {dog.name} - age: {dog.age} - gender: {dog.gender}")