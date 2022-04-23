import cx_Oracle
conn = cx_Oracle.connect(user="SYSTEM",password="nami",dsn="localhost")
print("succesfully connected to Oracle database ")
#print(conn.version)

from tkinter import*
root=Tk()
root.configure(bg="black")
root.geometry("1000x400")
root.title("User's table Details ")

def quitting():
    root.destroy()

cur=conn.cursor()
cur.execute("SELECT * FROM user_account")
i=0
for user_account in cur:
    for j in range(len(user_account)):
        e= Entry(root,width=25,fg="black")
        e.grid(row=i,column=j)
        e.insert(END,user_account[j])
    i=i+1

quit = Button(root,text="Exit",padx=20,pady=10,bg="red",fg="white",command=quitting)
quit.grid(row=i+1,columnspan=6)

root.mainloop()