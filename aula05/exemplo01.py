valor_pedido = float(input('Digite o valor: '))
distancia = float(input('Distancia: '))
frete = 8

if valor_pedido > 50 and distancia <= 3:
    valor_final = valor_pedido
    print('Frete Grátis')

else:
    valor_final = valor_pedido + frete
    print(f'Frete de R$: {frete}')
    print(f'Valor Final: R$ {valor_final:.2f}')
