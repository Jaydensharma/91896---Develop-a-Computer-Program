#06/08/2024
#Author: Jayden Sharma
#Purpose: The purpose of this stage is to start polishing and adding all the 
# neccessary lables and boxes into the hire window to allow everything to work

import tkinter as tk
from tkinter import *

#creates the main menu as its own application / class
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        #sizes the main menu and names the main menu
        self.title("Julie's Party Hire")
        self.geometry("400x300")

        #creates buttons that corrospond to what the user wants to do
        Button(self, text="Hire", command=self.open_hire_window).pack(pady=10)
        Button(self, text="Return", command=self.open_return_window).pack(pady=10)
        Button(self, text="Quit", command=self.quit_application).pack(pady=10)

    def open_hire_window(self):
        HireWindow(self) #when user presses hire it sends the user to this directory

    def open_return_window(self):
        pass # doesnt do anything at this stage
    
    #quits the program / ends the program
    def quit_application(self):
        self.destroy()

#creates it own hire window class / application
class HireWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        #names the window and sizes the winow
        self.title("Hire Window")
        self.geometry("400x300")
        
        #Creates the first Label/ text box which is the fist name box which allows the user to input there first name
        Label(self, text="First Name").grid(column=0, row=0, padx=10, pady=5)
        self.entry_fname = Entry(self)
        # positions the first name text box
        self.entry_fname.grid(column=1, row=0, padx=10, pady=5)

        #Creates a Lable / text box to let the user be able to input there last name
        Label(self, text="Last Name").grid(column=0, row=1, padx=10, pady=5)
        self.entry_lname = Entry(self)
        #Poistions the text box
        self.entry_lname.grid(column=1, row=1, padx=10, pady=5)

        # Creates a label / text box to let the user be able to input the item they would like to hire
        Label(self, text="Item Name").grid(column=0, row=2, padx=10, pady=5)
        self.entry_item = Entry(self)
        #Postions the item hired box
        self.entry_item.grid(column=1, row=2, padx=10, pady=5)

#allows the window to keep on looping back until the user decides what they would like to do.
if __name__ == "__main__":
    app = Application()
    app.mainloop()
