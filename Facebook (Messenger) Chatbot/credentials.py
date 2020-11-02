# Creator : Lissan Koirala
# Date of Creation : 08/03/2020

import tkinter as tk
from tkinter import *

def terms_conditions(user_id):
    def ok():
        what = variable.get()
        
        file_name = "Terms and Conditions.txt"
        user = "The owner of " + user_id + " " + "\n" + what + "s" + " to the Terms and Conditions of our Software"
        f = open(file_name, 'w')
        f.write(user)
        f.close()
        win.destroy()

    win = Tk()
    lb = Label(win, text = "Gentle Warning")
    lb.grid(row = 0, column = 0)
    lb = Label(win, text = "Please only continue to this software if\nyou can recover your account as Facebook might\n ask you to confirm your identity sometimes for your account security.\nThis is a non Facebook application which will log you in to your\naccount and Facebook might thing think that you were not\nthe one who did it!")
    lb.grid(row = 1, column = 0)

    variable = StringVar(win)
    variable.set("Agree/Disagree") # default value

    w = OptionMenu(win, variable, "Agree","Disagree")
    w.grid(row = 2, column = 0)

    button = Button(win, text="OK", command=ok)
    button.grid(row = 3, column = 0)

    win.mainloop()



def save_info():
    global email
    global password
    global win
    
    final_email = email.get()
    final_password = password.get()

    f = open("email.txt",'w')
    f.write(final_email)
    f.close()

    g = open("password.txt",'w')
    g.write(final_password)
    g.close()

    win.destroy()

    terms_conditions(final_email)
    
    

win = tk.Tk()

label = tk.Label(win, text = "Credentials")
label.grid(row = 0, column = 0)

lb = tk.Label(win, text = "Email")
lb.grid(row = 1, column = 0)
email = tk.Entry(win)
email.grid(row = 1, column = 1)

lb = tk.Label(win, text = "Password")
lb.grid(row = 2, column = 0)
password = tk.Entry(win)
password.grid(row = 2, column = 1)

submit = tk.Button(win, text = "Submit", command = save_info)
submit.grid(row = 3, column = 1)

win.mainloop()


