#03/08/2024
#Author: Jayden Sharma
#Purpose: The purpose of this stage is to figure out how to make the main menu


import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Julie's Party Hire")
        self.geometry("400x300")

        # Create buttons
        tk.Button(self, text="Hire", command=self.open_hire_window).pack(pady=10)
        tk.Button(self, text="Return", command=self.open_return_window).pack(pady=10)
        tk.Button(self, text="Quit", command=self.quit_application).pack(pady=10)

    def open_hire_window(self):
        pass  # To be implemented

    def open_return_window(self):
        pass  # To be implemented

    def quit_application(self):
        self.destroy()

if __name__ == "__main__":
    app = Application()
    app.mainloop()
