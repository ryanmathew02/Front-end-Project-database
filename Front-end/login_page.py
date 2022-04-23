from tkinter import*
import cx_Oracle
conn = cx_Oracle.connect(user="SYSTEM",password="nami",dsn="localhost")
print(" Connection Successfull... ")
import os
import sys



root = tk()
root.title("login page")
root.configure(bg="black")
root.geometry("600x400")

login= Label(root,text="LOGIN",padx=100,pady=60)
username = Label(root,text=" User's email ",padx=40,pady=25,bg="black",fg="white")
password = Label(root,text="Password",padx=40,pady=25,bg="black",fg="white")

