#integração do banco de dados com python

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#criar janela

jan = Tk()
jan.title("DP Systems - Acess Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)

#transparente
#jan.attributes("-alpha", 0.9)

#imagens
logo=PhotoImage(file="icons/logo.png")

#dividir a janela
LeftFrame = Frame(jan, width=200, height=300, bg="#008Fff", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="#008Fff", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="#008Fff")
LogoLabel.place(x=50, y=100)

#parte do usuario
UserLabel=Label(RightFrame, text ="Username:", font=('Century Gothic', 20), bg="#008Fff", fg="white")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150,y=113)

#parte da senha
PassLabel = Label(RightFrame, text="Passoword:", font = ('Century Gothic', 20), bg="#008fff", fg="white")
PassLabel.place(x=5, y=150)

PassEntry = ttk.Entry(RightFrame, width=30)
PassEntry.place(x=160, y = 163)

#botoes
LoginButton = ttk.Button(RightFrame, text ="Login", width=25)
LoginButton.place(x=95, y= 210)

RegisterButton = ttk.Button(RightFrame, text="Register", width=20)
RegisterButton.place(x=110, y= 250)


jan.mainloop()
