nota_final = float(input('Nota final '))
frequencia = float(input('Frequência (%)'))
mensalidade = float(input('Valor da mensalidade '))

if nota_final >= 7.0 and frequencia >= 75:
    bolsa = mensalidade * 0.20
    print(f'Tem direito a bolsa {bolsa:.2f}')

else:
    print('Nao tem direito a bolsa.')
    