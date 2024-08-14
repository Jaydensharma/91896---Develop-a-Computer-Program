#03/08/2024
#Author: Jayden Sharma
#Purpose: The purpose of this stage is to figure out how to make the main menu

#Imports tkinter
import tkinter as tk

#Creates the application and names it
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        #names the window Julie's Party Hire
        self.title("Julie's Party Hire")
        #creates the size of the window
        self.geometry("400x300")

        # Create buttons of the main menu
        tk.Button(self, text="Hire", command=self.open_hire_window).pack(pady=10)
        tk.Button(self, text="Return", command=self.open_return_window).pack(pady=10)
        tk.Button(self, text="Quit", command=self.quit_application).pack(pady=10)

    def open_hire_window(self):
        pass  # To be implemented

    def open_return_window(self):
        pass  # To be implemented

    def quit_application(self):
        self.destroy()

#loops the main menu so it doesnt just close and keeps on refreashing until the user inputs something
if __name__ == "__main__":
    app = Application()
    app.mainloop()
