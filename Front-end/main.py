#import Tkinter '*' means everything
from tkinter import*

#making a window of tkinter named root(we'll put everything in root0
root=Tk()
root.title("ryan ")


#function which instruct what to do when the button is clicked
def click():
    clicked=Label(root,text=e.get())
    clicked.pack()



#declaration of labels or buttons
label1=Label(root,text="Ryan's front end ")      #to decalre a label
button=Button(root,text=" Kick Me ",padx=50,pady=50,command=click,fg="white",bg="black")
e=Entry(root,width=50,borderwidth=10)

# pack or grid functions
label1.pack()
e.pack()
button.pack()



root.mainloop()
