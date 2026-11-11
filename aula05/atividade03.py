compra = float(input('Valor da compra:'))
fidelidade = input('Cliente cadastrado fidelidade? [S/N]: ').lower()[0]

cadastrado = fidelidade == 's'

if compra > 200 or cadastrado:
    total = compra
    print("Frete gratis!")

else:
    total = compra + 25
    print("Frete de R$ 25")
    print(f'Valor final da compra: R$ {total:.2f}')