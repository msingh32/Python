import turtle

def draw_square(brad):
    for i in range(0,4,1):
        brad.forward(100)
        brad.right(90)

def draw_circle():
    window = turtle.Screen()
    window.bgcolor("red")
    angie = turtle.Turtle()
    for i in range(1,38):
        draw_square(angie)
        angie.right(10)
    #angie.shape("arrow")
    #angie.color("blue")
   # angie.circle(100)
    window.exitonclick()
draw_circle()

