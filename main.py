import os

restaurantes = [
    {"nome": "Praça", "categoria": "Japonesa", "ativo": False},
    {"nome": "Pizza Suprema", "categoria": "Pizza", "ativo": True},
    {"nome": "Cantina", "categoria": "Italiano", "ativo": False},
]


def exibir_nome_programa():
    """
    Displays the name of the program in a stylized ASCII art format.

    This function prints a decorative ASCII art representation of the program's name
    to the console. It does not take any arguments or return any values."""
    print(
        """
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
"""
    )


def exibir_opções():
    """
    Displays a menu of options for the user to interact with the restaurant management system.

    Options:
    1. Cadastrar restaurante: Register a new restaurant.
    2. Listar restaurante: List all registered restaurants.
    3. Alternar estado do restaurante: Toggle the state of a restaurant (e.g., open/closed).
    4. Sair: Exit the application.
    """
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Alternar estado do restaurante")
    print("4. Sair\n")


def finalizar_app():
    """
    Finalizes the application by displaying a subtitle indicating the app is being closed.

    This function is used to gracefully terminate the application, ensuring that
    the user is informed about the closure process.
    """
    exibir_subtitulo("Finalizando o app")


def opcao_invalida():
    """
    Displays a message indicating an invalid option was selected and
    redirects the user back to the main menu.

    This function is typically used to handle cases where the user
    provides an input that does not match any of the expected options.
    """
    print("Opção inválida!\n")
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    """
    Exibe um subtítulo formatado no console com uma linha de asteriscos acima e abaixo do texto.

    Args:
        texto (str): O texto do subtítulo a ser exibido.

    Observação:
        A função utiliza o comando `os.system("cls")` para limpar o console antes de exibir o subtítulo.
        Isso é específico para sistemas Windows.
    """
    os.system("cls")
    linha = "*" * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()


def voltar_ao_menu_principal():
    """
    Pausa o programa e aguarda o usuário pressionar qualquer tecla antes de retornar ao menu principal.

    Esta função exibe um prompt solicitando ao usuário que pressione qualquer tecla para continuar.
    Assim que o usuário fornece a entrada, a função chama a função `main` para retornar ao menu principal.

    Nota:
        Certifique-se de que a função `main` esteja definida no mesmo módulo ou devidamente importada
        antes de chamar esta função para evitar um erro NameError.
    """
    input("\nDigite uma tecla para voltar ao menu principal.")
    main()


def cadastrar_novo_restaurante():
    """
    Cadastra um novo restaurante no sistema.

    Solicita ao usuário o nome e a categoria do restaurante, cria um dicionário
    com essas informações e adiciona-o à lista global de restaurantes. O restaurante
    é inicialmente marcado como inativo. Exibe uma mensagem de sucesso após o cadastro
    e retorna ao menu principal.

    Inputs:
        - Nome do restaurante (str): Nome do restaurante a ser cadastrado.
        - Categoria (str): Categoria do restaurante.

    Side Effects:
        - Adiciona um dicionário com os dados do restaurante à lista global `restaurantes`.
        - Exibe mensagens no console.
        - Chama a função `voltar_ao_menu_principal()`.

    Returns:
        None
    """
    exibir_subtitulo("Cadastro de novos restaurantes\n")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(
        f"Digite o nome da categoria do restaurante {nome_do_restaurante}: "
    )
    dados_do_restaurante = {
        "nome": nome_do_restaurante,
        "categoria": categoria,
        "ativo": False,
    }
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    voltar_ao_menu_principal()


def listar_restaurantes():
    """
    Exibe uma lista de restaurantes formatada com nome, categoria e status.
    A função exibe um subtítulo indicando que os restaurantes estão sendo listados.
    Em seguida, imprime uma tabela com os nomes dos restaurantes, suas categorias
    e seus respectivos status (ativado ou desativado). Após listar os restaurantes,
    a função retorna ao menu principal.
    Args:
        None
    Returns:
        None
    """
    exibir_subtitulo("Listando os restaurantes\n")

    print(f"{"Nome do Restaurante".ljust(22)} | {"Categoria".ljust(20)} | {"Status"}")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "ativado" if restaurante["ativo"] else "desativado"
        print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")
    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    """
    Alternates the active state of a restaurant in the list of restaurants.
    This function prompts the user to input the name of a restaurant. If the
    restaurant is found in the list, its "ativo" (active) state is toggled
    (activated if it was inactive, or deactivated if it was active). A message
    is displayed to indicate the success of the operation. If the restaurant
    is not found, an error message is displayed.
    The function also calls another function to return to the main menu after
    completing the operation.
    Side Effects:
        - Modifies the "ativo" state of a restaurant in the global `restaurantes` list.
        - Prints messages to the console.
        - Prompts the user for input.
    Raises:
        None
    Notes:
        - Assumes `restaurantes` is a global list of dictionaries, where each
          dictionary represents a restaurant with at least the keys "nome" and "ativo".
        - Assumes the existence of the `exibir_subtitulo` and `voltar_ao_menu_principal` functions.
    """
    exibir_subtitulo("Alternando estado do restaurante")
    nome_restaurante = input(
        "Digite o nome do restaurante que deseja alterar o estado: "
    )
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = (
                f"O restaurante {nome_restaurante} foi ativado com sucesso!"
                if restaurante["ativo"]
                else f"O restaurante {nome_restaurante} foi desativado com sucesso!"
            )
            print(mensagem)

    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")

    voltar_ao_menu_principal()


def escolher_opção():
    """
    Displays a menu to the user, prompts for an option, and executes the corresponding action.

    The function handles the following options:
    1. Calls the `cadastrar_novo_restaurante` function to register a new restaurant.
    2. Calls the `listar_restaurantes` function to list all restaurants.
    3. Calls the `alternar_estado_restaurante` function to toggle the state of a restaurant.
    4. Calls the `finalizar_app` function to terminate the application.

    If the user inputs an invalid option (not 1-4) or provides a non-integer input,
    the `opcao_invalida` function is called to handle the invalid input.

    Raises:
        ValueError: If the input cannot be converted to an integer.
    """
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()


def main():
    """
    Main function of the program.

    This function serves as the entry point for the application. It performs the following tasks:
    1. Clears the console screen.
    2. Displays the program name.
    3. Shows the available options to the user.
    4. Handles the user's choice of option.

    Note:
        Ensure that the required functions `os.system`, `exibir_nome_programa`,
        `exibir_opções`, and `escolher_opção` are properly defined and imported
        before calling this function.
    """
    os.system("cls")
    exibir_nome_programa()
    exibir_opções()
    escolher_opção()


if __name__ == "__main__":
    main()
