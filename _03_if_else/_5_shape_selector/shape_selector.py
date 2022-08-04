import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    Josh=turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    shape=simpledialog.askstring('title','Give me a shape that is listed. Square,triangle or pentagon. ')
    # Draw the shape requested by the user using if-elif-else statements
    if shape=='square':
        for i in range(4):
            Josh.forward(150)
            Josh.left(90)
    elif shape=='pentagon':
        for i in range(5):
            Josh.forward(150)
            Josh.left(360/5)
    else:
        for i in range(3):
            Josh.forward(150)
            Josh.left(360/3)
    # Call the turtle .done() method
    turtle.done()