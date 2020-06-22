import turtle
wn=turtle.Screen()
wn.bgcolor("lightblue")

t1=turtle.Turtle()
t1.color("blue")
t1.shape("turtle")

dist=5
t1.up()
for i in range(60):
    t1.stamp()
    t1.forward(dist)
    t1.right(24)
    dist=dist+2
wn.exitonclick()
