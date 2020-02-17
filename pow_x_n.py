class Pow:
	def __init__(self, x, n):
		self.x = x
		self.n = n

	def my_func(self):
		self.x = int(input("Enter x "))
		self.n = int(input("Enter n "))
		return pow(self.x, self.n)

my_number = Pow("x","n")
print(my_number.my_func())