#import tkinter library
import tkinter as tk


#creates the tkinter object
root = tk.Tk()

#sets a title for my window
root.title("fortnite")

#sets the default size for my window
root.geometry('400x400')

#limits or enables the ability to resize the window (by default 1)
#0 disables resizing, 1 enables resizing
#first is the x direction second is the y direction
root.resizable(0,0)

#Define a string variable
myNewLabel = tk.StringVar()

#set a default value for my string label
myNewLabel.set('Fortnite')

#define a function to change the label
def changeLabel():
    myNewLabel.set('Battle Royal')

#Creating a label for my user interface
#the order of therse variable names doesnt matter
myLabel = tk.Label(master=root,textvariable= myNewLabel,fg = 'blue', bg = 'pink', width =40).pack()

#Creating a button
myButton = tk.Button (master=root, width = 20,command=changeLabel, text='Enter Game').pack()
#runs mainloop to start listening to user events
#recursive function call
root.mainloop()

#ends the event listener from looping
#root.quit

#closes the GUI
#root.destroy()
