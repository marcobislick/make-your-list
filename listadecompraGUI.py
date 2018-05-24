from tkinter import *
from tkinter import ttk
import glob
import os

#-----------------------------------------------------    Functions def
def center(root):                                                               #To Center root Window
    root.update_idletasks()
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    size = tuple(int(_) for _ in root.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    root.geometry("%dx%d+%d+%d" % (size + (x, y)))

def agregar(*args):                                                             #Adds input to list variable and displays it in output label
    if nuevoitem.get().strip(): 
        lista.append(nuevoitem.get())
        agregado.set('Tu lista contiene: ' + str(len(lista)) + " items")
    mainentry.delete(0, END)
    labeltext=""
    i=0
    for item in lista:
        i+=1
        labeltext += "{}. ".format(i) + item + "\n"
    listalabel.set(labeltext)
    return lista

def presstoclear(*args):                                                        #Clears list, entry widget and labels
    lista.clear()
    agregado.set('')
    mainentry.delete(0, END)
    listalabel.set("")

def load(*args):                                                                #displays in listbox the existen lists
    archivos = glob.glob("D:/python_projects/tkintergui/listas/*.txt")
    for archivo in archivos:
        remplazo = archivo.replace("D:/python_projects/tkintergui/listas\\", "")
        lista1.append(remplazo.replace(".txt", ""))
    periodo.set(lista1)
    return lista1

def configuracion(event):                                                      #Updates scrollregion of outputframe
    outcanvas.configure(scrollregion=outcanvas.bbox("all"))

def cargarlista(*args):                                                        #Loads/displays selected list into outputframe
    lista.clear()
    lista2=[]
    labeltext=""
    for i in menu.curselection():
        with open('D:/python_projects/tkintergui/listas/' + lista1[i] + '.txt', 'r') as listaload:
            listacargada = listaload.readlines()
            for item in listacargada:                           
                lista2.append(item.replace("\n",""))
    for item in lista2:
        i+=1
        lista.append(item)
        labeltext += "{}. ".format(i) + item + "\n"
    listalabel.set(labeltext)
    return labeltext, lista
    
#============================================
#-------------------------------------------------  Main Window    
root= Tk()
root.title("MakeYourList!")
root.geometry("800x800")
root.resizable(False, False)
center(root)
#==================================
#------------------------------------------- Variable Declaration
lista = []
nuevoitem = StringVar()
listalabel = StringVar()
agregado = StringVar()
periodo=StringVar()
lista1=[]
labeltext=""
#=======================================
#---------------------------------------------------- Styles
stilo=ttk.Style()
stilo.configure("My.TLabel",  background='lightskyblue1', foreground='black')
#======================================
#---------------------------------------------------  Frames
mainframe = ttk.Frame(root, relief='sunken')
mainframe.pack(fill=BOTH, expand=1)

leftframe = ttk.Frame(mainframe, relief='flat')
leftframe.pack(side=LEFT, pady=5, padx=5)

rightframe = ttk.Frame(mainframe, relief='sunken')
rightframe.pack(pady=8, padx=8, expand=1, fill=BOTH)

inputframe = ttk.Frame(leftframe, relief='flat')
inputframe.grid(column=1,row=5,padx=8)

buttonframe = ttk.Frame(leftframe, relief='flat')
buttonframe.grid(column=1, row=4)

loadsframe =ttk.Frame(leftframe)
loadsframe.grid(column=1, row=7)

listboxbuttons=ttk.Frame(leftframe)
listboxbuttons.grid(column=1, row=8)

#================================================
#--------------------------------------------------   ListBox
scrollbar=Scrollbar(loadsframe)
scrollbar.pack(side=RIGHT, fill=Y)

menu = Listbox(loadsframe, listvariable=periodo, background='turquoise', foreground='black', yscrollcommand=scrollbar.set, width=34)
menu.pack(padx=(5,0),pady=8, expand=1, fill=BOTH)

scrollbar.config(command=menu.yview)
#================================================
#--------------------------------------------------- Output Canvas
scroll=Scrollbar(rightframe)
scroll.pack(side=RIGHT, fill=Y)

outcanvas=Canvas(rightframe, yscrollcommand=scroll.set)
outcanvas.pack(expand=1, fill=BOTH, padx=1, pady=2)

outputframe = ttk.Frame(outcanvas)
outcanvas.create_window((0,0), window=outputframe,anchor=NW)

scroll.config(command=outcanvas.yview)
#=============================================
#---------------------------------------------------  Labels, Buttons, Entries

ttk.Label(inputframe, text="Ingresa un item y presiona 'enter'").pack()
mainentry = ttk.Entry(inputframe, textvariable=nuevoitem)
mainentry.pack(padx=5, pady=5)
ttk.Label(inputframe,textvariable=agregado).pack(padx=5, pady=5)

ttk.Label(outputframe, textvariable=listalabel, wraplength=400,width=46, relief='raised', font=("Courier", 14), style='My.TLabel').pack(expand=1, fill=Y,pady=5,padx=5, side=LEFT)

ttk.Button(buttonframe, text="Press to Clear", command=presstoclear).pack(expand=1, fill=X, pady=5, padx=5)

ttk.Button(listboxbuttons, text="Saved Lists", command=load).pack(side=LEFT,expand=1, fill=X, pady=5)
ttk.Button(listboxbuttons, text='Load list', command=cargarlista).pack(side=LEFT, expand=1, fill=X, pady=5, padx=5)
#======================================
#-----------------------------------------------   Bindings
mainentry.focus()
root.bind('<Return>', agregar)
outputframe.bind('<Configure>', configuracion)
#=====================================
#---------END-------------
root.mainloop()