
# https://www.geeksforgeeks.org/python-tkinter-tutorial/

from tkinter import *
from tkinter import font
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfile
    
win = Tk()
win.geometry("600x500+5+5")
win.title('Sumar')


lb_titulo=Label(win, text='Calculadora',font=25)
lbA=Label(win, text='A=') 
lbB=Label(win, text='B=')
tbA=Entry()
tbB=Entry()
lb_titulo.place(x= 25, y=50)
lbA.place(x=50, y=100)
tbA.place(x=100, y=100)
lbB.place(x=50, y=200)
tbB.place(x=100, y=200)


#Datos de salida 
lbC=Label(win, text='C= ')
tbC=Entry()
lbC.place(x=50, y=400)
tbC.place(x=100, y=400)
        
#definición del botón 
boton=Button(win, text='sumar', command= lambda:sumar())
boton.place(x=100, y=300)

        
#definición del spinbotón 
spinbox=Spinbox(win,from_=0,to=100)
spinbox.place(x=400, y=100)


#definición del combo box 
combo = ttk.Combobox(win, width = 27)
# Adding combobox drop down list
combo['values'] = (' 1', 
                          ' 2',
                          ' 3',
                          ' 4')
combo.grid(column = 1, row = 5)
combo.current()
combo.place(x=400, y=200)


#definición de un botón de apertura de datos
btn = Button(win, text ='Open', command = lambda:open_file())
btn.place(x=400, y=300)
 
# This function will be used to open
# file in read mode and only Python files
def open_file():
    file = askopenfile(mode ='r', filetypes =[('Python Files', '*.py')])
    if file is not None:
        content = file.read()
        print(content)
    

def sumar():
    tbC.delete(0, 'end')
    A=float(tbA.get())
    B=float(tbB.get())
 
    d=float(combo.get())

    C=A+B+d
    tbC.insert(END, str(C))

mainloop()

