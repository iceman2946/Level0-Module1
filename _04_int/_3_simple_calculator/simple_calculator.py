"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""
from tkinter import messagebox, simpledialog, Tk
import math
if __name__ == '__main__':
    window=Tk()
    window.withdraw
    Number1=simpledialog.askinteger('title','Can you please give me a number?')
    Number2=simpledialog.askinteger('title', 'Can you please give me another number higher than your first number?')
    Operation=simpledialog.askstring('title','Do you want to add,subtract,multiply or divide?')
    if Operation=='add':
        Sum=Number1+Number2
        messagebox.showinfo('title','Your sum is' +str(Sum))
    elif Operation=='subtract':
        Difference=Number2-Number1
        messagebox.showinfo('title', 'Your difference is' +str(Difference))
    elif Operation=='multiply':
        Product=Number1*Number2
        messagebox.showinfo('title','Your product is' +str(Product))
    else:
      Quotient=Number2/Number1
      messagebox.showinfo('title','Your quotient is' +str(Quotient))
