def achar_elemento(elem, arr):
    try:
        indice = arr.index(elem)
        print(f"Achamos o nome: {elem} no índice {indice}")
    except ValueError:
        print(f"Não achamos o nome: {elem}")

# Lista de nomes
nomes = ['karol', 'miguel', 'jonny', 'kay']

# Loop para perguntar ao usuário o elemento que deseja encontrar
while True:
    elemento_desejado = input("Digite o nome que deseja encontrar (ou 'sair' para encerrar): ")

    if elemento_desejado.lower() == 'sair':
        print("Encerrando a busca.")
        break  # Sai do loop se o usuário digitar 'sair'
    
    # Chama a função achar_elemento com o elemento desejado
    achar_elemento(elemento_desejado, nomes)
