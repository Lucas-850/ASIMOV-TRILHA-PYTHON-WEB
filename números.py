lista = [i for i in range(4,26) if i % 2 != 0]
print(lista)


lista2 = [i**2 for i in range(1,11)]
print(lista2)


lista3 = [i for i in range(1,31)if i % 3== 0]
print(lista3)

nomes = ["ana", "maria", "joão", "pedro"]
lista4 = [i.upper() for i in nomes]
print(lista4)

palavras = ["python", "java", "c", "php", "javascript"]
lista5 = [i for i in palavras if len(i) > 3]
print(lista5)
