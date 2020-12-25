while True:
    print('\n\033[31m1 : para Calcular a área do Quadrado')
    print('2 : para Calcular a área do Retângulo')
    print('3 : para Calcular a área do Paralelogramo')
    print('4 : para Calcular a área do Trapézio')
    print('5 : para Calcular a área do losangulo')
    print('6 : para Calcular a área do Triângulo\033[m')

    a = str(input(': '))

    if(a == '1'):

        print('\nPara se calcular a área do Quadrado')
        print('pegue a medida de um lado e multiplique')
        print('por ele mesmo\n')

        h = float(input('Altura do quadrado: '))

        print(f'\nA área do quadrado é igual a \033[31m{h * h}\033[31m')

    elif(a == '2'):

        print('\nPara se calcular a área do Retângulo')
        print('pegue a medida da altura e da base')
        print('e multiplique altura * base\n')

        b = float(input('Base do Retângulo: '))
        h = float(input('Altura do Retângulo: '))

        print(f'\nA área do Retângulo é igual a \033[31m{b * h}\033[m')

    elif(a == '3'):

        print('\nPara se calcular a área do Paralelogramo')
        print('é semelhante ao Retângulo, altura * largura\n')

        b = float(input('Base do Paralelogramo: '))
        h = float(input('Altura do Paralelogramo: '))

        print(f'\nA área do Paralologramo é igual a \033[31m{b * h}\033[m')
    elif(a == '4'):

        print('\nPara se calcular a área do Trapézio')
        print('some base menor e base maior multiplique')
        print('pela altura e divida por 2\n')

        b = float(input('Base menor do Trapézio: '))
        b += float(input('Base maior do Trapézio: '))
        h = float(input('Altura do do Trapézio: '))

        print(f'\nA área do Trapézio é igual a \033[31m{(b * h) / 2}\033[m')
    elif(a == '5'):
        print('\nPara se calcular a área do Losangulo')
        print('Transforme-o em um Paralelogramo e')
        print('pegue a altura e base multiplique')
        print('altura * base e depois divida por 2\n')

        b = float(input('Base do Losangulo: '))
        h = float(input('Altura do Losangulo: '))

        print(f'\nA área do Losangulo é igual a \033[31m{(b * h) / 2}\033[m')
    elif(a == '6'):
        print('\nPara se calcular a área do Triângulo')
        print('transforme-o em um Paralelogramo pegue')
        print('a altura e a base e multiplique')
        print('depois divida-o por 2\n')

        b = float(input('Base do Triângulo: '))
        h = float(input('Altura do Triângulo: '))

        print(f'\nA área do Triângulo é igual a \033[31m{(b * h) / 2}\033[m')
    else:
        print('\n\003[31mERRO tente novamente\033[m')