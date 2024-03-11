import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql
import os

# Database connection details
db_host = "localhost"
db_user = "root"
db_password = "61366136"
db_name = "Ftest"
db_table = "regteach"

# Function to handle login button click
def login_button_clicked():
    username = username_var.get()
    password = password_var.get()

    if not username or not password:
        messagebox.showerror("Error", "Please enter username and password")
        return

    try:
        connection = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)
        cursor = connection.cursor()

        sql = f"SELECT * FROM {db_table} WHERE email = '{username}' AND password = '{password}'"
        cursor.execute(sql)

        if cursor.fetchone():
            messagebox.showinfo("Success", "Login Successful!")
            os.system("python AMS_Run.py")
            root.destroy()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    except pymysql.Error as err:
        messagebox.showerror("Error", f"Database connection error: {err}")
    finally:
        if connection:
            connection.close()
            cursor.close()

# Function to handle register button click
def register_button_clicked():

    os.system("python register.py")

# GUI window initialization
root = tk.Tk()
root.title("EZY Attendance")
root.geometry("500x300")

# Background image
bg_image = tk.PhotoImage(file="banner.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Make the window transparent
root.attributes("-alpha", 0.7)
# Login frame
login_frame = ttk.Frame(root, padding=20, style="Login.TFrame")
login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Email label and entry
username_label = ttk.Label(login_frame, text="Email:")
username_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

username_var = tk.StringVar()
username_entry = ttk.Entry(login_frame, textvariable=username_var)
username_entry.grid(row=0, column=1, padx=5, pady=5)

# Password label and entry
password_label = ttk.Label(login_frame, text="Password:")
password_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

password_var = tk.StringVar()
password_entry = ttk.Entry(login_frame, textvariable=password_var, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

# Login button
login_button = ttk.Button(login_frame, text="Login", command=login_button_clicked, style="Green.TButton")
login_button.grid(row=2, columnspan=2, pady=10)

# Register button
register_button = ttk.Button(login_frame, text="Register", command=register_button_clicked, style="Green.TButton")
register_button.grid(row=3, columnspan=2, pady=5)

# Styling
style = ttk.Style()

# Styling for login frame
style.configure("Login.TFrame", background="#f0f0f0")

# Styling for green buttons
style.configure("Green.TButton", foreground="white", background="#4CAF50", font=("Helvetica", 12))

root.mainloop()
