#Crie uma tupla contendo os números de 1 a 10. Exiba o terceiro e o penúltimo elemento da tupla.
tupla1 = (1,2,3,4,5,6,7,8,9,10,)
print(tupla1[2])
print(tupla1[-2])

#Crie uma tupla com os números: (2, 4, 6, 8, 2, 4, 2). Conte quantas vezes o número 2 aparece na tupla.
numeros= (2, 4, 6, 8, 2, 4, 2)
vezes = numeros.count(2)
print(vezes)

#Crie duas tuplas: uma contendo os números de 1 a 5 e outra com os números de 6 a 10. Concatene-as e exiba o resultado.
tupla2 = (1,2,3,4,5,)
tupla3= (6,7,8,9,10,)
nova_tupla = tupla2+tupla3
print(nova_tupla)

#Crie uma tupla com os números de 1 a 5. Converta a tupla para uma lista, adicione o número 6 ao final da lista e converta-a novamente para tupla.
tupla4 = (1,2,3,4,5,)
lista= list(tupla4)
lista.append(6)
tupla4 = tuple(lista)
print(tupla4)

#Peça ao usuário que insira 5 palavras e armazene-as em uma lista. 
# Depois: exiba as palavras em ordem alfabética e em ordem reversa.

palavras=[]
for i in range(5):
   num = input(f"Digite a {i+1}° palavra \n")
   palavras.append(num)

palavras_ordenadas = sorted(palavras) 
print("Palavras em ordem alfabética:", palavras_ordenadas)

# Exibindo as palavras em ordem reversa
palavras_reversa = list(reversed(palavras)) 
print("Palavras em ordem reversa:", palavras_reversa)