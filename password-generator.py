import random # Importing libraries

chars = "qwertyuiop[]asdfghjkl;'zxcvbnm,./1234567890QWERTYUIOPASDFGHJKLZXCVBNM',!#$%~&?"

num = int(input("How many passwords to generate? "))
lenght = int(input("Password lenght: "))

for x in range(num):
	password = ""

	for i in range(lenght):
		password += random.choice(chars)

	print(password)