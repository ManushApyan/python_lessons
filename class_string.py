class MyStrings:
	def __init__(self,your_string):
		self.string = your_string

	def get_string(self):
		self.your_string = input("Please input your string ")
		print(self.your_string)


	def print_string(self):
		print(self.your_string.upper())


my_object = MyStrings("as as f sdf ")
my_object.get_string()
my_object.print_string()