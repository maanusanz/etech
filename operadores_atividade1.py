
media = float(input("Digite a sua media: "))
frequencia = float(input("Digite a sua frequencia: "))

if  frequencia >= 75 and media >= 7:
    print("Aprovado")
elif frequencia < 75 or (frequencia >= 75 and media < 5):
    print("Reprovado")
elif frequencia >= 75 and 5 <= media <= 6.9:
    print("Recuperação")