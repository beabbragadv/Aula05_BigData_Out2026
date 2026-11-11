# Quatro notas
 
nota1 = float(input('Nota1: '))
nota2 = float(input('Nota2: '))
nota3 = float(input('Nota3: '))
nota4 = float(input('Nota4: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f'Média final: {media:.2f}')

if media >= 7.0:
    print('Situação: Aprovado')

elif media >= 5.0:
    print('Situação: Em recuperação')

else:
    print('Reprovado')