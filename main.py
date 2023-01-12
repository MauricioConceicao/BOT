from tkinter import *


#nome = input("Me diga seu nome:")


#__vvvvvvvvvvv_configuraçao de uma janela_vvvvvvvv_____
janela = Tk()
janela.title("mauricio")
janela.geometry("400x400")
Label(janela, text="nome", background="#dde", foreground="#009", anchor=W).place(x=10, y=10, width=100, height=20)
#  S = sul , N = norte , E = leste , W = oeste
#  NE = nordeste , SE = sudeste , SO = sudoeste , NO = noreoeste
texto = Label(janela, text="bem-vindo")
vnome = Entry(janela)
vnome.place(x=10, y=365, width=375, height=20)
#largura = width/x
#altura = height/y



janela.mainloop()
#____________^^^^^^^^configuraçao de uma janela^^^^^^^^^^^^____________