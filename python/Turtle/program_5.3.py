import turtle

turtle.shape('turtle')

a = 10
for i in range(10):
	for i in range(4):
		turtle.forward(a)
		turtle.left(90)

	turtle.penup() #Не оставлять след при движении
	turtle.forward(-10)
	turtle.left(-90)
	turtle.forward(10)
	turtle.left(90)
	turtle.pendown() #Оставлять след при движении

	a +=20

q = input()	