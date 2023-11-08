import os

message = []

name = input("Seu Nome: ")

while True:
    
    os.system('cls')#limpando terminal

    if len(message) > 0:
        for m in message:
            print(m['nome'], "-", m['texto'])


            print("__________")

            #obtendo texto
            