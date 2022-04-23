import cx_Oracle
conn = cx_Oracle.connect(user="SYSTEM",password="nami",dsn="localhost")
print("succesfully connected to Oracle database ")
#print(conn.version)

from tkinter import*
root=Tk()
root.configure(bg="black")
root.geometry("900x650")
root.title("User_account Table")


def insert_user():
    id = e_id.get()
    name = e_name.get()
    email = e_email.get()
    password = e_password.get()
    phone = e_phone.get()
    address = e_address.get()
    cur=conn.cursor()
    insert_values = "insert into user_account values('" + id + "','" + name + "','" + email +"','" + password +"','"+ phone +"','"+ address +"')"
    cur.execute(insert_values)
    conn.commit()
    print(" Value Inserted ")
    success = Label(root,text="Values inserted",)
    success.grid(row=8,column=0)
    e_name.delete(0,END)
    e_email.delete(0, END)
    e_password.delete(0, END)
    e_phone.delete(0, END)
    e_address.delete(0, END)
    e_id.delete(0, END)

def out():
    root.destroy()


#labels
temp = Label(root,text="       ",padx=100,pady=30,bg="black",fg="black")
details = Label(root,text="Enter the New Users details ",padx=100,pady=30,bg="green",fg="white")
user_id = Label(root,text="Enter user_id",padx=40,pady=25,bg="black",fg="white")
user_name = Label(root,text="Enter username",padx=40,pady=25,bg="black",fg="white")
user_email = Label(root,text="Enter email",padx=40,pady=25,bg="black",fg="white")
user_password = Label(root,text="Enter password",padx=40,pady=25,bg="black",fg="white")
user_phone = Label(root,text="Enter phone number",padx=40,pady=25,bg="black",fg="white")
user_address = Label(root,text="Enter address",padx=40,pady=25,bg="black",fg="white")
submit = Button(root,text="SUBMIT",padx=30,pady=20,bg="blue",fg="white",command=insert_user)
quit = Button(root,text="Exit",padx=30,pady=20,bg="red",fg="white",command=out)


#entries
e_id = Entry(root,width=60,borderwidth=5)
e_name = Entry(root,width=60,borderwidth=5)
e_email = Entry(root,width=60,borderwidth=5)
e_password = Entry(root,width=60,borderwidth=5)
e_phone = Entry(root,width=60,borderwidth=5)
e_address = Entry(root,width=60,borderwidth=5)

#pack
temp.grid(row=0,column=0)
details.grid(row=0,column=1)
user_id.grid(row=1,column=0)
user_name.grid(row=2,column=0)
user_email.grid(row=3,column=0)
user_password.grid(row=4,column=0)
user_phone.grid(row=5,column=0)
user_address.grid(row=6,column=0)

e_id.grid(row=1,column=1)
e_name.grid(row=2,column=1)
e_email.grid(row=3,column=1)
e_password.grid(row=4,column=1)
e_phone.grid(row=5,column=1)
e_address.grid(row=6,column=1)

quit.grid(row=8,column=1)
submit.grid(row=7,column=1)


root.mainloop()