"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
from tkinter import messagebox, simpledialog, Tk
import math
if __name__ == '__main__':
    window=Tk()
    window.withdraw

    guess1=simpledialog.askstring('title', 'When can you add two to eleven and get one as the correct answer?')
    answer1='When you add two hours to eleven o clock, you get one o clock.'
    if answer1==guess1:
        messagebox.showinfo('title','You have solved the first riddle!' )
    else:
        messagebox.showinfo('title','Bad luck this time. Better get the next one.')
    guess2=simpledialog.askstring('title','The ages of a father and son add up to 66.\n The fathers age is the sons age reversed.\n How old could they be?\n.')
    answer2a= '51 and 15'
    answer2b= '42 and 24'
    answer2c= '60 and 6'
    if guess2==answer2a or guess2==answer2b or guess2==answer2c:
        messagebox.showinfo('title','Good job! You solved the second riddle!')
    else:
        messagebox.showinfo('title','Bad luck. Try to solve the next riddle with more thinking.')
    guess3=simpledialog.askstring('title','Can you name three consecutive days without using the words Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday')
    answer3='Yesterday,Today or Tomorrow'
    if guess3==answer3:
        messagebox.showinfo('title', 'Amazing job! You solved the last riddle! Try to play this game again to see if you are lucky.')
    else:
        messagebox.showinfo('title','Sorry. Try to play this game again and see if you are lucky.')
