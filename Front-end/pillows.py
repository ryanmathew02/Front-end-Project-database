from tkinter import*
root=Tk()
root.title("OTT_platform ")
root.geometry("600x400")
root.configure(bg='black')

def log():
    label = Label(root,text=user_e.get())
    label.grid(row=4,column=0,columnspan=2)
    label2 = Label(root,text=pass_e.get())
    label2.grid(row=5,column=0,columnspan=2)

temp=Label(root,text="     ",bg="black")
log_display=Label(root,text="LOG IN PAGE OTT PLATFORM",padx=100,pady=50,fg="red",bg="black")
username = Label(root,text="USER's EMAIL",padx=25,pady=10,fg="white",bg="black")
password = Label(root,text="password",padx=25,pady=10,fg="white",bg="black")
login = Button(root,text="Submit",padx=40,pady=40,command=log,bg="blue",fg="white")
user_e=Entry(root,width=55,borderwidth=5)
pass_e=Entry(root,width=55,borderwidth=5)

temp.grid(row=0,column=0)
log_display.grid(row=0,column=1)
username.grid(row=1,column=0)
password.grid(row=2,column=0)
user_e.grid(row=1,column=1)
pass_e.grid(row=2,column=1)
login.grid(row=3,column=1,columnspan=2)

root.mainloop()




