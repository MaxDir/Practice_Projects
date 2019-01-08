#31.12.2018
i = str(input("Введите текст: "))

file = open("text.txt", "w")
file.write(i)
file.close()

file = open("text.txt", "r")
print(file.read())
file.close()

file = open("text.txt", "w")
file.write("Антон ПИТУХ")
file.close()

file = open("text.txt", "r")
print(file.read())
file.close()