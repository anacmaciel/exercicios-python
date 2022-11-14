def jogar():

    print("*****")
    print("Bem vindo ao jogo da forca")
    print("*****")
    palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    while(not acertou and not enforcou):
        chute = input("Qual a letra? ")
        chute = chute.strip()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    #print(chute)
                    print("Encontrei a letra {} na posição {}".format(letra, index))
                    letras_acertadas[index] = letra

                print(letras_acertadas)
                index += 1
        else:
            erros += 1
            if(erros == 6):
                break
            if("_" not in letras_acertadas):
                break
            print("Ops! Você errou, faltam {} tentativas".format(6-erros))
            #acertou = "_" not in letras_acertadas
            #enforcou = erros == 6

            print("Jogando...")
            print(letras_acertadas)

    if(acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")
    print("fim do jogo!")

if(__name__ == "__main__"):
    jogar()