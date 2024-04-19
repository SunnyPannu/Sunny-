import turtle

# Create a turtle object
star = turtle.Turtle()

# Function to draw a star
def draw_star(size):
    for i in range(5):
        star.forward(size)
        star.right(144)

# Set the speed of the turtle
star.speed(5)

# Move the turtle to starting position
star.penup()
star.goto(-50, 0)
star.pendown()

# Call the draw_star function
draw_star(100)

# Hide the turtle
star.hideturtle()

# Keep the window open
turtle.done()
