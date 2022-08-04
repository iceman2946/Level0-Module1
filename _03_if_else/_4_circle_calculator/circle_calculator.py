import turtle
from tkinter import messagebox, simpledialog, Tk
import math
if __name__ == '__main__':
    window=Tk()
    window.withdraw()
# Write a Python program that asks the user for the radius of a circle.
    Radius=simpledialog.askinteger('title', 'What is the radius of a circle?')
# Next, ask the user if they would like to calculate the area or circumference of a circle.
    answer=simpledialog.askstring('title','Do you want to calculate the area or circumference of the circle.')
# If they choose area, display the area of the circle using the radius.
    if answer=='area':
       area=math.pi*Radius*Radius
       print(area)
       messagebox.showinfo('title','The area of your circle is'+str(area))
# Otherwise, display the circumference of the circle using the radius.
    else:
        circumference=math.pi*2*Radius
        print(circumference)
        messagebox.showinfo('title','The circumference of your circle'+str(circumference))
#Area = πr^2
#Circumference = 2πr 