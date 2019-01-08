import random

print("-----------------------------")
print("Игра угадай число")
print("-----------------------------")

ran = random.randint(1,100)

player = 0

while player != ran:
	
	player = int(input("Введите число от 1 до 100: "))
	print("-----------------------------")

	if player > 100:
		print ("Максимальное число 100:")
	elif player < 1:
		print ("Минимальное число 1:")
	elif player > ran:
		print ("Загаданное число меньше")
	elif player < ran:
		print("Загаданное число больше")
	elif player == ran:
		print("Ты выиграл!!!\nЗагаданное число", player)
		print("-----------------------------")
		break
	else:
		pass
