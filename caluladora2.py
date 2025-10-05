from tkinter import *
from tkinter import ttk

from tkcalendar import Calendar, DateEntry

###importando dateutil####

from dateutil.relativedelta import relativedelta

###importando datetime####

from datetime import date


janela= Tk()
janela.title("Calculadora de idade")
janela.geometry('310x400')

#cores
cor1= "#646156"
cor2="#312D2D"
cor3= "#ffffff"    #branca
cor4="#ffcc58"   #laranja 



#criando frames

frame_cima=Frame(janela, width=310, height=140,pady=0,padx=0,relief=FLAT, bg=cor2)
frame_cima.grid(row=0, column=0)
frame_baixo=Frame(janela, width=310, height=300,pady=0,padx=0, relief=FLAT, bg=cor1)
frame_baixo.grid(row=1, column=0)

#criando labels

l_calculadora= Label(frame_cima, text= "CALCULADORA", width=25, height=1, padx=3, relief='flat',anchor="center", font=("Ivi", 15, "bold"), bg=cor2, fg=cor3)
l_calculadora.place(x=0, y=30)

l_idade= Label(frame_cima, text= "DE IDADE", width=11, height=1, padx=0, relief='flat',anchor="center", font=("Arial", 35, "bold"), bg=cor2, fg=cor4)
l_idade.place(x=0, y=70)

def calcular():
    inicial = cal_1.get_date()  # pega como datetime.date
    termino = cal_2.get_date()
    diferenca = relativedelta(termino, inicial)
    l_app_anos.config(text=diferenca.years)
    l_app_meses.config(text=diferenca.months)
    l_app_dias.config(text=diferenca.days)


####separando valores e atributos###

l_data_inicial= Label(frame_baixo, text= "Data inicial", height=1, padx=0, pady=0, relief='flat',anchor='nw', font=("Arial", 11, "bold"), bg=cor1, fg=cor3)
l_data_inicial.place(x=40, y=30)

l_data_nascimento= Label(frame_baixo, text= "Data de nascimento", height=1, padx=0, pady=0, relief='flat',anchor='nw', font=("Arial", 11, "bold"), bg=cor1, fg=cor3)
l_data_nascimento.place(x=40, y=70)

from datetime import date

cal_1=DateEntry(frame_baixo, width=13, bg='darkblue', fg=cor3, borderwidth=2, date_pattern='mm/dd/y', year=date.today().year)
cal_1.place(x=180, y=30)

cal_2=DateEntry(frame_baixo, width=13, bg='darkblue', fg=cor3, borderwidth=2, date_pattern='mm/dd/y', year=date.today().year)
cal_2.place(x=180, y=70)

l_app_anos= Label(frame_baixo, text= "27", height=1, padx=0, pady=0, relief='flat',anchor='center', font=("Ivy", 25, "bold"), bg=cor1, fg=cor3)
l_app_anos.place(x=60, y=135)

l_app_anos_nome= Label(frame_baixo, text= "anos", height=1, padx=0, pady=0, relief='flat',anchor='center', font=("Ivy", 11, "bold"), bg=cor1, fg=cor3)
l_app_anos_nome.place(x=60, y=175)

l_app_meses= Label(frame_baixo, text= "12", height=1, padx=0, pady=0, relief='flat',anchor='center', font=("Ivy", 25, "bold"), bg=cor1, fg=cor3)
l_app_meses.place(x=140, y=135)

l_app_meses_nome= Label(frame_baixo, text= "meses", height=1, padx=0, pady=0, relief='flat',anchor='center', font=("Ivy", 11, "bold"), bg=cor1, fg=cor3)
l_app_meses_nome.place(x=140, y=175)

l_app_dias= Label(frame_baixo, text= "27", height=1, padx=0, pady=0, relief='flat',anchor='center', font=("Ivy", 25, "bold"), bg=cor1, fg=cor3)
l_app_dias.place(x=220, y=135)

l_app_dias_nome= Label(frame_baixo, text= "dias", height=1, padx=0, pady=0, relief='flat',anchor='center', font=("Ivy", 11, "bold"), bg=cor1, fg=cor3)
l_app_dias_nome.place(x=220, y=175)

#criando botão calcular#

b_calcular= Button(frame_baixo, command=calcular, text= "Calcular", width=20, height=1, relief='raised',anchor='center', overrelief='ridge', font=("Ivy", 10, "bold"), bg=cor1, fg=cor3)
b_calcular.place(x=70, y=225)











janela.mainloop()

