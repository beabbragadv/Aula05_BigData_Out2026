numero = float(input('Número: '))

match numero:
    case 0:
        print('Zero')

    case num if num > 0:
        print('Positivo')

    case num if num < 0:
        print('Negativo')