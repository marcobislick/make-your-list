from tkinter import *
from tkinter import ttk
import glob
import os
#import re

#-----------------------------------------------------    Functions def
def center(root):
    root.update_idletasks()
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    size = tuple(int(_) for _ in root.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    root.geometry("%dx%d+%d+%d" % (size + (x, y)))

def agregar(*args):
    #if re.search('[a-zA-Z]', nuevoitem.get()):
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

def presstoclear(*args):
    lista.clear()
    agregado.set('')
    mainentry.delete(0, END)
    listalabel.set("")

def load():
    a=[]
    i=0
    archivos = glob.glob("D:/python_projects/tkintergui/listas/*.txt")
    for archivo in archivos:
        i+=1
        remplazo = archivo.replace("D:/python_projects/tkintergui/listas\\", "")
        a.append("{}. ".format(i) + remplazo.replace(".txt", ""))
    loads.set("Listas disponibles:\n" + "\n".join(a))

def configuracion(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=200,height=200)

def configuracion2(event):
    outcanvas.configure(scrollregion=outcanvas.bbox("all"),height=1000)

def clearlist():
    loads.set("")
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
listalabel2=StringVar()
agregado = StringVar()
loads = StringVar()
#=======================================
#---------------------------------------------------- Styles
stilo=ttk.Style()
stilo.configure("My.TLabel",  background='turquoise', foreground='black')
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

loadbuttons=ttk.Frame(leftframe)
loadbuttons.grid(column=1, row=8)

#================================================
#--------------------------------------------------   Load Canvas
scrollbar=Scrollbar(loadsframe)
scrollbar.pack(side=RIGHT, fill=Y)

canvas=Canvas(loadsframe, yscrollcommand=scrollbar.set,scrollregion=(0,0,500,500), background='turquoise')
canvas.pack(side=LEFT, fill=BOTH, expand=1, padx=5)

elframe=ttk.Frame(canvas)
canvas.create_window((0,0),window=elframe,anchor=NW)

scrollbar.config(command=canvas.yview)
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

cargadito= ttk.Label(elframe, textvariable=loads, width=31, style="My.TLabel" )
cargadito.pack(expand=1, fill=Y)

ttk.Label(outputframe, textvariable=listalabel, wraplength=400,width=46, relief='raised', font=("Courier", 14), style='My.TLabel').pack(expand=1, fill=Y,pady=5,padx=5, side=LEFT)

ttk.Button(buttonframe, text="Press to Clear", command=presstoclear).pack(expand=1, fill=X, pady=5, padx=5)

ttk.Button(loadbuttons, text="Saved Lists", command=load).pack(side=LEFT,expand=1, fill=X, pady=5)
ttk.Button(loadbuttons, text='Clear lists', command=clearlist).pack(side=LEFT, expand=1, fill=X, pady=5, padx=5)
#======================================
#-----------------------------------------------   Bindings
mainentry.focus()
root.bind('<Return>', agregar)
elframe.bind('<Configure>', configuracion)
outputframe.bind('<Configure>', configuracion2)
#=====================================
#---------END-------------
root.mainloop()