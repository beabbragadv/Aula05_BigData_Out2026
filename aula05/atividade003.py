valor_compra = float(input('Valor da Compra '))
cadastro = input('Cliente cadastrado? [S/N]: ').lower()[0]

frete = 25

if valor_compra > 200 or cadastro == 's':
    valor_final = valor_compra
    print(f'Frete gratis. Valor final: R$ {valor_final}')

else:
    valor_final = valor_compra + frete
    print(f'Frete de R$ {frete}. Valor Final R$ {valor_final}')
    