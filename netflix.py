import turtle

def draw_netflix_logo():
    # Set up the turtle
    screen = turtle.Screen()
    screen.bgcolor("black")
    
    netflix_turtle = turtle.Turtle()
    netflix_turtle.speed(1)
    netflix_turtle.color("red")
    
    # Draw the letter "N"
    netflix_turtle.penup()
    netflix_turtle.goto(-30, 0)
    netflix_turtle.pendown()
    netflix_turtle.left(90)
    netflix_turtle.forward(100)
    netflix_turtle.right(150)
    netflix_turtle.forward(110)
    netflix_turtle.left(150)
    netflix_turtle.forward(100)
    
    # Hide the turtle
    netflix_turtle.hideturtle()

    # Display the window
    screen.mainloop()

# Call the function to draw the Netflix logo
draw_netflix_logo()
