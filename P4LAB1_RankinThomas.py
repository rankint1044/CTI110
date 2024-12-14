# Rankin Thomas
# 12/5/24
# P4LAB1 - Drawing Shapes with Turtle
 
import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.title("Square and Triangle Drawing")
 
# Create the turtle
pen = turtle.Turtle()
pen.speed(3)
 
# Draw the square using a for loop
pen.color("blue")
for _ in range(4):
     pen.forward(100)  # Move forward 100 units
     pen.right(90)     # Turn 90 degrees to the right
 
# Move the turtle to a new position for the triangle
pen.penup()
pen.goto(-150, 0)
pen.pendown()
 
# Draw the triangle using a while loop
pen.color("green")
sides = 0
while sides < 3:
     pen.forward(100)  # Move forward 100 units
     pen.left(120)     # Turn 120 degrees to the left
     sides += 1
 
# Finish the drawing
pen.hideturtle()
 
# Keep the window open until clicked
screen.mainloop()
