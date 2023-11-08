import os

mensagem = []

nome = input("Seu Nome: ")

while True:
    
    #limpando terminal
    os.system('cls')

    if len(mensagem) > 0:
        for m in mensagem:
            print(m['nome'], "-", m['texto'])


    print("__________________")

            #obtendo texto
    texto = input("Digite a mensagem: ")
    if texto == "fim":
        print("Chat encerrado.")
        break

    mensagem.append({
     "nome": nome,
     "texto": texto
    })