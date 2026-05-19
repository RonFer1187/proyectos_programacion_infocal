
palabra_1 = input('Ingrese una palabra: ')

palabra_2 = palabra_1[::-1]

if palabra_1 == palabra_2:
    print(f'La palabra {palabra_1} es un palíndromo')
else:
    print(f'La palabra {palabra_1} no es un palíndromo')

