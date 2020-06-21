import turtle
wn=turtle.Screen()
wn.bgcolor("lightgreen")
t1=turtle.Turtle()
distance=50
for i in range(50):
    t1.forward(distance)
    t1.right(90)
    distance=distance + 10
