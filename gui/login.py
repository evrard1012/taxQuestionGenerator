import tkinter as tk
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime

import alino.entity.users as usr
import alino.dao.userdao as udao
from menu_student import MenuUser
from menu_prof import Home

class Login:
    iduser=0
    idoffice=0
    def __init__(self,master):
        self.master=master
        self.master.title("Systeme de GEstion Commerciale")

        self.filename = PhotoImage(file = "background3.png")
        w = self.master.winfo_screenwidth()
        h = self.master.winfo_screenheight()
        self.master.geometry("%dx%d+0+0" % (w, h))
        
        #self.master.geometry('1350x750+0+0')
        self.master.config(bg="powder blue")

        self.C = Canvas(self.master, bg="blue", height=250, width=300)
        self.background_label = Label(self.master, image=self.filename)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.C.pack()
        
        self.frame=Frame(self.master,bg="grey")
        self.frame.pack()

        self.Username=StringVar()
        self.PassWord=StringVar()

        self.lblTitle=Label(self.frame,text='CONNEXION',font=('italique',28,'bold'),bg='white',fg='black')
        self.lblTitle.grid(row=0,column=0,columnspan=2,pady=40)
        # frame de login,
        self.LoginFrame1=LabelFrame(self.frame,width=1350,height=100,font=('arial',20,'bold'),relief='ridge',fg='cadet blue',bd=20)
        self.LoginFrame1.grid(row=1,column=0)

        # labels et champs de saisie
        self.lblUsername=Label(self.LoginFrame1,text='Username',font=('arial',20,'bold'))
        self.lblUsername.grid(row=0,column=0)
        self.txtUsername=Entry(self.LoginFrame1,font=('arial',20,'bold'),textvariable=self.Username)
        self.txtUsername.grid(row=0,column=1)


        self.lblPassWord=Label(self.LoginFrame1,text='PassWord',font=('arial',20,'bold'))
        self.lblPassWord.grid(row=1,column=0)
        self.txtPassWord=Entry(self.LoginFrame1,font=('arial',20,'bold'),show='*',textvariable=self.PassWord)
        self.txtPassWord.grid(row=1,column=1)

        # boutons 
        
        self.btnLogin=Button(self.LoginFrame1,text = 'Login',width=17,command=self.Login_System,bg='blue')#self.new_window#
        self.btnLogin.grid(row=3,column=0,pady=20,padx=10)

        self.btnExit=Button(self.LoginFrame1,text = 'Exit',width=17,command=self.iExit,bg='red')
        self.btnExit.grid(row=3,column=1,pady=20,padx=10)
        #----------------------------------fonction -------------------------
    def Login_System(self):
        u=(self.Username.get())
        p=(self.PassWord.get())
        user = udao.login(u,p)
        if user is not None :
            iduser=user[0]
            idoffice=user[6]
            print('welcome')
            profil = user[3]
            if profil == 1:
                print('admin')
                self.command()
            elif profil ==2:
                print('commercant')
                self.command_com()
            elif profil ==3:
                print('gestionnaire fournisseur')
                self.command_gf()
            elif profil ==4:
                print('gestionnaire stock')
                self.command_gs()
            else:
                print('erreur')
        else:
            print('failed')
        

        
    def Rest(self):
        self.Username.set('')
        self.PassWord.set('')
        self.txtUsername.focus()

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
        app = MenuUser(toplevel)
    def command_com(self):
        self.master.withdraw()
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("350x350")
        app = cp.CommanderHome(toplevel)
    def command_gs(self):
        self.master.withdraw()
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("350x350")
        app = Home(toplevel)
    def command_gf(self):
        self.master.withdraw()
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("350x350")
        app = HomeGestFournisseur(toplevel)        

root = tk.Tk()
root.title("window")
root.geometry("1178x782")
cls = Login(root)
root.mainloop()
