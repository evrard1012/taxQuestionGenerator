import tkinter as tk
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime

import alino.entity.users as usr
import alino.dao.userdao as udao


class Home:
    def __init__(self,master):
        self.master=master
        self.master.title("Systeme de Generation QCM")

        self.filename = PhotoImage(file = "background.png")
        w = self.filename.width()
        h = self.filename.height()
        self.master.geometry("%dx%d+0+0" % (w, h))
        
        #self.master.geometry('1350x750+0+0')
        self.master.config(bg="powder blue")

        self.C = Canvas(self.master, bg="blue", height=150, width=500)
        self.background_label = Label(self.master, image=self.filename)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.C.pack()
        
        self.frame=Frame(self.master,bg="red")
        self.frame.pack()

        self.lblTitle=Label(self.frame,text='BIENVENUE PROF',font=('italique',28,'bold'),bg='white',fg='black')
        self.lblTitle.grid(row=0,column=0,columnspan=2,pady=40)
        # frame de login,
        self.LoginFrame1=LabelFrame(self.frame,width=60,height=100,font=('arial',20,'bold'),relief='ridge',fg='cadet blue',bd=20)
        self.LoginFrame1.grid(row=1,column=0)


        # boutons 
        
        self.btnLogin=Button(self.LoginFrame1,text = 'CONFIGS',width=25,command=self.Rest,bg='blue')#self.new_window#
        self.btnLogin.grid(row=0,column=0,pady=30,padx=10)

        

        self.btnLogin=Button(self.LoginFrame1,text = 'DECONNECTER',width=25,command=self.iExit,bg='blue')#self.new_window#
        self.btnLogin.grid(row=0,column=1,pady=30,padx=10)

        #----------------------------------fonction -------------------------

    def Rest(self):
        print('test')

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno('Voulez vous vraiment quitter !!')
        if self.iExit>0:
            self.master.destroy()
    def new_window(self):
        self.newWindow=Toplevel(self.master)
        #self.app=Window2(self.newWindow)
    def command(self):
        self.master.withdraw()
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("350x350")
        #app = windowclass(toplevel)
#root = tk.Tk()
#root.title("window")
#root.geometry("1178x782")
#cls = Home(root)
#root.mainloop()
