import os

# import sys

# sys.plataform = diz o sistema operacional. pode ser usado para dar resposta de compatibilidade atribuindo a uma variavel e utilizando if, elif e else.

def start():
    nome = input("ola seja bem vindo como devo chama você?")
    resposta = input(
        f"como posso ajuda-lo?{os.linesep}[1] - Abrir calculadora {os.linesep}[2] - Abrir Bloco de Notas, {os.linesep}")
        # {os.linesep} = quebra linha importando a biblioteca OS
    while True:
        def processar_resposta(resposta, nome):
            if resposta == "1":
                os.startfile("Calculadora")
            elif resposta == "2":
                os.startfile("notepad.exe")
            else:
                print("Digite apenas 1 ou 2!")

        processar_resposta(resposta, nome)


if __name__ == "__main__":
    start()