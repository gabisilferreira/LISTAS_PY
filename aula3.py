#lista de listas e seus índices

salas =[
    ['Maria', 'Helena',],
    ['Elaine',],
    ['Luiz', 'Joaquim', 'Eduarda', (0,10,20,30,40)]
]

print(salas[0][1]) #acessa o item dentro da lista
print(salas[2][2])
print(salas[2][3][2])


salas_aula=[
     ['Maria', 'Helena',],
    ['Elaine',],
    ['Luiz', 'Joaquim', 'Eduarda',]
]

for sala in salas_aula:
    print(f"A sala é {sala}")
    for aluno in sala:
        print(aluno)