
#███╗░░░███╗░█████╗░██╗░░██╗  ░█████╗░░██████╗░███████╗███╗░░██╗██████╗░░█████╗░
#████╗░████║██╔══██╗╚██╗██╔╝  ██╔══██╗██╔════╝░██╔════╝████╗░██║██╔══██╗██╔══██╗
#██╔████╔██║███████║░╚███╔╝░  ███████║██║░░██╗░█████╗░░██╔██╗██║██║░░██║███████║
#██║╚██╔╝██║██╔══██║░██╔██╗░  ██╔══██║██║░░╚██╗██╔══╝░░██║╚████║██║░░██║██╔══██║
#██║░╚═╝░██║██║░░██║██╔╝╚██╗  ██║░░██║╚██████╔╝███████╗██║░╚███║██████╔╝██║░░██║
#╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝  ╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝
# Max Agenda
# Criador:  Rafael Guedes
# Github: https://github.com/guedes2142

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import Scrollbar as scroll
import webbrowser
from time import sleep
from tkcalendar import Calendar, DateEntry
from view import *
from view import atualizar_info
from view import delete_info

window = Tk()
window.geometry('1080x550')
window.resizable(width=False, height=False)
window.config(bg='white')
window.title('Max Agenda')
window.iconphoto(False, PhotoImage(file='agenda.png'))

# -------------------------------------------Logica---------------------------------------------------------#


def donation():

    messagebox.showinfo('Sua doação é importante!!', 'Pix: rafaguedesinveste@gmail.com\n'
                        'Sua contribuição é muito importante\n'
                        'Equipe MaxSoftware agradeçe!')

    donaSite = webbrowser.open('https://www.vakinha.com.br/3505393')


def openSpotify():

    spoty = webbrowser.open('https://open.spotify.com/')


def openGmail():

    gmail = webbrowser.open('https://gmail.com/')


def opengit():

    github = webbrowser.open('https://github.com')


def openEmail():

    messagebox.showinfo('Meu Email!!', 'rafaguedes.dev@gmail.com')


def display_info():  # TODO: mostar informaçoes no display two

    mostrar = showinfoInDisplayTwo()
    show = print(mostrar)
    displayTwo.get(show)
    ...

# Colors-----------------------------------------------------------------------------------------------------


cor1 = '#c7bc9d'  # cinza/amarelado
cor2 = '#59888f'  # azul/acizentado
cor3 = '#55cf90'  # verde
cor4 = '#f2e9dc'  # creme
cor5 = '#dcf2e7'  # verde muito claro
cor6 = '#bf3232'  # vermelho/red
cor7 = '#cfb929'  # amarelo/yellow

# Menu
# ----------------------------------------------------------------------------------------------------------
menubar = tk.Menu(window)

filemenu = tk.Menu(menubar)
filemenu.add_command(label="MaxMessageencription")
filemenu.add_command(label="MaxYoutubedownloader")
filemenu.add_command(label="MaxPasswordcreator")
filemenu.add_command(label="GitHub do projetos", command=opengit)
filemenu.add_command(label="Meu email", command=openEmail)

menubar.add_cascade(label="Outros app", menu=filemenu)

window.config(menu=menubar)

# criar frame nome

layoutNome = Frame(window, width=300, bg='white')
layoutNome.grid(row=0, column=0, sticky=NSEW)

# LabelNome
# ----------------------------------------------------------------------------------------------------------
labelNome = Label(layoutNome, width=33, height=2, text='Rafael Guedes',
                  font='Verdana 10 bold', bg='white', fg='black')
labelNome.grid(row=0, column=0, sticky=NSEW, pady=5)

# criar frame foto
# ----------------------------------------------------------------------------------------------------------
layoutPhoto = Frame(window, width=120, height=120, bg='white')
layoutPhoto.grid(row=1, column=0, sticky=NS)

# Photo
# ----------------------------------------------------------------------------------------------------------
logotipo = Image.open('png.png')
logotipo = logotipo.resize((120, 120), Image.ANTIALIAS)
logotipo = ImageTk.PhotoImage(logotipo)
app_logo = Label(layoutPhoto, width=120, image=logotipo,
                 compound=LEFT, relief='flat', anchor='center', bg='white')
app_logo.grid(row=0, column=0, sticky=NSEW)

# layout botoes
# ----------------------------------------------------------------------------------------------------------
opiton = Frame(window, background='white')
opiton.grid(row=2, column=0, sticky=NSEW)

global tree
# função  inserir


def insertSubject():

    nome = entryName.get()
    telefone = entryPhone.get()
    endereco = entryEnd.get()
    data = entrydata.get()
    notas = entryObs.get('1.0', 'end-1c')

    lista = [nome, telefone, endereco, data, notas]

    if nome == '':
        messagebox.ERROR('Erro', 'Nome não pode estar vazio')
    else:
        insertInfomations(lista)
        messagebox.showinfo('Sucesso', 'Novo contato salvo com sucesso')

        entryName.delete(0, 'end')
        entryPhone.delete(0, 'end')
        entryEnd.delete(0, 'end')
        entrydata.delete(0, 'end')
        entryObs.delete('1.0', END)

    for widget in displayOne.winfo_children():
        widget.destroy()

        showInfo()

# atualizar


def updateInformation():

    global tree

    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = tree_lista[0]

        entryName.delete(0, 'end')
        entryPhone.delete(0, 'end')
        entryEnd.delete(0, 'end')
        entrydata.delete(0, 'end')
        entryObs.delete('1.0', END)

        entryName.insert(0, tree_lista[1])
        entryPhone.insert(0, tree_lista[2])
        entryEnd.insert(0, tree_lista[3])
        entrydata.insert(0, tree_lista[4])
        entryObs.insert('1.0', tree_lista[5])

        def update():

            nome = entryName.get()
            telefone = entryPhone.get()
            endereco = entryEnd.get()
            data = entrydata.get()
            notas = entryObs.get('1.0', 'end-1c')

            lista = [nome, telefone, endereco, data, notas, valor_id]

            if nome == '':
                messagebox.showerro('Erro', 'Nome não pode estar vazio')
            else:
                atualizar_info(lista)
                messagebox.showinfo(
                    'Sucesso', 'Os dados foram atualizados com sucesso')

                entryName.delete(0, 'end')
                entryPhone.delete(0, 'end')
                entryEnd.delete(0, 'end')
                entrydata.delete(0, 'end')
                entryObs.delete('1.0', END)

            for widget in displayOne.winfo_children():
                widget.destroy()

            showInfo()

        btnConfirme = Button(opiton, command=update, text='Confirma', width=7,
                             height=1, font='Verdana 7 bold', bg=cor3, fg='black', relief=GROOVE)
        btnConfirme.place(x=255, y=9)

    except IndexError:
        messagebox.showerror('Erro', 'Selecionar os dados na tabela')


def deletar():

    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = [tree_lista[0]]

        delete_info(valor_id)
        messagebox.showinfo('Sucesso', 'O contato foi deletado com sucesso')

        for widget in displayOne.winfo_children():
            widget.destroy()

        showInfo()

    except IndexError:
        messagebox.showerror('Erro', 'Selecionar um contato para deletar')


# Layout entries
# ----------------------------------------------------------------------------------------------------------
frameEntry = Frame(window, width=300,  bg='white')
frameEntry.grid(row=3, column=0, sticky=NSEW, pady=5)

# Entries
# ----------------------------------------------------------------------------------------------------------
inputName = Label(frameEntry, width=10, height=2,
                  text='Nome:', font='Verdana 10 bold', bg='white')
inputName.grid(row=0, column=0, sticky=NSEW, padx=5)
entryName = Entry(frameEntry, width=20, font='Verdana 10 ', relief=SOLID)
entryName.grid(row=0, column=1)

inputPhone = Label(frameEntry, width=10, height=2,
                   text='Contato:', font='Verdana 10 bold', bg='white')
inputPhone.grid(row=1, column=0, sticky=NSEW, padx=5)
entryPhone = Entry(frameEntry, width=20,
                   font='Verdana 10 italic', relief=SOLID)
entryPhone.grid(row=1, column=1)

inputEnd = Label(frameEntry, width=10, height=2,
                 text='Endereço:', font='Verdana 10 bold', bg='white')
inputEnd.grid(row=2, column=0, sticky=NSEW, padx=5)
entryEnd = Entry(frameEntry, width=20, font='Verdana 10 italic', relief=SOLID)
entryEnd.grid(row=2, column=1)

inputObs = Label(frameEntry, width=10, height=2, text='Notas:',
                 font='Verdana 10 bold', bg='white')
inputObs.grid(row=4, column=0, sticky=NSEW, padx=5)
entryObs = Text(frameEntry, width=20,  height=5,
                font='Verdana 10 italic', relief=SOLID)
entryObs.grid(row=4, column=1)

inputdata = Label(frameEntry, width=10, height=2, text='Data:',
                  font='Verdana 10 bold', bg='white', fg='black')
inputdata.grid(row=3, column=0, sticky=NSEW, padx=5)
entrydata = DateEntry(frameEntry, width=12, height=1,
                      font='Verdana 10 italic', bg='dar kblue', fg='white', relief=SOLID,)
entrydata.grid(row=3, column=1, sticky=NSEW)

# Layout display 01
# ----------------------------------------------------------------------------------------------------------
displayOne = Frame(window, width=580, height=300, bg=cor4, relief=SUNKEN)
displayOne.place(x=310, y=5)

# Layout display 02
# ----------------------------------------------------------------------------------------------------------
displayTwo = Frame(window, width=580, height=258, bg=cor5, relief=SUNKEN)
displayTwo.place(x=310, y=260)

displayTree = Frame(window, width=169, height=518, bg=cor6, relief=SUNKEN)
displayTree.place(x=900, y=5)

# ----------------------------------------------------------------------------------------------------------
btnDonation = Button(frameEntry, width=8, command=donation, height=2, text='CONTRIBUA',
                     font='Verdana 8 bold', bg=cor7, fg='black', relief=FLAT, overrelief='solid')
btnDonation.grid(row=5, column=0, pady=5, padx=5, sticky=NSEW)
btnSpotify = Button(frameEntry, width=10, command=openSpotify, height=2, text='Abrir Spotify',
                    font='Verdana 8 bold', bg=cor3, fg='black', relief=FLAT, overrelief='solid')
btnSpotify.grid(row=5, column=1, pady=5, padx=5, sticky=W)
btnGmail = Button(frameEntry, width=10, command=openGmail, height=2, text='Abrir Gmail',
                  font='Verdana 8 bold', bg=cor6, fg='black', relief=FLAT, overrelief='solid')
btnGmail.place(x=210, y=241)

# Botoes
# ----------------------------------------------------------------------------------------------------------
btnAdd = Button(opiton, text='Adiconar', command=insertSubject, width=8,
                height=1, font='Verdana 10 bold', bg=cor4, fg='black', relief=FLAT)
btnAdd.grid(row=0, column=0, pady=2, padx=45)

btnEdit = Button(opiton, command=updateInformation, text='Editar', width=8,
                 height=1, font='Verdana 10 bold', bg=cor4, fg='black', relief=FLAT)
btnEdit.grid(row=0, column=1)

btnESave = Button(opiton, command=display_info, text='Ver Info:', width=8,
                  height=1, font='Verdana 10 bold', bg=cor3, fg='black', relief=FLAT)
btnESave.grid(row=1, column=0)

btnDel = Button(opiton, command=deletar, text='Deletar', width=8,
                height=1, font='Verdana 10 bold', bg=cor6, fg='black', relief=FLAT)
btnDel.grid(row=1, column=1)

# ----------------------------------------------------------------------------------------------------------
 
def showInfo():

    global tree

    lista = show()

    tabela_header = ['ID', 'nome', 'telefone', 'endereco', 'data', 'notas']
    dfLista = lista

    tree = ttk.Treeview(displayOne, selectmode='extended',
                        columns=tabela_header, show='headings')
    vsb = ttk.Scrollbar(displayOne, orient='vertical', command=tree.yview)
    hsb = ttk.Scrollbar(displayOne, orient='horizontal', command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky=NSEW)
    vsb.grid(column=1, row=0, sticky=NS)
    hsb.grid(column=0, row=1, sticky=NS)
    displayOne.grid_rowconfigure(0, weight=12)

    hd = ['nw', 'nw', 'nw', 'nw', 'nw', 'nw']
    h = [30, 150, 90, 130, 65, 95]
    n = 0

    for col in tabela_header:
        tree.heading(col, tex=col.title(), anchor=CENTER)
        tree.column(col, width=h[n], anchor=hd[n])

        n += 1

    for item in dfLista:
        tree.insert('', 'end', values=item)

showInfo()

window.mainloop()
