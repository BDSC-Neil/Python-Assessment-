import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def enter_data():
    accepted = accept_var.get()

    if accepted == "Accepted":
        # User info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if firstname and lastname:
            title = title_combobox.get()
            age = int(age_spinbox.get())  # Convert to integer
            year = int(year_combobox.get())  # Convert to integer

            # Check if age is outside the valid range (18 to 30)
            if age < 18 or age > 30:
                message = f"Sorry {firstname} {lastname}, but your age is invalid for this application."
                tkinter.messagebox.showwarning(title="Invalid Details", message=message)
                window.destroy()  # Close the tkinter window and terminate the program
                return

            # Course info
            registration_status = reg_status_var.get()
            numexperience = numexperience_spinbox.get()
            numhours = numhours_spinbox.get()

            # Check if experience or hours is below 3
            if int(numexperience) < 3 or int(numhours) < 3:
                message = f"Sorry {firstname} {lastname}, but some of your details are invalid for this application."
                tkinter.messagebox.showwarning(title="Invalid Details", message=message)
                window.destroy()  # Close the tkinter window and terminate the program
                return

            # Printing the collected data (for testing purposes)
            print("First name:", firstname, "Last name:", lastname)
            print("Title:", title, "Age:", age, "Year Level:", year)
            print("# Experience:", numexperience, "# Hours:", numhours)
            print("Registration status:", registration_status)
            print("------------------------------------------")

            # Creating or connecting to the SQLite database
            conn = sqlite3.connect('data.db')

            # Creating a table for Student Data if it doesn't exist already
            table_create_query = '''CREATE TABLE IF NOT EXISTS Student_Data 
                    (firstname TEXT, lastname TEXT, title TEXT, age INT, year INT, 
                    registration_status TEXT, num_courses INT, num_semesters INT)
            '''
            conn.execute(table_create_query)

            # Inserting the collected data into the table
            data_insert_query = '''INSERT INTO Student_Data (firstname, lastname, title, 
            age, year, registration_status, num_courses, num_semesters) VALUES 
            (?, ?, ?, ?, ?, ?, ?, ?)'''
            data_insert_tuple = (firstname, lastname, title,
                                 age, year, registration_status, numexperience, numhours)
            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)

            # Committing the changes to the database
            conn.commit()

            # Closing the database connection
            conn.close()

        else:
            tkinter.messagebox.showwarning(title="Error", message="First name and last name are required.")
    else:
        tkinter.messagebox.showwarning(title="Error", message="You have not accepted the terms")

# Creating the main tkinter window
window = tkinter.Tk()
window.title("Data Entry Form")

# Creating a frame to hold all the widgets
frame = tkinter.Frame(window)
frame.pack()

# --- User Information Section ---

user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

# Widgets to collect user's first name, last name, title, age, and year level
first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=0, to=100)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Year Level")
year_combobox = ttk.Combobox(user_info_frame, values=[9, 10, 11, 12, 13])
nationality_label.grid(row=2, column=1)
year_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# --- Courses Section ---

courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

# Widgets to collect registration status, programming experience (number of courses), and working hours
registered_label = tkinter.Label(courses_frame, text="Registration Status")
reg_status_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered",
                                       variable=reg_status_var, onvalue="Registered", offvalue="Not registered")
registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(courses_frame, text="# Programming Experience")
numexperience_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
numcourses_label.grid(row=0, column=1)
numexperience_spinbox.grid(row=1, column=1)

numsemesters_label = tkinter.Label(courses_frame, text="# Working Hours")
numhours_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
numsemesters_label.grid(row=0, column=2)
numhours_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# --- Terms & Conditions Section ---

terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

# Widget to accept terms and conditions
accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

# --- Enter Data Button ---

# Button to enter data
button = tkinter.Button(frame, text="Enter data", command=enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

# Run the tkinter main event loop
window.mainloop()
