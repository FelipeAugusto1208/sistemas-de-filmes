#Filmes perereca.com.br@gmail.com
nomes = []
generos = []
datas_de_lancamento = []
notas = []
avaliacoes = []





def cadastrar_films():
    nome = input("Digite o nome do films: ")
    genero = input("DIgite o genero do films: ")
    data_de_lancamento = int(input("Digite a data de lançamento do films: "))
    nota = int(input("Digite a nota do filme: "))

    nomes.append (nome)
    generos.append (genero)
    datas_de_lancamento.append (data_de_lancamento)
    notas.append (nota)

    if nota >= 8:
        avaliacoes.append("top")
    elif nota >= 6:
       avaliacoes.append("bom")
    elif nota >= 4:
        avaliacoes.append("ruim")
    else:
        avaliacoes.append("horroroso")

    print(f"Films {nome} cadastrado com sucesso!")

    

def listar_films():
    if len(nomes)==0:
        print("Nenhum films cadastrado ainda.")
    else:
        for i in range(len(nomes)):
            print(f"Titulo: {nomes[i]} - Genero: {generos[i]} - Data de lançamento: {datas_de_lancamento[i]} - Nota: {notas[i]} - avaliacoes: {avaliacoes[i]}")



def buscas_films():
    films_busca = input("Digite o nome do films que procura: ")
    for i in range(len(nomes)):
        if films_busca == nomes[i]:
            print(f"Titulo: {nomes[i]} - Genero: {generos[i]} - Data de lançamento: {datas_de_lancamento[i]} - Nota: {notas[i]} - avaliacoes: {avaliacoes[i]}")




def remover_films():
    films_remover = input("Digite o nome do films que deseja remover: ")
    for i in range(len(nomes)):
        if films_remover == nomes[i]:
            nomes.pop(i)
            notas.pop(i)
            generos.pop(i)
            datas_de_lancamento.pop(i)
            print("Films removido com sucesso.")



def estatisticas():
    if len(nomes)==0:
        print("Nenhum films cadastrado ainda.")
    else:        
        for i in range(len(nomes)):
            if notas[i] >= 8:
                print(f"Films com nota maior que 8: Nome: {nomes[i]}, Nota: {notas[i]}, Genero: {generos[i]}, Data de lançamento: {datas_de_lancamento[i]}, Avaliação: {avaliacoes[i]}")

        media = sum(notas) / len(notas)
        print(f"Media de notas: {notas}")

        mais_repetido = max(set(generos), key=generos.count)
        print(f"Gênero mais cadastrado: {mais_repetido}")

        quantidade = len(nomes)
        print(f"Quantidade de films: {quantidade}")


def menu():
    while True:
        print(f"menu")
        print("1 - Cadastrar films")
        print("2 - Listar films")
        print("3 - Buscar films")
        print("4 - Remover films")
        print("5 - Estatisticas")
        print("6 - Sair")
        opcao = input("Escolha uma das opções: ")

        if opcao == "1":
            cadastrar_films()
        elif opcao == "2":
            listar_films()
        elif opcao == "3":
            buscas_films()
        elif opcao == "4":
            remover_films()
        elif opcao == "5":
            estatisticas()
        elif opcao == "6":
            print("Encerrando o programa...")
            break
        else:
            print("Opção invalida.")


menu()