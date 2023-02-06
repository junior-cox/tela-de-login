import tkinter as tk
from tkinter import ttk
from tkinter import Menu

def sobre():
    tela2=tk.Tk()
    tela2.geometry('200x200')
    tela2.title('sobre')
    tela2.iconbitmap('vazil.ico')
    tela2.config(bg='blue')

    #esse cria as abras
    abas=ttk.Notebook(tela2,width=300,height=400)
    abas.pack()
    #esse cria as caixas da abas
    caixa=ttk.Frame(abas,width=300,height=200)
    caixa2=ttk.Frame(abas,width=300,height=200)
    #essa parte fecha as caixas
    caixa.pack(expand=True)
    caixa2.pack(expand=True)
    #esse defini o nome das caixas
    abas.add(caixa,text='contato')
    abas.add(caixa2,text='criador')
    #por dentro da caixa
    ema=tk.Label(caixa,text='critinacox@gmail.com').pack()
    tel=tk.Label(caixa,text='5533998558139').pack()
    nom=tk.Label(caixa2,text='junior h oliveira').pack()

tela=tk.Tk()
tela.title('faça login')
tela.geometry('450x600')
tela.iconbitmap('vazil.ico')
tela.config(bg='blue')
#imagen de fundo
ima=tk.PhotoImage(file="fundo.png")
imaf=ttk.Label(image=ima)
imaf.pack()
#primeiro  texto
texto=tk.Label(tela,text='gigite seu email',font=("Helvetica",15))
texto.place(x=0,y=250)
#campo de texto
user=tk.StringVar()
usertext=ttk.Entry(tela,textvariable=user,font=("Helvetica",14))
usertext.place(x=0,y=300)
#texto 2
texto1=tk.Label(tela,text='digite a senha',font=('Hvelvetica',15))
texto1.place(x=0,y=350)
#outra caixar de texto
sen=tk.StringVar()
sentext=ttk.Entry(tela,textvariable=sen,font=('fonte',14),show='*')
sentext.place(x=0,y=400)
#um botao sinplis
bu=tk.Button(tela,text='entra',font=('arial',13))
bu.place(x=0,y=500,width=60,height=30)
#icone de cadeado 
cadeado=tk.PhotoImage(file='cadeado.png')
cadeado1=tk.Label(image=cadeado,width=100,height=100)
cadeado1.place(x=4,y=5)
#info
info=tk.Button(tela,text='sobre',command=sobre)
info['relief']='flat'
info.place(x=0,y=580)

tela.mainloop()