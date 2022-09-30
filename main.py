from tkinter import *
from tkinter import ttk
from cores import *

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=cor1_preta)

# CRIANDO FRAMES
frame_tela = Frame(janela, width=235, height=50, bg=cor3_azul)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

#CRIANDO LABEL
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor3_azul, fg=cor2_branca)
app_label.place(x=0, y=0) 


button_1 = Button(frame_corpo, command= lambda:apagar_valores(), text="C", width=11, height=2, bg=cor4_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_1.place(x=0, y=0 )

button_2 = Button(frame_corpo, command= lambda:pegar_valores('%'), text="%", width=5, height=2, bg=cor4_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_2.place(x=118, y=0 )

button_3 = Button(frame_corpo, command= lambda:pegar_valores('/'), text="/", width=5, height=2, bg=cor5_laranja, fg=cor2_branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_3.place(x=177, y=0 )

# SEGUNDA LINHA
button_4 = Button(frame_corpo, command= lambda:pegar_valores('7'), text="7", width=5, height=2, bg=cor4_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_4.place(x=0, y=52 )
button_5 = Button(frame_corpo, command= lambda:pegar_valores('8'), text="8", width=5, height=2, bg=cor4_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_5.place(x=59, y=52 )
button_6 = Button(frame_corpo, command= lambda:pegar_valores('9'), text="9", width=5, height=2, bg=cor4_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_6.place(x=118, y=52 )

button_7 = Button(frame_corpo, command= lambda:pegar_valores('*'), text="*", width=5, height=2, bg=cor5_laranja, fg=cor2_branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_7.place(x=177, y=52)

# TERCEIRA LINHA
button_8 = Button(frame_corpo, command= lambda:pegar_valores('4'), text="4", width=5, height=2, bg=cor4_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_8.place(x=0, y=104 )
button_9 = Button(frame_corpo, command= lambda:pegar_valores('5'), text="5", width=5, height=2, bg=cor4_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_9.place(x=59, y=104 )
button_10 = Button(frame_corpo, command= lambda:pegar_valores('6'), text="6", width=5, height=2, bg=cor4_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_10.place(x=118, y=104 )

button_11 = Button(frame_corpo, command= lambda:pegar_valores('-'), text="-", width=5, height=2, bg=cor5_laranja, fg=cor2_branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_11.place(x=177, y=104)

# QUARTA LINHA
button_12 = Button(frame_corpo, command= lambda:pegar_valores('1'), text="1", width=5, height=2, bg=cor4_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_12.place(x=0, y=156 )
button_13 = Button(frame_corpo, command= lambda:pegar_valores('2'), text="2", width=5, height=2, bg=cor4_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_13.place(x=59, y=156 )
button_14 = Button(frame_corpo, command= lambda:pegar_valores('3'), text="3", width=5, height=2, bg=cor4_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_14.place(x=118, y=156 )

button_15 = Button(frame_corpo, command= lambda:pegar_valores('+'), text="+", width=5, height=2, bg=cor5_laranja, fg=cor2_branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_15.place(x=177, y=156)

# QUINTA LINHA
button_16 = Button(frame_corpo, command= lambda:pegar_valores('0'), text="0", width=11, height=2, bg=cor4_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_16.place(x=0, y=208 )
button_17 = Button(frame_corpo, command= lambda:pegar_valores('.'), text=".", width=5, height=2, bg=cor4_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_17.place(x=118, y=208 )

button_18 = Button(frame_corpo, command= lambda:calcular_valores(), text="=", width=5, height=2, bg=cor5_laranja, fg=cor2_branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_18.place(x=177, y=208)


todos_valores = ''
# CRIANDO FUNÇÕES
def pegar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)

    # resultado =eval(todos_valores)
    # PASSANDO VALOR PARA A TELA 
    valor_texto.set(todos_valores)

def  calcular_valores():
    resultado = eval(todos_valores)
    valor_texto.set(resultado)

def apagar_valores():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")


janela.mainloop()
