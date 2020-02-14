my_dict = {"first":"10", "second":"20", "third":"30", "fourth":"40"}
my_word = input("Input your key: ")
if my_word in  my_dict:
	print( my_word, "is exist in our dictionary!")
else:
	print("is not exist in dictionary as a key!")
