# import everything from tkinter module
from tkinter import *   
 
# create a tkinter window
root = Tk()             
 
# Open window having dimension 100x100
root.geometry('200x200')
 
# Create a Button
btn = Button(root, text = 'Click me !', bd = '5',command = root.destroy)


# Dropdown menu options
options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

clicked = StringVar()

clicked.set( "Monday")

# Create Dropdown menu
drop = OptionMenu( root , clicked , *options )
drop.pack()

print(clicked.get)
 
# Set the position of button on the top of window.  
btn.pack(side = 'top')   
 
root.mainloop()