"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""
from tkinter import messagebox, simpledialog, Tk
import math
if __name__ == '__main__':
    window=Tk()
    window.withdraw
    Number1=simpledialog.askinteger('title','Can you please give me a number?')
    Number2=simpledialog.askinteger('title','Can you please give me another number higher than your 1st number ?')
    Sum=Number2+Number1
    messagebox.showinfo('title','The sum of your 2 numbers is '+str(Sum))
    window.mainloop()