class Rectangle:
	def __init__(self, length, width):
		self.length = int(input("Please input length "))
		self.width = int(input("Please input width "))

	def compute_area(self):
		return self.length * self.width

my_obj = Rectangle(4,5)
print(my_obj.compute_area())