class ReverseWords:
	def __init__(self, my_string):
		self.my_string = my_string

	def my_reverse_func(self):		
		reversed_string = self.my_string.split() 
		reversed_string.reverse()
		reversed_string = " ".join(reversed_string)
		return reversed_string
		

my_obj = ReverseWords("Lala fafa")
print(my_obj.my_reverse_func())
			

