# using del to delete the attribute from the class
class Dog(object):
	"""docstring for Dog"""
	def __init__(self, name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender



dog = Dog("fido", 5, 'male')
print(f"name: {dog.name}, age: {dog.age}, gender: {dog.gender}")
print("deleting the gender attribute")
del dog.gender
print(dog.gender)



# name: fido, age: 5, gender: male
# deleting the gender attribute
# Traceback (most recent call last):
#   File "/py-oops/del_ex.py", line 15, in <module>
#     print(dog.gender)
#           ^^^^^^^^^^
# AttributeError: 'Dog' object has no attribute 'gender'

