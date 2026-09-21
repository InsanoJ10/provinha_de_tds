def calcular_media(notas):
    soma = 0
    for nota in notas:
        soma += nota # soma = soma + nota
    return soma / len(notas)
notas = [8,9,7]
media = calcular_media(notas)


if media >= 7:
    print("Aprovado")
else:
    print("Reprovou jumento")