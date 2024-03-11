from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import os

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("600x400")

        # Background color
        self.root.configure(bg="#f0f0f0")

        # variables
        self.var_email = StringVar()
        self.var_password = StringVar()
        self.var_security_question = StringVar()
        self.var_security_answer = StringVar()

        # Title
        title = Label(self.root, text="EZY Attendance Registration", font=("Arial", 25, "bold"), bg="#f0f0f0")
        title.place(relx=0.5, y=20, anchor=CENTER)

        # Email
        lbl_email = Label(self.root, text="Email:", font=("Arial", 12), bg="#f0f0f0")
        lbl_email.place(x=60, y=80)
        self.txt_email = Entry(self.root, textvariable=self.var_email, font=("Arial", 12))
        self.txt_email.place(x=200, y=80, width=180)

        # Password
        lbl_password = Label(self.root, text="Password:", font=("Arial", 12), bg="#f0f0f0")
        lbl_password.place(x=60, y=120)
        self.txt_password = Entry(self.root, textvariable=self.var_password, font=("Arial", 12), show="*")
        self.txt_password.place(x=200, y=120, width=180)

        # Security Question
        lbl_security_question = Label(self.root, text="Security Question:", font=("Arial", 12), bg="#f0f0f0")
        lbl_security_question.place(x=60, y=160)
        self.combo_security = ttk.Combobox(self.root, textvariable=self.var_security_question,
                                           font=("Arial", 12), state="readonly")
        self.combo_security["values"] = ("Your Date of Birth", "Your Nick Name", "Your Favorite Book")
        self.combo_security.place(x=200, y=160, width=180)

        # Security Answer
        lbl_security_answer = Label(self.root, text="Security Answer:", font=("Arial", 12), bg="#f0f0f0")
        lbl_security_answer.place(x=60, y=200)
        self.txt_security_answer = Entry(self.root, textvariable=self.var_security_answer,
                                         font=("Arial", 12))
        self.txt_security_answer.place(x=200, y=200, width=180)

        # Register Button
        btn_register = Button(self.root, text="Register", command=self.register, font=("Arial", 12),
                              bg="#4CAF50", fg="white", activebackground="#45a049", padx=10)
        btn_register.place(relx=0.5, y=250, anchor=CENTER)

    def register(self):
        if self.var_email.get() == "" or self.var_password.get() == "" \
                or self.var_security_question.get() == "" or self.var_security_answer.get() == "":
            messagebox.showerror("Error", "All fields are required!")
        else:
            try:
                conn = mysql.connector.connect(
                    username='root',
                    password='61366136',
                    host='localhost',
                    database='Ftest',
                    port=3306
                )
                cursor = conn.cursor()
                cursor.execute("INSERT INTO regteach (email, password, ss_que, s_ans) VALUES (%s, %s, %s, %s)",
                               (self.var_email.get(), self.var_password.get(), self.var_security_question.get(),
                                self.var_security_answer.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Registration Successful!")
                os.system("python login.py")
                self.root.destroy()  # Close register window
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")

if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
