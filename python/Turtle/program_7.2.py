import turtle

turtle.shape('turtle')
a = 0.5
z = -10
for x in range(10):
	i = 0
	while i < 105:
		turtle.left(3)
		turtle.forward(a)
		i += 1

	turtle.goto(0, z)
	a += 0.5
	z -= 10

q = input()