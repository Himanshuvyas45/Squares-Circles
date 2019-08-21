import turtle

wn = turtle.Screen()
wn.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.shape("arrow")
 
for i in range(8):
    for colors in ["red", "green", "yellow", "cyan", "magenta", "blue", "white", "brown"]:
        t.color(colors)
        t.pensize(3)
        t.lt(12)
        t.fd(200)
        t.lt(90)
        t.fd(200)
        t.lt(90)
        t.fd(200)
        t.lt(90)
        t.fd(200)
        t.lt(90)
for i in range(8):
    for colours in ["#0652DD", "#FFC312", "#C4E538", "#ED4C67", "#B53471", "#6F1E51",]:
        t.color(colours)
        t.pensize(3)
        t.circle(100)
        t.lt(10)


wn.mainloop()
