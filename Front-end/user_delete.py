import cx_Oracle
conn = cx_Oracle.connect(user="SYSTEM",password="nami",dsn="localhost")
print("succesfully connected to Oracle database ")
#print(conn.version)

from tkinter import*
root=Tk()
root.configure(bg="black")
root.geometry("900x650")
root.title("User_account Table delete ")


cur=conn.cursor()
cur.execute("SELECT * FROM user_account")
i=0
for user_account in cur:
    for j in range(len(user_account)):
        e= Entry(root,width=25,fg="black")
        e.grid(row=i,column=j)
        e.insert(END,user_account[j])
    i=i+1


def delete_value():
    users_id = e_user_id.get()
    cur = conn.cursor()
    remove = " delete from user_account where user_id ='"+users_id+"' "
    cur.execute(remove)
    conn.commit()
    root.destroy()


def quitting():
    root.destroy()

user_id = Label(root,text="Enter the user ID",padx=40,pady=30,bg="black",fg="white")
e_user_id = Entry(root,width=30,borderwidth=5)
det = Button(root,text="delete",padx=30,pady=10,bg="red",fg="white",command=delete_value)
quit = Button(root,text="Exit",padx=15,pady=10,bg="blue",fg="white",command=quitting)

user_id.grid(row=i+1,column=0,columnspan=6)
e_user_id.grid(row=i+2,column=0,columnspan=6)
det.grid(row=i+3,column=0,columnspan=6)
quit.grid(row=i+4,columnspan=6)

root.mainloop()


