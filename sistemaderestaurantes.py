import os

restaurantes = []


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_logo():
    print("""
--------------------------------
       SISTEMA DE RESTAURANTES
--------------------------------
""")


def mostrar_menu():
    print("1 - Adicionar restaurante")
    print("2 - Listar restaurantes")
    print("3 - Alterar status")
    print("4 - Buscar restaurante")
    print("5 - Sair\n")


def pausar():
    input("\nPressione ENTER para continuar...")


def titulo(texto):
    limpar_tela()
    print("-" * 30)
    print(texto)
    print("-" * 30)
    print()


def adicionar_restaurante():
    titulo("Cadastro de Restaurante")

    nome = input("Nome do restaurante: ").strip()

    if nome == "":
        print("O nome não pode ficar vazio.")
        pausar()
        return

    categoria = input("Categoria: ").strip()

    restaurante = {
        "nome": nome,
        "categoria": categoria,
        "ativo": False
    }

    restaurantes.append(restaurante)

    print(f"\nRestaurante '{nome}' cadastrado com sucesso!")
    pausar()


def listar_restaurantes():
    titulo("Lista de Restaurantes")

    if len(restaurantes) == 0:
        print("Nenhum restaurante cadastrado.")
        pausar()
        return

    print(f"{'Nome':<20} | {'Categoria':<15} | Status")
    print("-" * 50)

    for restaurante in restaurantes:

        status = "Ativo" if restaurante["ativo"] else "Inativo"

        print(
            f"{restaurante['nome']:<20} | "
            f"{restaurante['categoria']:<15} | "
            f"{status}"
        )

    pausar()


def alterar_status():
    titulo("Alterar Status")

    nome = input("Digite o nome do restaurante: ").strip()

    encontrado = False

    for restaurante in restaurantes:

        if restaurante["nome"].lower() == nome.lower():

            restaurante["ativo"] = not restaurante["ativo"]

            status = "ativado" if restaurante["ativo"] else "desativado"

            print(f"\nRestaurante {status} com sucesso!")

            encontrado = True
            break

    if not encontrado:
        print("\nRestaurante não encontrado.")

    pausar()


def buscar_restaurante():
    titulo("Buscar Restaurante")

    nome = input("Digite o nome do restaurante: ").strip()

    for restaurante in restaurantes:

        if restaurante["nome"].lower() == nome.lower():

            status = "Ativo" if restaurante["ativo"] else "Inativo"

            print("\nRestaurante encontrado:\n")

            print(f"Nome: {restaurante['nome']}")
            print(f"Categoria: {restaurante['categoria']}")
            print(f"Status: {status}")

            pausar()
            return

    print("\nNenhum restaurante encontrado.")
    pausar()


def finalizar():
    titulo("Sistema encerrado")


def opcao_invalida():
    print("\nOpção inválida.")
    pausar()


def executar_sistema():

    while True:

        limpar_tela()

        mostrar_logo()
        mostrar_menu()

        try:

            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                adicionar_restaurante()

            elif opcao == 2:
                listar_restaurantes()

            elif opcao == 3:
                alterar_status()

            elif opcao == 4:
                buscar_restaurante()

            elif opcao == 5:
                finalizar()
                break

            else:
                opcao_invalida()

        except ValueError:
            print("\nDigite apenas números.")
            pausar()


if __name__ == "__main__":
    executar_sistema()