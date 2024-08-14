#05/08/2024
#Author: Jayden Sharma
#Purpose: The purpose of this stage is to figure start creating the hire window to start setting everything up

#imports tkinter
import tkinter as tk
from tkinter import *

#creates the application as a class
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        #names the window
        self.title("Julie's Party Hire")
        #sizes the window
        self.geometry("400x300")

        #creates the buttons
        Button(self, text="Hire", command=self.open_hire_window).pack(pady=10)
        Button(self, text="Return", command=self.open_return_window).pack(pady=10)
        Button(self, text="Quit", command=self.quit_application).pack(pady=10)

    def open_hire_window(self):
        HireWindow(self) #sends the user to the hire window

    def open_return_window(self):
        pass #doesnt do anything at this stage

    def quit_application(self):
        #ends the program which is also the quit button
        self.destroy()

#puts the hire window in its own class and own application
class HireWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        #names and sizes the hire window
        self.title("Hire Window")
        self.geometry("300x200")

#makes the application and loops it until the user inputs
if __name__ == "__main__":
    app = Application()
    app.mainloop()
