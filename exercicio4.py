#Conjuntos

print("Crie um conjunto de números inteiros")
conjunto1 =[]

for i in range(5):
    item= input("Digite um número positivo \n")
    if item.isdigit():
        item = int(item)
        conjunto1.append(item)
    else:
        print("Você não digitou um número")

conjuntopri= set(conjunto1)

print("Conjunto sem duplicadas:", conjuntopri)
print("Quantidade de elementos únicos:", len(conjuntopri))


#Receba dois conjuntos de números inteiros do usuário e determine:
# Os números que aparecem em ambos os conjuntos (interseção).
# Os números que aparecem apenas no primeiro conjunto.
# Os números que aparecem apenas no segundo conjunto.


lista1 =[]

for i in range(4):
    elemento= input(f"Digite {i+1}° número da primeira lista:\n")
    try:
        elemento = int(elemento)
        lista1.append(elemento)
    except:
        print("Você não digitou um número")

conjunto3 = set(lista1)

lista2 = []
for i in range(4):
    elemento2= input(f"Digite {i+1}° número da segunda lista:\n")
    try:
        elemento2 = int(elemento2)
        lista2.append(elemento2)
    except:
        print("Você não digitou um número")

conjunto4= set(lista2)

print(f"A interseção do conjunto 1 e conjunto 2 é", conjunto3.intersection(conjunto4))
print("Items que tem no conjunto 1, mas não no conjunto 2", conjunto3.difference(conjunto4))
print("Items que tem no conjunto 2, mas não no conjunto 1", conjunto4.difference(conjunto3))



#Crie um programa que analise dois textos fornecidos pelo usuário e:
# Identifique as palavras únicas que aparecem em ambos os textos (interseção).
# Liste as palavras que aparecem em apenas um dos textos (diferença simétrica).

frase1 = input("Digite a primeira frase \n")
frase2 = input("Digite a segunda frase \n")

texto1 =  set(frase1.lower().split())
texto2 = set(frase2.lower().split())

print("A palavras iguais em ambos os textos são:", texto1.intersection(texto2))
print("Palavras que aparecem apenas na frase 1:", texto1.symmetric_difference(texto2))



