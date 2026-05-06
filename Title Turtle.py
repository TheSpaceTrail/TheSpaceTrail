import turtle, random

# black bgcolor 
screen = turtle.Screen()
screen.bgcolor("black")

# makes turtle with silver colours & size 6
t = turtle.Turtle()
t.ht()
t.color("grey", "darkgrey")
t.speed(0)
t.pensize(6)

# makes turtle for stars
star = turtle.Turtle()
star.color("white")
star.ht()
star.speed(0)

# Makes background stars
def stars(star_num):
    for x in range(star_num):
        star.penup()
        star.setx(random.randint(-400,400))
        star.sety(random.randint(-400,400))
        star.pendown()
        for i in range(5):
            star.forward(2)
            star.right(144)

# Makes simple oval based on radius and distance before circling
def make_oval(radius, distance):
    t.begin_fill()
    for i in range(2):
        t.circle(radius, 180)
        t.forward(distance)
    t.end_fill()

# Makes stars and general base of ship
stars(10)
make_oval(15, 100)

# Re-adjusts position to make thruster shape
t.color("grey", "darkgrey")
t.goto(0,5)

# Fills in circle to make thruster
t.pendown()
t.begin_fill()
t.color("lightblue", "blue")
t.circle(10)
t.end_fill()

# Makes back compartment
t.penup()
t.color("grey", "darkgrey")
t.goto(-100, 50)
t.pendown()
make_oval(10, 60)

# Makes bridge
t.goto(-100, 50)
t.right(45)
t.forward(22)
t.left(45)

# Makes other back compartment
t.penup()
t.color("grey", "darkgrey")
t.goto(0, 50)
t.pendown()
make_oval(10, 60)

# Makes other bridge
t.goto(0, 50)
t.right(135)
t.forward(28)
t.left(135)

# Makes base connecting ship to main command centre & command centre itself
t.penup()
t.color("grey", "darkgrey")
t.goto(150, 70)
t.pendown()
make_oval(27, 120)

# Makes bridge
t.goto(50, 70)
t.right(135)
t.forward(55)
t.left(135)
t.penup()

# Makes orange thruster
t.goto(77, 66)
t.color("orange")
t.pendown()
t.forward(20)
t.penup()

# Writes THE SPACE TRAIL at top
t.goto(0, 195)
t.color("white")
t.write("THE SPACE TRAIL", font=("Fantasy", 33, "bold italic underline"), align="center")

# Writes Click to start! at bottom
t.goto(0, -130)
t.write("Click to start!", font=("Vardana", 25, "bold italic"), align="center")

# Closes turtle screen if screen is clicked
while True: 
    turtle.exitonclick()

# Keeps screen on until screen is clicked
turtle.done()