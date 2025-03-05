# Inicializa uma lista vazia para a matriz do cinema
cinema = []

# Loop externo para percorrer as fileiras
for x in range(5):

    # Inicializa uma lista vazia para a fileira atual
    fileira = []

    # Loop interno para percorrer os assentos dentro de uma fileira
    for y in range(10):

        # Adiciona um assento disponível ('D') à fileira atual
        fileira.append("D")

    # Adiciona a fileira completa à matriz do cinema
    cinema.append(fileira)

fila = 0

assento = 0

print("Resserva de Assentos no Cinema")

# Inicia um loop infinito para o menu de opções
while True:

    print() 
    
    # Imprime o menu de opções
    print("Menu")

    print()

    print("1 - Ver assentos disponíveis")

    print("2 - Reservar assento")

    print("3 - Sair")

    print()

    # Solicita ao usuário que escolha uma opção
    op = input("Escolha uma opção: ")

    print()

    # Se o usuário escolher a opção 1
    if op == "1":

        # Inicia um loop para percorrer cada fileira da matriz do cinema
        for x in cinema:

            # Inicia um loop interno para percorrer cada assento na fileira atual
            for y in x:

                # Imprime o status do assento (por exemplo, 'D' para disponível ou 'R' para reservado) sem quebrar a linha
                print(f"{y}", end = " ")

            # Imprime uma quebra de linha após imprimir todos os assentos de uma fileira completa
            print()

        print()

        print("Legendas:") 
    
        print("(D) - Disponível")
    
        print("(R) - Reservado")

    # Se o usuário escolher a opção 2
    elif op == "2":

        # Solicita ao usuário que escolha a fileira e o assento que deseja reservar
        fila = int(input("Escolha a fileira (1-5): "))

        if fila >= 1 and fila <= 5:

            assento = int(input("Escolha o assento (1-10): "))

            if assento >= 1 and assento <= 10:

                # Verifica se o assento escolhido está disponível
                if cinema[fila - 1][assento - 1] == "D":

                    print("Assento reservado com sucesso")

                    # Se estiver disponível, marca o assento como reservado (R = Reservado)
                    cinema[fila - 1][assento - 1] = "R"
    
                else: 

                    # Se o assento já estiver reservado, informa ao usuário
                    print("Este assento já está ocupado")

            else:

                print("Assento Inválido")

        else:

            print("Fileira Inválida")

    # Se o usuário escolher a opção 3
    elif op == "3":

        # Agradece ao usuário e encerra o programa
        print("Obrigado por usar o nosso sistema")

        break

    # Se o usuário escolher uma opção inválida
    else:

        print("Opção Inválida")
