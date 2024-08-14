#07/08/2024
#Author: Jayden Sharma
#Purpose: The purpose of this prototype is to start finalising the hire window by adding all the options 
# and fancy buttons to make the GUI interface look professional

import tkinter as tk
from tkinter import ttk
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
        HireWindow(self) #when user presses hire it sends the user to this directory / application / class

    def open_return_window(self):
        pass # doesnt work at this stage.

    def quit_application(self):
        self.destroy() # ends the program / quits the program

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

        # creates the text next to the combobox which displayes hire name and positions the lable on the far left side.
        Label(self, text="Item Name").grid(column=0, row=2, padx=10, pady=5)
        # creates a list of party items that the user can choose to hire from
        party_items = ["Balloons", "Streamers", "Party Hats", "Cake", "Cupcakes"]
        # loads the party_items directory into the combo box to allow it to be displayed as options
        self.combo_item = ttk.Combobox(self, values=party_items)
        #positions the combo box
        self.combo_item.grid(column=1, row=2, padx=10, pady=5)

        #adding the number of items option in the code and positions it below all the other labels
        Label(self, text="Number Of Items").grid(column=0, row=3, padx=10, pady=5)
        #creates a spin box which ranges from 1- 100
        self.spinbox_items = Spinbox(self, from_=1, to=100)
        # positions the spin box
        self.spinbox_items.grid(column=1, row=3, padx=10, pady=5)

#allows the window to keep on looping back until the user decides what they would like to do.
if __name__ == "__main__":
    app = Application()
    app.mainloop()
