import os
import sys
import cx_Oracle
conn = cx_Oracle.connect(user="SYSTEM",password="nami",dsn="localhost")
print("succesfully connected to Oracle database ")
#print(conn.version)

from tkinter import*
root=Tk()
root.configure(bg="black")
root.geometry("530x500")
root.title("User_account Table")

def user_input():
    os.system('C:\python\python.exe E:/python/user_account.py')

def  user_output():
    os.system('C:\python\python.exe E:/python/user_show.py')

def quitting():
    root.destroy()

def removes():
    os.system('C:\python\python.exe E:/python/user_delete.py')

def change_password():
    os.system('C:\python\python.exe E:/python/update_password.py')


label1 = Label(root,text="SELECT THE OPERATION ",padx=100,pady=30,bg="green",fg="white")
temp=Label(root,text="                ",bg="black",fg="black")
temp2=Label(root,text="                ",bg="black",fg="black")
user_insert = Button(root,text="Insert Into User Account ",padx=60,pady=35,bg="blue",fg="white",command=user_input)
user_show = Button(root,text="Show values in the tables ",padx=60,pady=35,bg="blue",fg="white",command=user_output)
user_update = Button(root,text="Update the details ",padx=60,pady=35,bg="blue",fg="white",command=change_password)
user_remove = Button(root,text="Delete the details ",padx=60,pady=35,bg="blue",fg="white",command=removes)
quit = Button(root,text="Exit",padx=35,pady=30,bg="red",fg="white",command=quitting)


label1.grid(row=0,column=0,columnspan=2)
temp.grid(row=1,column=0)
user_insert.grid(row=2,column=0)
user_show.grid(row=2,column=1)
user_update.grid(row=3,columnspan=2)
user_remove.grid(row=4,columnspan=2)
temp2.grid(row=5,column=0)
quit.grid(row=6,columnspan=2)


root.mainloop()