my_year = input("Please enter the year: ")
my_year = int(my_year)
print(my_year)
x = 4
y = my_year%4
y = bool( not y)
print("That fact than your inputted year leap is",y)