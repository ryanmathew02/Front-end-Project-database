from tkinter import *

root=Tk()

button1=Button(root,text="1",padx=50,pady=50)
button2=Button(root,text="2",padx=50,pady=50)
button3=Button(root,text="3",padx=50,pady=50)

button4=Button(root,text="4",padx=50,pady=50)
button5=Button(root,text="5",padx=50,pady=50)
button6=Button(root,text="6",padx=50,pady=50)

button7=Button(root,text="7",padx=50,pady=50)
button8=Button(root,text="8",padx=50,pady=50)
button9=Button(root,text="9",padx=50,pady=50)

button0=Button(root,text="0",padx=50,pady=50)
button_clear=Button(root,text="Clear",padx=90,pady=50)
button_add=Button(root,text="+",padx=60,pady=50)
button_equal=Button(root,text="=",padx=60,pady=50)


# pack or grid to insert into root
e=Entry(root,width=50)

e.grid(row=0,column=0,columnspan=3)
button9.grid(row=1,column=0)
button8.grid(row=1,column=1)
button7.grid(row=1,column=2)

button6.grid(row=2,column=0)
button5.grid(row=2,column=1)
button4.grid(row=2,column=2)

button3.grid(row=3,column=0)
button2.grid(row=3,column=1)
button1.grid(row=3,column=2)

button0.grid(row=4,column=0)
button_clear.grid(row=4,column=1,columnspan=2)
button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)

button_add.grid(row=5,column=0)

root.mainloop()