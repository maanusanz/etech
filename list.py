# criando uma lista a partir de uma sequência

lista_numeros = list([1,2,3,4,5])
print(lista_numeros)


lista_caracteres = list("python")
print(lista_caracteres)

#append() adiciona um elemento no final da lista
#supondo que 'numero' é [1,2,3,4,5]
numero = [1,2,3,4,5]
numero.append(6)
print(numero)

numero.remove(3)
print(numero)

ultimo = numero.pop()
print(ultimo)
print(numero)