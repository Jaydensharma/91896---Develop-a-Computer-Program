#09/08/2024
#Author: Jayden Sharma
#Purpose: The purpose of my prototype number 7 is to start adding my validation and allowing my code
#to start functioning correctly.

import tkinter as tk
from tkinter import ttk
from tkinter import *
import random
import os

#creates the main menu as its own class / application so all the code is seperate
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        #names and sizes the application
        self.title("Julie's Party Hire")
        self.geometry("600x400")

        #makes the buttons on the main menu for the user to select you from
        Button(self, text="Hire", command=self.open_hire_window).pack(pady=10)
        Button(self, text="Return", command=self.open_return_window).pack(pady=10)
        Button(self, text="Quit", command=self.quit_application).pack(pady=10)

    #sends the user to the hire window
    def open_hire_window(self):
        HireWindow(self)

    #sends the user to the returns window
    def open_return_window(self):
        ReturnWindow(self)

    #quits the program
    def quit_application(self):
        self.destroy()

#this is the hire window under its own class / application
class HireWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        #names and sizes the window
        self.title("Hire Window")
        self.geometry("400x300")

        #lable which displays First Name which is positioned next to the entry box
        Label(self, text="First Name").grid(row=0, column=0, padx=10, pady=5)
        self.entry_fname = Entry(self)
        # positions the entry box
        self.entry_fname.grid(row=0, column=1, padx=10, pady=5)

        #lable which displays Last Name which is positioned next to the entry box
        Label(self, text="Last Name").grid(row=1, column=0, padx=10, pady=5)
        self.entry_lname = Entry(self)
        # positions the entry box
        self.entry_lname.grid(row=1, column=1, padx=10, pady=5)

        #label which displays Item Name which is positioned next to the entry box
        Label(self, text="Item Name").grid(row=2, column=0, padx=10, pady=5)
        self.combo_item_hired = ttk.Combobox(self, values=["Balloons", "Streamers", "Party Hats"])
        # positions the combo box
        self.combo_item_hired.grid(row=2, column=1, padx=10, pady=5)

        #label which displays Number Of Items which is positioned next to the entry box
        Label(self, text="Number Of Items").grid(row=3, column=0, padx=10, pady=5)
        self.spinbox_number_of_items = Spinbox(self, from_=1, to=100)
        #positions the spin box next to the label
        self.spinbox_number_of_items.grid(row=3, column=1, padx=10, pady=5)

        #submit button below all the labels
        Button(self, text="Submit", command=self.check_inputs).grid(row=4, column=0, columnspan=2, pady=10)

    #own def which checks the inputs and 
    def check_inputs(self):
        # Check that no inputs are empty and if theyre all correct it creates a success message box
        if len(self.entry_fname.get().strip()) == 0 or len(self.entry_lname.get().strip()) == 0 or len(self.combo_item_hired.get().strip()) == 0:
            tk.messagebox.showwarning("Input Error", "Please fill in all fields.")
        else:
            tk.messagebox.showinfo("Success", "Hire details recorded!")

#return window application / own class
class ReturnWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        #names and sizes the window
        self.title("Return Window")
        self.geometry("400x300")

#loops the window and specific application untill the user chooses what to do.
if __name__ == "__main__":
    app = Application()
    app.mainloop()
