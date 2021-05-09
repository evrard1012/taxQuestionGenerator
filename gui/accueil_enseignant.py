from tkinter import *
import time
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfile


def execr():
    return askopenfile(mode='r', filetypes=[("CSV Files","*.csv")])

def main():
    root=Tk()
    app=Window_Accueil_Ensiegnant(root)

class Window_Accueil_Ensiegnant:

    def __init__(self, master):
        self.master=master
        self.master.title("Page Accueil")
        self.master.geometry("850x600")
        self.master.config(bg="powder blue")

        
        
        self.frame=Frame(self.master,bg="powder blue")
        self.frame.pack()

        self.frame1=Frame(self.frame,bg="powder blue")
        self.frame4=Frame(self.frame,bg="powder blue")
        self.frame2=Frame(self.frame,bg="powder blue")
        self.frame3=Frame(self.frame,bg="powder blue")
        

        self.frame1.pack()
        self.frame4.pack()
        self.frame2.pack()
        self.frame3.pack(side=LEFT)
        
        #self.frame2.pack_propagate(False)
        
        self.liste=[]
        self.nomFichier= StringVar()
        self.montants=StringVar()
        self.nomFichier.set('')
        
        self.fileFrame=LabelFrame(self.frame1,width=135,height=10,font=('arial',20,'bold')
                                   ,relief='ridge',fg='cadet blue',bd=20)
        self.fileFrame.grid(row=0,column=0,pady=40)

        self.montantFrame=LabelFrame(self.frame2,width=135,height=10,font=('arial',20,'bold')
                                   ,relief='ridge',fg='cadet blue',bd=20)
        self.montantFrame.grid(row=0,column=0,pady=40)

        

        #########################'
        self.lblfile=Label(self.fileFrame,text='chargement automatique',
                           font=('arial',20,'bold'))
        self.lblfile.grid(row=0,column=0,padx=10)
        
        self.lblfile=Label(self.fileFrame,text='fichier au format CSV',
                           font=('arial',20,'bold'))
        self.lblfile.grid(row=1,column=0)

        self.fileChr=Entry(self.fileFrame,text=self.nomFichier,state='disabled',
                           font=('arial',20,'bold'))
        self.fileChr.grid(row=2,column=0,padx=10)
        ######################### button
        self.btnchg=Button(self.fileFrame,text = 'Choisir',width=17,
                           command=lambda:self.open_file())
        self.btnchg.grid(row=1,column=1,pady=20,padx=10)

        self.btnchg=Button(self.fileFrame,text = 'valider',width=17,command=lambda:self.uploadFiles())
        self.btnchg.grid(row=2,column=1,pady=20,padx=10)

        ###########################
        self.lblfile=Label(self.montantFrame,text='renseignez les montants',
                           font=('arial',20,'bold'))
        self.lblfile.grid(row=4,column=0,padx=10)
        
        self.ent1=Entry(self.montantFrame,textvariable=self.montants,width=55)
        self.ent1.grid(row=5,column=0,padx=5,pady=3)
        ########################## boutton
        self.btnMts=Button(self.montantFrame,text = 'valider',width=17,command=self.valider())
        self.btnMts.grid(row=5,column=1,pady=20,padx=10)

        ######################deconexion
        self.btnDcx=Button(self.frame3,text = 'deconexion',width=17,command=self.valider())
        self.btnDcx.grid(row=0,column=0,pady=20,padx=10)

    def valider(self):
        list_montants=self.montants.get()
        self.montants.set('')
        print(list_montants)


    def open_file(self):
        file_path = execr()
        if file_path is not None:
            #print(file_path)
            #print(file_path.name)
            nom=file_path.name
            print(nom)
            self.nomFichier.set(nom)
            print(self.nomFichier.get())
            with open(file_path.name) as f:
                mylist = [line.rstrip('\n') for line in f]
            pass
            self.liste=mylist
            

    def uploadFiles(self):
        pb1 = ttk.Progressbar(self.frame4,
                      orient=HORIZONTAL,
                      length=300,
                      mode='determinate')
        pb1.grid(row=1, pady=20)
        for i in range(5):
            self.frame4.update_idletasks()
            pb1['value'] += 20
            time.sleep(1)
        pb1.destroy()
        self.nomFichier.set('')
        ttk.messagebox.askyesno('fichier charge avec success !!')
        Label(self.frame4, text='File Uploaded Successfully!',
              foreground='green').grid(row=2, pady=10)



    

#main()

