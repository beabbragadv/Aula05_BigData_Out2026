venda = float(input('Valor da venda: '))

match venda:
    case vd if vd < 100:
        print('Venda Pequena')

    case vd if vd <= vd < 500:
        print('Venda média')
    
    case _:
        print('Venda grande')