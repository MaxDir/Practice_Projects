print("---------Калькулятор---------")
print("1) +\n2) -\n3) *\n4) /")

i = int(input("-------Введите действия-------\n"))

if i == 1:

	a = float(input("Введите 1-е числол: "))
	y = float(input("Введите 2-е числол: "))

	z = a + y

	print("------------------------------")
	print("Ответ: ", a, "+", y, "=", z)
	print("------------------------------")

elif i == 2:

	a = float(input("Введите 1-е числол: "))
	y = float(input("Введите 2-е числол: "))

	z = a - y

	print("------------------------------")
	print("Ответ: ", a, "-", y, "=", z)
	print("------------------------------")

elif i == 3:

	a = float(input("Введите 1-е числол: "))
	y = float(input("Введите 2-е числол: "))

	z = a * y

	print("------------------------------")
	print("Ответ: ", a, "*", y, "=", z)
	print("------------------------------")

elif i == 4:

	a = float(input("Введите 1-е числол: "))
	y = float(input("Введите 2-е числол: "))

	z = a / y

	print("------------------------------")
	print("Ответ: ", a, "/", y, "=", z)
	print("------------------------------")

else:
	print("Введите число от 1 доа 4")
