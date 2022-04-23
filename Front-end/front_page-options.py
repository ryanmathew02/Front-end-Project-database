import os
import sys
from tkinter import*
root=Tk()
root.title("Category ")
root.configure(bg="black")
root.geometry("600x400")

def genre_table():
    os.system('C:\python\python.exe E:/python/insert_genre_name.py')

def users_table():
    os.system('C:\python\python.exe E:/python/user_insert_update.py')


genre_name = Button(root,text='Genre table        ',padx=40,pady=30,command=genre_table,bg="blue",fg="white")
titles = Label(root,text='Ott_platform Management system ',padx=100,pady=60,fg="red",bg="black")
user = Button(root,text="User's table ",padx=40,pady=30,command=users_table,bg="blue",fg="white")


titles.grid(row=0,column=0,columnspan=2)
genre_name.grid(row=1,column=1)
user.grid(row=1,column=0)


root.mainloop()


