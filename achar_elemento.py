def verificar_presenca(elemento, lista):
    encontrado = False
    for item in lista:
        if item == elemento:
            encontrado = True
    if not encontrado:
        print(f'O nome "{elemento}" não foi encontrado.')
    else:
        print(f'O nome "{elemento}" foi encontrado.')

ativo = True
nomes_lista = ['Karol', 'Miguel', 'Jhonathan', 'Kaylane']

while ativo:
    print("O que deseja fazer?\n"
          "1 - Adicionar um nome\n"
          "2 - Verificar a presença de um nome\n"
          "3 - Sair")

    opcao = int(input())

    if opcao == 1:
        novo_nome = input("Digite o nome: ").capitalize()
        nomes_lista.append(novo_nome)
        print(nomes_lista)

    elif opcao == 2:
        nome_procurado = input("Digite o nome desejado:").capitalize()
        verificar_presenca(nome_procurado, nomes_lista)

    elif opcao == 3:
        ativo = False

    elif 1 > opcao or opcao > 3:
        print("Opção inválida")

