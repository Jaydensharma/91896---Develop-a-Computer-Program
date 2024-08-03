#Date: 09/05/2024 
#Author: Jayden Sharma
#Purpose: Demonstrate Github and use it correctly

from tkinter import *
from tkinter import ttk

# Quit subroutine
def quit():
    main_window.destroy()

# Print details of all the camps
def print_camp_details():
    name_count = 0
    # Create the column headings
    Label(main_window, font=("Helvetica 10 bold"), text="Row").grid(column=0, row=7)
    Label(main_window, font=("Helvetica 10 bold"), text="First Name").grid(column=1, row=7)
    Label(main_window, font=("Helvetica 10 bold"), text="Last Name").grid(column=2, row=7)
    Label(main_window, font=("Helvetica 10 bold"), text="Item Name").grid(column=3, row=7)
    Label(main_window, font=("Helvetica 10 bold"), text="Number of Items").grid(column=4, row=7)
    # Add each item in the list into its own row
    while name_count < counters['total_entries']:
        Label(main_window, text=name_count).grid(column=0, row=name_count+8)
        Label(main_window, text=(camp_details[name_count][0])).grid(column=1, row=name_count+8)
        Label(main_window, text=(camp_details[name_count][1])).grid(column=2, row=name_count+8)
        Label(main_window, text=(camp_details[name_count][2])).grid(column=3, row=name_count+8)
        Label(main_window, text=(camp_details[name_count][3])).grid(column=4, row=name_count+8)
        name_count += 1
        counters['name_count'] = name_count

# Check the inputs are all valid
def check_inputs():
    input_check = 0
    # Clear previous error messages
    Label(main_window, text="               ").grid(column=2, row=0)
    Label(main_window, text="               ").grid(column=2, row=1)
    Label(main_window, text="               ").grid(column=2, row=2)
    Label(main_window, text="               ").grid(column=2, row=3)
    # Check that First Name is not blank, set error text if blank
    if len(entry_fname.get().strip()) == 0:
        Label(main_window, fg="red", text="Required").grid(column=2, row=0)
        input_check = 1
    # Check that Last Name is not blank, set error text if blank
    if len(entry_lname.get().strip()) == 0:
        Label(main_window, fg="red", text="Required").grid(column=2, row=1)
        input_check = 1
    # Check that Item Name is not blank, set error text if blank
    if len(entry_item_hired.get().strip()) == 0:
        Label(main_window, fg="red", text="Required").grid(column=2, row=2)
        input_check = 1
    # Check that number of items is selected
    if number_of_items.get() == '':
        Label(main_window, fg="red", text="Required").grid(column=2, row=3)
        input_check = 1
    if input_check == 0:
        append_name()

# Add the next camper to the list
def append_name():
    # Append each item to its own area of the list
    camp_details.append([entry_fname.get(), entry_lname.get(), entry_item_hired.get(), number_of_items.get()])
    # Clear the boxes
    entry_fname.delete(0, 'end')
    entry_lname.delete(0, 'end')
    entry_item_hired.delete(0, 'end')
    number_of_items.set('')
    counters['total_entries'] += 1

# Delete a row from the list
def delete_row():
    # Find which row is to be deleted and delete it
    del camp_details[int(delete_item.get())]
    counters['total_entries'] -= 1
    name_count = counters['name_count']
    delete_item.delete(0, 'end')
    # Clear the last item displayed on the GUI
    Label(main_window, text="       ").grid(column=0, row=name_count+7)
    Label(main_window, text="       ").grid(column=1, row=name_count+7)
    Label(main_window, text="       ").grid(column=2, row=name_count+7)
    Label(main_window, text="       ").grid(column=3, row=name_count+7)
    Label(main_window, text="       ").grid(column=4, row=name_count+7)
    # Print all the items in the list
    print_camp_details()

# Create the buttons and labels
def setup_buttons():
    # Create all the empty and default labels, buttons and entry boxes. Put them in the correct grid location
    Label(main_window, text="First Name").grid(column=0, row=0, sticky=E)
    Label(main_window, text="Last Name").grid(column=0, row=1, sticky=E)
    Label(main_window, text="Item Name").grid(column=0, row=2, sticky=E)
    Label(main_window, text="Number Of Items").grid(column=0, row=3, sticky=E)
    Button(main_window, text="Append Details", command=check_inputs).grid(column=3, row=1)
    Button(main_window, text="Print Details", command=print_camp_details, width=10).grid(column=4, row=1, sticky=E)
    Button(main_window, text="Delete Receipt", command=delete_row, width=10).grid(column=4, row=3, sticky=E)
    Label(main_window, text="               ").grid(column=2, row=0)
    
    # Load the image for the Quit button
    sunset_image = PhotoImage(file="sunset.png")
    Button(main_window, text="Quit", command=quit, image=sunset_image, width=50, height=50, compound=LEFT).grid(column=4, row=0, sticky=E)
    # Keep a reference to the image to prevent it from being garbage collected
    main_window.image = sunset_image

# Start the program running
def main():
    # Start the GUI
    setup_buttons()
    main_window.mainloop()

# Create empty list for camp details and empty variable for entries in the list
counters = {'total_entries': 0, 'name_count': 0}
camp_details = []
main_window = Tk()
main_window.title("Julie's Party Hire")

entry_fname = Entry(main_window)
entry_fname.grid(column=1, row=0)

entry_lname = Entry(main_window)
entry_lname.grid(column=1, row=1)

entry_item_hired = Entry(main_window)
entry_item_hired.grid(column=1, row=2)

values = list(range(1, 100))
number_of_items = ttk.Combobox(main_window, values=values)
number_of_items.grid(column=1, row=3)

delete_item = Entry(main_window)
delete_item.grid(column=3, row=3)

main()
