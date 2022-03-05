#integração do banco de dados com python

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import font

#criar janela

jan = Tk()
jan.title("DP Systems - Acess Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.iconbitmap(default="icons/LogoIcon.ico")

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
UserLabel=Label(RightFrame, text ="Username", font=('Century Gothic', 20), bg="#008Fff", fg="white")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=35)
UserEntry.place(x=160,y=113)



#parte da senha
PassLabel = Label(RightFrame, text="Passoword", font = ('Century Gothic', 20), bg="#008fff", fg="white")
PassLabel.place(x=5, y=150)

PassEntry = ttk.Entry(RightFrame, width=35, show="•")
PassEntry.place(x=160, y = 163)

#botoes
LoginButton = ttk.Button(RightFrame, text ="Login", width=25)
LoginButton.place(x=95, y= 210)

def Register():
    #removendo botoes
    LoginButton.place(x="601")
    RegisterButton.place(x="601")

    #inserir os botoes de cadastro
    NomeLabel = Label(RightFrame, text = "Nome", font = ('Century Gothic', 20), bg="#008fff", fg="white")
    NomeLabel.place(x=5, y =5)

    NomeEntry = ttk.Entry(RightFrame, width="45")
    NomeEntry.place(x=100, y=18)

    EmailLabel = Label(RightFrame, text="Email", font=('Century Gothic', 20), bg="#008fff", fg="white")
    EmailLabel.place(x=5, y = 50)

    EmailEntry = ttk.Entry(RightFrame, width="45")
    EmailEntry.place (x = 100, y = 62)
    #botao back to login
    def BackToLogin():
        NomeLabel.place(x=601)
        NomeEntry.place(x=601)
        EmailEntry.place(x=601)
        EmailLabel.place(x=601)
        RegisterButton.place(x=601)
        Back.place(x=601)
        Register.place(x=601)

        #trazendo de volta os botoes
        LoginButton.place(x=95, y= 210)
        RegisterButton.place(x=110, y= 250)

    #botoes
    Register = ttk.Button(RightFrame, text="Register", width=25)
    Register.place(x=95, y= 210)

    Back = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin)
    Back.place(x=110, y= 250)


    

RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=Register)
RegisterButton.place(x=110, y= 250)



jan.mainloop()
