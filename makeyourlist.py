#---------------------------------------------------    Imports
from tkinter import *
from tkinter import ttk
import glob
import os

#===================================================
#---------------------------------------------------    Functions definition
def center(root):
    "To Center root Window"
    root.update_idletasks()
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    size = tuple(int(_) for _ in root.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    root.geometry("%dx%d+%d+%d" % (size + (x, y)))

def agregar(*args):
    "Adds input to list variable and displays it in output label"
    if nuevoitem.get().strip():
        original_list.append(nuevoitem.get())
        sortedlist.append(nuevoitem.get())
        agregado.set('Tu lista contiene: ' + str(len(original_list)) + " items")
        display_list.append("{}. ".format(len(original_list)) + nuevoitem.get())  
    mainentry.delete(0, END)
    listalabel.set(display_list)
    return display_list, original_list, sortedlist

def presstoclear(*args):
    "Clears list, entry widget and labels"
    display_list.clear()
    original_list.clear()
    sortedlist.clear()
    agregado.set('')
    mainentry.delete(0, END)
    listalabel.set("")

def load(*args):
    "displays in listbox the existen lists"
    loadedfiles.clear()
    global pathvar
    pathvar = load_entry_path.get()
    if load_radiobutton.get() == 'default':
        try:
            archivos = glob.glob(dir_path + "/*.txt")
            for archivo in archivos:
                txtfiles = archivo.replace(dir_path[0:len(dir_path)], "")
                loadedfiles.append(txtfiles[1:len(txtfiles)].replace(".txt", ""))
            agregado.set('Estas son las listas existentes')
        except:
            agregado.set("Parece que esta direccion no existe")
    elif load_radiobutton.get() == 'custom':
        try:
            if pathvar[len(pathvar)-1] == '/':
                archivos = glob.glob(pathvar + "*.txt")
                print('custom file path with /')
                for archivo in archivos:
                    txtfiles = archivo.replace(pathvar[0:len(pathvar)-1], "")
                    loadedfiles.append(txtfiles[1:len(txtfiles)].replace(".txt", ""))
                agregado.set('Estas son las listas existentes')
            else:
                archivos = glob.glob(pathvar + "/*.txt")
                for archivo in archivos:
                    txtfiles = archivo.replace(pathvar+"\\", "")
                    loadedfiles.append(txtfiles.replace(".txt", ""))
                agregado.set('Estas son las listas existentes')
        except:
            agregado.set('Parece que esta no es una direccion valida')
    listboxdisplay.set(loadedfiles)
    return pathvar, loadedfiles

def loadlistfile(*args):
    "Loads/displays selected list into outputframe"
    i=0
    if load_radiobutton.get() == 'default':
        try:
            with open(load_entry_path.get()+ "/" + loadedfiles[menu.curselection()[0]] + '.txt', 'r') as listaload:
                display_list.clear()
                original_list.clear()
                sortedlist.clear()
                for item in listaload.readlines():
                    i+=1                          
                    display_list.append("{}. ".format(i) + item.replace("\n",""))
                    original_list.append(item.replace('\n',""))
                    sortedlist.append(item.replace('\n',""))
                agregado.set('Se ha cargado la lista "{}"'.format(loadedfiles[menu.curselection()[0]])+ ' exitosamente')
        except:
            agregado.set('Error al cargar, asegurate de haber seleccionado una lista')
    elif load_radiobutton.get() == 'custom':
        if load_entry_path.get()[len(load_entry_path.get())-1] == '/':
            try:
                with open(load_entry_path.get() + loadedfiles[menu.curselection()[0]] + '.txt', 'r') as listaload:
                    display_list.clear()
                    original_list.clear()
                    sortedlist.clear()
                    for item in listaload.readlines():
                        i+=1                          
                        display_list.append("{}. ".format(i) + item.replace("\n",""))
                        original_list.append(item.replace('\n',""))
                        sortedlist.append(item.replace('\n',""))
                agregado.set('Se ha cargado la lista "{}"'.format(loadedfiles[menu.curselection()[0]])+ ' exitosamente')
            except:
                agregado.set('Error al cargar, asegurate de haber seleccionado una lista')
        else:
            try:
                with open(load_entry_path.get() + "/" + loadedfiles[menu.curselection()[0]] + '.txt', 'r') as listaload:
                    display_list.clear()
                    original_list.clear()
                    sortedlist.clear()
                    for item in listaload.readlines():
                        i+=1                          
                        display_list.append("{}. ".format(i) + item.replace("\n",""))
                        original_list.append(item.replace('\n',""))
                        sortedlist.append(item.replace('\n',""))
                agregado.set('Se ha cargado la lista "{}"'.format(loadedfiles[menu.curselection()[0]])+ ' exitosamente')
            except:
                agregado.set('Error al cargar, asegurate de haber seleccionado una lista')
    listalabel.set(display_list)
    return display_list, original_list, sortedlist

def removeitem(*args):
    "Deletes Selected List item"
    i=0
    if original_list != sortedlist:
        display_list.clear()
        popvariable = sortedlist.pop(outmenu.curselection()[0])
        agregado.set('Se ha eliminado "{}" de tu lista'.format(popvariable))
        original_list.remove(popvariable)
        for item in sortedlist:
            i+=1
            display_list.append('{}. '.format(i) + item)
    elif outmenu.curselection():
        display_list.clear()
        popvariable=original_list.pop(outmenu.curselection()[0])
        agregado.set('Se ha eliminado "{}" de tu lista'.format(popvariable))
        sortedlist.pop(outmenu.curselection()[0])
        for item in original_list:
            i+=1
            display_list.append("{}. ".format(i) + item)
    listalabel.set(display_list)
    return original_list, display_list, sortedlist

def sortear(*args):
    "Sorts lists"
    display_list.clear()
    sortedlist.sort()
    i=0
    for item in sortedlist:
        i+=1
        display_list.append("{}. ".format(i) + item)
    listalabel.set(display_list)
    return display_list, sortedlist

def save_list(*args):
    "Saves list in path as name"
    selection = pathselection.get()
    path = savepath.get()
    listname = listsavename.get()
    if listname.strip():
        if selection == 'custom':
            if path[len(path)-1] == "/":
                try:
                    with open(path + "/" + listname + '.txt', 'w') as savefile:
                        for item in original_list:
                            savefile.write(item + '\n')
                    savelabel.set('Tu lista se ha guardado exitosamente')
                except:
                    savelabel.set('Parece que has ingresado un nombre o direccion no valido.')
            else:
                try:
                    with open(path + "/" + listname + '.txt', 'w') as savefile:
                        for item in original_list:
                            savefile.write(item + '\n')
                    savelabel.set('Tu lista se ha guardado exitosamente')
                except:
                    savelabel.set('Parece que has ingresado un nombre o direccion no valido.')
        elif selection == 'default':
            try:
                with open(dir_path + "/" + listname + '.txt', 'w') as savefile:
                    for item in original_list:
                        savefile.write(item + '\n')
                savelabel.set('Tu lista se ha guardado exitosamente')
            except:
                savelabel.set('Parece que has ingresado un nombre no valido')
        else:
            savelabel.set('Debes seleccionar un directorio!')
    else:
        savelabel.set('Ingresa un nombre para tu lista!')


def radioevent1(*args):
    "radiobutton1 click event"
    savepath.set(dir_path)
    savepathentry.configure(state='readonly')

def radioevent2(*args):
    "radiobutton1 click event"
    savepath.set('D:/')
    savepathentry.configure(state='normal')

def defaultpath(*args):
    "Defaultpath radiobutton click event"
    load_entry_path.set(dir_path)
    loadpathentry.configure(state='readonly')

def custompath(*args):
    "Custompath radiobutton click event"
    load_entry_path.set('D:/')
    loadpathentry.configure(state='normal')

def deletefile(*args):
    "Deletes selected file from system"
    selectedfile=loadedfiles[menu.curselection()[0]]
    if pathvar == dir_path:
        try:
            os.remove(dir_path + "/" + selectedfile + ".txt")
            load()
            agregado.set('Se ha eliminado el archivo {}.txt satisfactoriamente'.format(selectedfile))
        except:
            agregado.set("Ha ocurrido un error, asegurate de tener seleccionada una lista")
    else:
        try:
            if pathvar[len(pathvar)-1] == '/':
                os.remove(pathvar + loadedfiles[menu.curselection()[0]] + ".txt")
                load()
                agregado.set('Se ha eliminado el archivo {}.txt satisfactoriamente'.format(selectedfile))
            else:
                os.remove(pathvar + '/' + loadedfiles[menu.curselection()[0]] + ".txt")
                load()
                agregado.set('Se ha eliminado el archivo {}.txt satisfactoriamente'.format(selectedfile))
        except:
            agregado.set("Ha ocurrido un error, asegurate de tener seleccionada una lista")


#===================================================
#---------------------------------------------------    Main Window    
root= Tk()
root.title("MakeYourList!")
root.geometry("800x800")
root.resizable(False, False)
root.option_add('*tearOff', False)
#===================================================
#---------------------------------------------------    Menubar
menubar = Menu(root)
root['menu'] = menubar
menu_file = Menu(menubar)
menu_edit = Menu(menubar)
menubar.add_cascade(menu=menu_file, label='File')
menubar.add_cascade(menu=menu_edit, label='Edit')
menu_file.add_command(label='New')
menu_file.add_command(label='Open...')
menu_file.add_command(label='Close')
menu_file.add_separator()
menu_file.add_command(label='Test')
#===================================================
#---------------------------------------------------    Variable Declaration
nuevoitem = StringVar()
listalabel = StringVar()
agregado = StringVar()
listboxdisplay=StringVar()
savepath = StringVar()
listsavename = StringVar()
savelabel = StringVar()
pathselection = StringVar()
load_radiobutton=StringVar()
load_entry_path=StringVar()

display_list = []
original_list=[]
loadedfiles=[]
sortedlist=[]

pathvar=""
dir_path = os.path.dirname(os.path.realpath(__file__))
#===================================================
#---------------------------------------------------    Styles
stilo=ttk.Style()
stilo.configure("My.TLabel",  background='lightskyblue1', foreground='black')

stilo2=ttk.Style()
stilo2.configure("My.TFrame", background='lightskyblue4')
#===================================================
#---------------------------------------------------    Frames Declaration and packing/griding

mainframe = ttk.Frame(root, relief='sunken')
mainframe.pack(fill=BOTH, expand=1)

leftframe = ttk.Frame(mainframe, relief='flat')
leftframe.pack(side=LEFT, pady=5, padx=5,anchor=N)

rightframe = ttk.Frame(mainframe, relief='sunken')
rightframe.pack(pady=(8,0), padx=8, expand=1, fill=BOTH)

saveframe = ttk.Frame(mainframe, relief='flat')
saveframe.pack(padx=(8,27), expand=1, fill=BOTH, anchor=S, side=RIGHT)

buttonframe = ttk.Frame(leftframe, relief='flat')
buttonframe.grid(column=1, row=4)

inputframe = ttk.Frame(leftframe, relief='flat')
inputframe.grid(column=1,row=5,padx=5, sticky=(W,E,N,S))

radiobuttonsframe=ttk.Frame(leftframe)
radiobuttonsframe.grid(column=1, row=6, sticky=(W,E))

listboxframe =ttk.Frame(leftframe)
listboxframe.grid(column=1, row=7)

loadpathentry=ttk.Frame(leftframe)
loadpathentry.grid(column=1, row=8,padx=5, pady=5)

listboxbuttons=ttk.Frame(leftframe)
listboxbuttons.grid(column=1, row=9, padx=(0,15))

#===================================================
#---------------------------------------------------    Loading Listbox declaration and packing

scrollbar=Scrollbar(listboxframe)
scrollbar.pack(side=RIGHT, fill=Y)

menu = Listbox(listboxframe, listvariable=listboxdisplay, background='turquoise', foreground='black', yscrollcommand=scrollbar.set, width=34)
menu.pack(padx=(5,0),pady=(8,0), expand=1, fill=BOTH)

scrollbar.config(command=menu.yview)

#===================================================
#---------------------------------------------------    Output Listbox declaration and packing

scroll=Scrollbar(rightframe)
scroll.pack(side=RIGHT, fill=Y)

outmenu=Listbox(rightframe,listvariable=listalabel, background='lightskyblue1',relief='raised', font=("Courier", 14), foreground='black', yscrollcommand=scroll.set)
outmenu.pack(expand=1, fill=BOTH, padx=2, pady=2)

scroll.config(command=outmenu.yview)

#===================================================
#---------------------------------------------------    Widgets inside inputframe

ttk.Label(inputframe, text="Ingresa un item y presiona 'enter'").pack()
mainentry = ttk.Entry(inputframe, textvariable=nuevoitem)
mainentry.pack(padx=5, pady=(5,0))
Label(inputframe,textvariable=agregado, wraplength=221, justify=CENTER, height=3).pack(padx=5, pady=6, expand=1, fill=BOTH)

#===================================================
#---------------------------------------------------    Widgets inside buttonframe

ttk.Button(buttonframe, text="Press to Clear", command=presstoclear).pack(expand=1, fill=X, pady=5, padx=5)

#===================================================
#---------------------------------------------------    Widgets inside listboxbuttons

ttk.Button(listboxbuttons, text="Show files", command=load).pack(side=LEFT,expand=1, fill=X, pady=(1,5), padx=8)
ttk.Button(listboxbuttons, text='Load list', command=loadlistfile).pack(side=LEFT, expand=1, fill=X, pady=(1,5), padx=8)

#===================================================
#---------------------------------------------------    Widgets inside leftframe

ttk.Button(leftframe, text='Remove Item', command=removeitem).grid(column=1, row=0, padx=2,pady=(50,10), sticky=E) 
ttk.Button(leftframe, text='Sort List', command=sortear).grid(column=1, row=1,padx=2, sticky=E, pady=(0,150))
ttk.Button(leftframe, text='Delete File', command=deletefile).grid(column=1,row=10)

#===================================================
#---------------------------------------------------    Widgets inside saveframe

ttk.Button(saveframe, text='Save list', command=save_list).grid(column=5,row=0, padx=(5,1), pady=3, columnspan=2,sticky=E)
ttk.Entry(saveframe, textvariable=listsavename).grid(column=4,row=0,pady=2, sticky=E, padx=(5,0))
ttk.Label(saveframe, text="as").grid(column=3,row=0, padx=(5,0),pady=2)
savepathentry=ttk.Entry(saveframe, textvariable=savepath)
savepathentry.grid(column=2,row=0,padx=(5,0),pady=2)
ttk.Label(saveframe, text='Save in').grid(column=1,row=0,padx=(5,0),pady=2)
defaultradiobutton=ttk.Radiobutton(saveframe, text='Default Path', variable=pathselection, value='default')
defaultradiobutton.grid(column=0,row=0,padx=(8,2), pady=2)
customradiobutton=ttk.Radiobutton(saveframe, text='Custom Path', variable=pathselection, value='custom')
customradiobutton.grid(column=0,row=1, pady=(0,8), padx=(12,2))
ttk.Label(saveframe, textvariable=savelabel).grid(column=2,row=1, columnspan=3,pady=(0,10))

#===================================================
#---------------------------------------------------    Widgets inside radiobuttonsframe

defaultpathradiobutton=ttk.Radiobutton(radiobuttonsframe, text='Default Path', variable=load_radiobutton, value='default')
defaultpathradiobutton.pack(side=LEFT,padx=(20,7),pady=2)
custompathradiobutton=ttk.Radiobutton(radiobuttonsframe, text='Custom Path', variable=load_radiobutton, value='custom')
custompathradiobutton.pack(side=RIGHT,padx=(5,20),pady=2)

#===================================================
#---------------------------------------------------    Widgets inside loadpathentry

loadpathentry=ttk.Entry(loadpathentry, textvariable=load_entry_path, state='readonly', width=30)
loadpathentry.pack(padx=(0,15))

#===================================================
#---------------------------------------------------    Bindings

mainentry.focus()
mainentry.bind('<Return>', agregar)
outmenu.bind('<Double-1>', removeitem)
defaultradiobutton.bind('<Button-1>', radioevent1)
customradiobutton.bind('<Button-1>', radioevent2)
menu.bind('<Double-1>', loadlistfile)
defaultpathradiobutton.bind('<Button-1>', defaultpath)
custompathradiobutton.bind('<Button-1>', custompath)

#===================================================
#---------------------------------------------------    Functions to run on start

load_radiobutton.set('default')
defaultpath()
center(root)

#===================================================
#---------------------------------------------------    End Program

root.mainloop()