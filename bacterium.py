class Bacterium(object):
	"""docstring for Bacterium"""
	def __init__(self, x, y, size, shape, multi_cellular):
		self.size = size
		self.shape = shape
		self.multi_cellular = multi_cellular
		self.x = x
		self.y = y


bacteria1 = Bacterium(1, 2, 0.5, 'spherical', 'single')
bacteria2 = Bacterium(2, 2, 1.5, 'rod', 'single')
bacteria3 = Bacterium(2, 1, 1.0, 'comma', 'single')
		