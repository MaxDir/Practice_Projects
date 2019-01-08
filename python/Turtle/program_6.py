import turtle

turtle.shape('turtle')

for i in range(12):
	turtle.right(30)
	turtle.forward(70)
	turtle.stamp()
	turtle.goto(0, 0)

q = input()	