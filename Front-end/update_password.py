import cx_Oracle
conn = cx_Oracle.connect(user="SYSTEM",password="nami",dsn="localhost")
print("succesfully connected to Oracle database ")
#print(conn.version)

from tkinter import*
root=Tk()
root.configure(bg="black")
root.geometry("1000x650")
root.title("User_account Table")


cur=conn.cursor()
cur.execute("SELECT * FROM user_account")
i=0
for user_account in cur:
    for j in range(len(user_account)):
        e= Entry(root,width=25,fg="black")
        e.grid(row=i,column=j)
        e.insert(END,user_account[j])
    i=i+1

def new_password():
    users_id = input.get()
    new = new_input.get()
    cur = conn.cursor()
    update = " Update user_account set password='"+new+"' where user_id='"+users_id+"' "
    cur.execute(update)
    conn.commit()
    root.destroy()

def quitting():
    root.destroy()

label1 = Label(root,text="ENTER THE USER ID ",padx=40,pady=30,bg="black",fg="white")
input = Entry(root,width=50,borderwidth=5)
label2 = Label(root,text="ENTER THE NEW PASSWORD ",padx=40,pady=30,bg="black",fg="white")
new_input = Entry(root,width=50,borderwidth=5)
change = Button(root,text="Update",pady=25,padx=30,bg="red",fg="white",command=new_password)
quit = Button(root,text="Exit",padx=35,pady=30,bg="red",fg="white",command=quitting)


label1.grid(row=i+1,column=0,columnspan=3)
input.grid(row=i+1,column=4,columnspan=3)
label2.grid(row=i+2,column=0,columnspan=3)
new_input.grid(row=i+2,column=4,columnspan=3)
change.grid(row=i+3,column=4,columnspan=3)
quit.grid(row=i+4,columnspan=6)

root.mainloop()