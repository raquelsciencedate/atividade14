def calcular_area():
    figuras = {
        '1': ('Quadrado', lambda lado: lado ** 2),
        '2': ('Triângulo', lambda base, altura: (base * altura) / 2),
        '3': ('Círculo', lambda raio: 3.14159 * (raio ** 2)),
        '4': ('Trapézio', lambda base_maior, base_menor, altura: ((base_maior + base_menor) * altura) / 2)
    }

    print("Escolha a figura geométrica para calcular a área:")
    print("1. Quadrado")
    print("2. Triângulo")
    print("3. Círculo")
    print("4. Trapézio")
    
    escolha = input("Digite o número correspondente à figura: ")

    if escolha in figuras:
        figura, formula = figuras[escolha]
        if escolha == '1':
            lado = float(input("Digite o lado do quadrado: "))
            area = formula(lado)
        elif escolha == '2':
            base = float(input("Digite a base do triângulo: "))
            altura = float(input("Digite a altura do triângulo: "))
            area = formula(base, altura)
        elif escolha == '3':
            raio = float(input("Digite o raio do círculo: "))
            area = formula(raio)
        elif escolha == '4':
            base_maior = float(input("Digite a base maior do trapézio: "))
            base_menor = float(input("Digite a base menor do trapézio: "))
            altura = float(input("Digite a altura do trapézio: "))
            area = formula(base_maior, base_menor, altura)
        
        print(f"A área do {figura} é: {area}")
    else:
        print("Opção inválida. Tente novamente.")

calcular_area()
