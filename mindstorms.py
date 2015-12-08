import turtle

def draw_square(some_turtle):
    i = 0
    while i < 4:
        some_turtle.forward(100)
        some_turtle.right(90)
        i = i+1
        
def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #Create the turtle Brad - Draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(10)
    i = 0
    while i<5:
        draw_square(brad)
        brad.right(10)
        i = i+1
    brad.right(180)
    j = 0
    while j<5:
        draw_square(brad)
        brad.right(10)
        j = j+1
    #Create the turtle Angie - Draws a circle
##    angie = turtle.Turtle()
##    angie.shape("arrow")
##    angie.color("blue")
##    angie.circle(100)
    
    window.exitonclick()

draw_art()
