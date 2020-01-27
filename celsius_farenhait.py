temp_numb = int(input("Please input temperature: "))
temp_type = input("Please input C or F :")
if temp_type == "C":
	temp_fahren = (temp_numb*9/5)+32
	print(temp_fahren,"F")
elif temp_type == "F":
	temp_cels = (temp_numb-32)*5/9
	print(temp_cels,"C")
else:
	print("You have inputed wrong type of temperature.Try again :-)")

