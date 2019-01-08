#Игра камень ножници бумага v0.3         31.12.2018
import random

print("-----------ИГРА-----------")
print("1)Камень\n2)Ножницы\n3)Бумага")
print("--------------------------")

#Компютер загадыват рандомное число, которое соответствет придмету
number = int(random.randint(1, 3))

if number == 1:
	gg = "Камень"
elif number == 2:
	gg = "Ножницы"
else:
	gg = "Бумага"

def line():
	print("--------------------------")

try:
	#Игрок выбирает предмет
	player = int(input("Выберите число: \n"))
	line()

	if player == 1:
		print("Вы выбрали 'Камень'")
		print("Оппонент выбрал", "'" + str(gg) +"'")
		line()
		if number == 1:
			print("Ничья")
		elif number == 2:
			print("Вы победили")
		else:
			print("Вы проиграли")
		line()
		print("")
	elif player == 2:
		print("Вы выбрали 'Ножницы'")
		print("Оппонент выбрал", "'" + str(gg) + "'")
		line()
		if number == 1:
			print("Вы проиграли")
		elif number == 2:
			print("Ничья")
		else:
			print("Вы победили")
		line()
		print("")
	elif player == 3:
		print("Вы выбрали 'Бумагу'")
		print("Оппонент выбрал", "'" +str(gg) + "'")
		line()
		if number == 1:
			print("Вы победили")
		elif number == 2:
			print("Вы проиграли")
		else:
			print("Ничья")
		line()
		print("")
	else:
		print("Введите число от 1 до 3")
except:
	print("Введите ЦЕЛОЕ число")
