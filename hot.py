import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
pen = turtle.Turtle()
pen.speed(0)  # Set the drawing speed to the fastest

# Function to draw a petal
def draw_petal():
    pen.circle(50, 60)
    pen.left(120)
    pen.circle(50, 60)
    pen.left(120)

# Main drawing logic
pen.color("red")  # Set the pen color to red
pen.begin_fill()  # Begin filling the shape
for _ in range(6):
    draw_petal()
    pen.left(60)
pen.end_fill()    # End filling the shape

# Hide the turtle and display the result
pen.hideturtle()
screen.mainloop()
