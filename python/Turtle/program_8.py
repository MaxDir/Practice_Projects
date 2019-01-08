import turtle

turtle.shape('turtle')

length = 10
count = 0

while count < 20:
	turtle.forward(length)
	turtle.left(90)
	length += 10
	count += 1

q = input()