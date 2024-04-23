class Movie:
	
	pk_counter = 1

	def __init__(self, title, rating):
		self.id = Movie.pk_counter
		self.title = title
		self.rating = rating
		Movie.pk_counter += 1
		


movie1 = Movie('movie 1', 4.5)
movie2 = Movie("Die hard", 4)

print(f"movie name: {movie1.title}, rating: {movie1.rating}, id: {movie1.id}")
print(f"movie name: {movie2.title}, rating: {movie2.rating}, id: {movie2.id}")