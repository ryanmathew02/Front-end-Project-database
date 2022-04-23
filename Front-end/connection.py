import cx_Oracle
conn = cx_Oracle.connect(user="SYSTEM",password="nami",dsn="localhost")
#print("succesfully connected to Oracle database ")
#print(conn.version)

def insert_genre():
    movies_id = m_id_e.get()
    genres_id = id_e.get()
    cur=conn.cursor()
    insert_values ="insert into genre_type values('"+movies_id+"','"+genres_id+"')"
    cur.execute(insert_values)
    conn.commit()
    print(" values inserted ")

from tkinter import*
root=Tk()
root.title("Genre_name")
root.configure(bg="black")
root.geometry("600x400")


temp=Label(root,text=" ",bg="black")
title = Label(root,text="Table Genre_type",padx=80,pady=50,bg="black",fg="white")
movie_id = Label(root,text="Enter Movie's id ",padx=25,pady=15,bg="black",fg="white")
id = Label(root,text="Enter the Genre's ID",padx=25,pady=15,bg="black",fg="white")
insert = Button(root,text="INSERT",padx=40,pady=40,bg="blue",fg="white",command=insert_genre)
m_id_e=Entry(root,width=60,borderwidth=5)
id_e=Entry(root,width=60,borderwidth=5)

temp.grid(row=0,column=0)
title.grid(row=0,column=1)
movie_id.grid(row=1,column=0)
id.grid(row=2,column=0)
m_id_e.grid(row=1,column=1)
id_e.grid(row=2,column=1)
insert.grid(row=3,columnspan=2)

root.mainloop()
