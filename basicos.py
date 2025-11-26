inteiro = 10 #int (número inteiro)
decimal = 10.5 #float (número dcimal)
complexo = 3 + 4j #complex (número complexo)

print(inteiro, decimal, complexo)  #print retorna o valor no console(tela)
print(f"tipos: {type(inteiro)}, {type(decimal)}, {type(complexo)}")

#texto
texto = "Olá, mundo!" # str -> string/texto
print(texto)
print(f"tipos: {type(texto)}")


#booleanos

verdadeiro = True #bool (booleanos verdadeiros)
falso = False #bool (booleanos falso)

print(verdadeiro, falso)
print(f"tipos: {type(verdadeiro)}, {type(falso)}")

#coleções

lista = [1, 2, 3]  #list (lista mútavel)
tupla = (1, 2, 3)  #tupla (tupla imútavel)
dicionario = {"nome: manuella"} #dict (dicionário)
conjunto = {1, 2, 3}  #set (conjunto)
print(lista, conjunto, dicionario, tupla)
print(f"tipo: {type(lista)},{type(dicionario)},{type(tupla)}, {type(conjunto)}")