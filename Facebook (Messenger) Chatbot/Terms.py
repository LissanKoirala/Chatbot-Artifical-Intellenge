# Creator : Lissan Koirala
# Date of Creation : 08/03/2020

from tkinter import *

def ok():
    global user_id
    
    what = variable.get()
    
    t = "Terms and Conditions"
    file_name = t + ".txt"
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

lb = Label(win, text = "Your Email ID")
lb.grid(row = 2, column = 0)
user_id = Entry(win)
user_id.grid(row = 3, column = 0)

variable = StringVar(win)
variable.set("Agree/Disagree") # default value

w = OptionMenu(win, variable, "Agree","Disagree")
w.grid(row = 4, column = 0)

button = Button(win, text="OK", command=ok)
button.grid(row = 5, column = 0)

win.mainloop()

