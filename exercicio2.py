#Crie uma lista com os números de 1 a 10. Peça ao usuário um número e remova-o da lista. 
# Mostre a lista atualizada. 
# Caso o número não esteja na lista, exiba uma mensagem dizendo que ele não foi encontrado.

# Lista inicial
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Solicitando o número do usuário
item = input("Digite o número que deseja retirar da lista: \n")

# Convertendo o item para inteiro
if item.isdigit():  # Verifica se o input é um número
    item = int(item)  # Converte para inteiro

    # Verifica se o número está na lista
    if item in lista:
        lista.remove(item)
        print("O item removido foi:", item)
        print("A lista atualizada é:", lista)
    else:
        print("Item não pertence à lista.")
else:
    print("Você não digitou um número válido.")
