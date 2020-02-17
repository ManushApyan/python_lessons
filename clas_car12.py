class Vehicle:
	def __init__(self, name, color, cost):
		self.name = name
		self.color = color
		self.cost = cost

car1 = Vehicle("Fer", "Red", "60000$")
car2 = Vehicle("Jump", "Blue", "10000$")
print(car1.name, car1.color, car1.cost)
print(car2.name, car2.color, car2.cost)