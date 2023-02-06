import tkinter as tk
from tkinter import ttk
import time

tela=tk.Tk()
tela.geometry('200x200')

def vai():
   b=ttk.Label(tela,text=valor1.get()).pack()
def vai2():
   time.sleep(3)
   tela1=tk.Tk()
   tela1.geometry('200x200')
   
bu=ttk.Button(tela,text='resutado',command=vai)
bu.pack()

valor1=tk.StringVar()
texto=ttk.Entry(tela,textvariable=valor1)
texto.focus()
texto.pack()

bu1=ttk.Button(tela,text='ado',command=vai2)
bu1.pack()

tela.mainloop()