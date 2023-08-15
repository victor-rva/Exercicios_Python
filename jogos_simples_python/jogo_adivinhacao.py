secreto = "python"
digitados = []
chances = 5

while True:
    if chances <= 0:
        print("Você perdeu!!")
        break

    letra = input("Digite uma letra: ")

    if len(letra) > 1:
        print("Isso não vale, digite uma letra.")
        continue

    digitados.append(letra)

    if letra in secreto:
        print(f"UHUUULL, a letra {letra} existe na palavra secreta.")
    else:
        print(f"A letra {letra} não existe na palavra secreta :/ ")
        digitados.pop()

    secreto_temporario = ""
    for letra_secreta in secreto:
        if letra_secreta in digitados:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += "*"

    if secreto_temporario == secreto:
        print(f"Que legal, você GANHOU!!! A palavra era {secreto_temporario}.")
        break
    else:
        print(f"A palavra secreta está assim: {secreto_temporario}")

    if letra not in secreto:
        chances -= 1
    print(f"Você ainda tem {chances} chances.")
    print()
