# ---------------------- Les modules utilisés
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from PIL import Image, ImageTk
import pickle
# ---------------------- Les fonctions qui sont utilisées par le programme


def AddFunc(txt, index=END):
    """
    Cette fonction est responsable de créer une nouvelle tâche.
    """
    # Déclaration d'une variable global d'une nouvelle fenêtre
    global add  # var global / defint comme variable globala l interieur d une fonction/permet de manipuler la variable add a l interieur et/ou a l'exterieur d'une fonction
    add = Tk()  # creer la fenetre ou on va saisir la tache
    add.iconbitmap('img/icon.ico')  # creer l'icone de la fenetre
    add.title('Add Note')
    add.geometry(f'{800}x{600}')
    # ne permet pas leredimentionnement de la fenetre
    add.resizable(width=False, height=False)
    add.config(background='#FFF')
    # déclaration d'une variable de la zone de texte
    global Write
    global Writedate
    #ZONNE DE SAISIE 1
    Write = Entry(add,font=(ft,16,''))
    Write.place(x=5,y=80, width=380, height=30)  
    #ZONNE DE SAISIE 2
    Writedate = Entry(add, font=(ft,16,''))
    Writedate.place(x=5,y=180, width=380, height=30)  

    iFinish = ImageTk.PhotoImage(Image.open('img/finished1.png'), master=add)
    bFinish = Button(add, width=40, height=40, image=iFinish,
                     bd=0, highlightthickness=0, command=lambda: GetText())
    bFinish.place(x=750, y=550)
    #label tache
    lab_taches = Label(add, text='TACHES  :')
    lab_taches.place(x=5,y=50)


    #label date
    lab_date = Label(add, text='date :')
    lab_date.place(x=5,y=150)

    add.mainloop()

def GetText():
    """
    Cette fonction permet de mettre à jour le compteur lors d'une nouvelle tâche
    """
    text = Write.get()
    date_t=  Writedate.get()
    mes_taches.insert(END, text + "la dabdjrfjzhhjzejhe est "+  date_t)
    add.destroy()


# ---------------------- Importantes variables
# Ici on déclare 4 variables (En utilisant une ligne) la largeur et la longeur, la couleur blanche et le nom de la police du texte
w, h, b, ft = 994, 700, '#FFF', 'Century Gothic'
# ---------------------- Paramètres de la fenêtre
app = Tk()
# L'icone
app.iconbitmap('img/icon.ico')
# Le titre
app.title('TO DO LIST')
# La taille (ou la résolution)
app.geometry(f'{w}x{h}')
# la désactivation de changement de la résolution de fenêtre
app.resizable(width=False, height=False)
# la couleur de l'arrière plan (background)
app.config(background=b)
# ---------------------- Paramètres des widgets
# Déclaration d'une variable *global*
global mes_taches
# Déclaration de plusieurs widgets, ex: des canvas, des barres de défilement, des listes et des textes
TSCanv = Canvas(app, bg='#8aff70')
mes_taches = Listbox(TSCanv, bd=2, relief='solid', width=38, height=19, font=(
    ft, 16, ''), highlightcolor='#0f0', selectmode=BROWSE)
labeltS = Label(app, text='TACHES PLANIFIEES :', bg=b,
                fg='#F00', font=(ft, 25, 'bold'))
# Positionnement des widgets
mes_taches.pack()  # positionner la lisbox dans tout canvas
TSCanv.place(x=250, y=70)  # positionner le canevas
labeltS.place(x=250, y=10)

# ---------------------- les raccourcis claviers
# ---------------------- Les images des bouttons
IAdd = ImageTk.PhotoImage(Image.open('img/Add.png'))
IDAdd = ImageTk.PhotoImage(Image.open('img/AddD.png'))
iAdd = ImageTk.PhotoImage(Image.open('img/plus.png'))

# ---------------------- Les bouttons
# Déclaration de 4 variables (dans une ligne) des tailles des grands et petits bouttons
Wd, Hg, wd, hg = 165, 56, 40, 40
BAdd = Button(app, text='Add', width=Wd, height=Hg, image=IAdd,
              command=lambda: AddFunc(''), bd=0, highlightthickness=0)
bAdd = Button(app, text='+', width=wd, height=hg, image=iAdd,
              command=lambda: AddFunc(''), bd=0, highlightthickness=0)
# Positionnement des boutons
bAdd.place(x=650, y=12)
BAdd.place(x=10, y=580)
# ---------------------- Ouverture du programme
app.mainloop()

