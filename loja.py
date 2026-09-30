continuar = True

while continuar:
    print("=== Sistema de Loja ===")
    print("1. Calcular Desconto")
    print("2. Calcular Troco")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        try:
            preco = float(input("Informe o preço do produto: "))
            print(f"O preço do produto é: R${preco:.2f}")
            desconto = float(input("Informe o percentual de desconto: "))
            print(f"O desconto é: {desconto}%")
            valor_desconto = preco * (desconto / 100)
            valor_final = preco - valor_desconto
            print(f"O valor do desconto é: R${valor_desconto:.2f}")
            print(f"O valor final do produto com desconto é: R${valor_final:.2f}")
        except ValueError:
            print("Valor inválido! Digite apenas números.")
    elif opcao == "2":
        try:
            valor_produto = float(input("Informe o valor do produto: "))
            valor_pago = float(input("Informe o valor pago pelo cliente: "))
            if valor_pago < valor_produto:
                print("O valor pago é insuficiente para cobrir o valor do produto.")
            else:
                troco = valor_pago - valor_produto
                print(f"O troco a ser devolvido ao cliente é R${troco:.2f}")
        except ValueError:
            print("Valor inválido! Digite apenas números.")
    elif opcao == "3":
        print("Saindo do sistema...")
        continuar = False
    else:
        print("Opção inválida")