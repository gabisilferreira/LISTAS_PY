elementos =["banana", "maça", "pera", "uva"]

elemento= elementos[::-1]
print(elemento)

#Crie uma lista com 4 frutas: "maçã", "banana", "laranja" e "uva". 
# Mostre na tela o segundo e o último elemento da lista.

frutas = ["maçã", "banana", "laranja", "uva"]
print("Primeiro elemento:",frutas[1], ", último elemento:", frutas[-1])

#Crie um programa que peça ao usuário para digitar 3 números e os armazene em uma lista. 
# Depois, mostre essa lista na tela.
itens=[]

for i in range(3):
    item= input("Digite um número \n")
    itens.append(item)

print(itens)

#Crie uma lista com os números 10, 20 e 30. Substitua o número do meio (20) 
# pelo número 25 e mostre a lista atualizada

numeros = [10,20,30]
numeros[1]=25
print(numeros)

#Crie uma lista vazia e peça ao usuário para adicionar 2 elementos usando o método append(). 

lista =[]

for j in range(2):
    adc = input("Adicione um item a lista \n")
    lista.append(adc)

print(lista)