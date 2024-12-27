print("Lista de compras")

# Lista inicializada vazia
lista = []

while True:  
    opcao = input("\nSelecione uma opção: \n" 
                  "[i]nserir [a]pagar  [l]istar [s]air \n").lower()

    if opcao == "i":
        item = input("Digite o elemento que deseja adicionar à lista: \n")
        lista.append(item)
        print(f"Item '{item}' adicionado com sucesso.")

    elif opcao == "a":
        apagar = input("Digite o item que deseja apagar: \n")
        if apagar in lista:
            lista.remove(apagar)
            print(f"Item '{apagar}' foi removido com sucesso.")
        else:
            print(f"O item '{apagar}' não está na lista.")

    elif opcao == "l":
        if lista:
            print("Itens na lista de compras:")
            for i, item in enumerate(lista):
                print(f"{i}. {item}")
        else:
            print("A lista está vazia.")

    elif opcao == "s":
        print("Programa encerrado. Até mais!")
        break

    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")
