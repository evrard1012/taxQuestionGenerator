from tkinter import *
import time
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfile



def main():
    root=Tk()
    app=Window_Accueil_Etudiant(root)

class Window_Accueil_Etudiant:

    def __init__(self, master):
        self.master=master
        self.master.title("Page Accueil")
        self.master.geometry("800x650")
        self.master.config(bg="powder blue")

        
        
        self.frame=Frame(self.master,bg="powder blue")
        self.frame.pack()

        self.frame1=Frame(self.frame,bg="powder blue")
        
        

        self.frame1.pack()
        
        
        self.nombreQuestion= IntVar()
        
        self.nombreQtsFrame=LabelFrame(self.frame1,width=135,height=20,font=('arial',20,'bold')
                                   ,relief='ridge',fg='cadet blue',bd=20)
        self.nombreQtsFrame.grid(row=0,column=0,pady=200)
        

        #########################'
        self.lblnombreQts=Label(self.nombreQtsFrame,text='Nombre de Questions',
                           font=('arial',20,'bold'))
        self.lblnombreQts.grid(row=0,column=0)

        self.lblnombreQts=Label(self.nombreQtsFrame,text='Valeur',
                           font=('arial',20,'bold'))
        self.lblnombreQts.grid(row=1,column=0)

        self.ent1=Entry(self.nombreQtsFrame,textvariable= self.nombreQuestion.get(),width=15)
        self.ent1.grid(row=1,column=1)

        ######################### button
        self.btnQts=Button(self.nombreQtsFrame,text = 'Debuter',width=17,command=self.debuter)
        self.btnQts.grid(row=2,column=1,pady=20,padx=10)

        ######################deconexion
        self.btnDcx=Button(self.nombreQtsFrame,text = 'deconexion',width=17,command=self.iExit)
        self.btnDcx.grid(row=2,column=0,pady=20,padx=10)

    def debuter(self):
        valeur=self.ent1.get()
        if self.ent1.get()=='':
            messagebox.showinfo("Alert", "renseignez bien le nombre de question!!!")
        else:
            print("la valeur est :",valeur)
            self.nombreQuestion=IntVar()

        

    def iExit(self):
        self.iExit=messagebox.askyesno('Voulez vous vraiment quitter !!')
        if self.iExit>0:
            self.master.destroy()




    

main()

