file = open("2.txt", "w")
file.write("      " * 8000000)
file.close()

file = open("2.txt", "r")
print(file.read())
file.close()
