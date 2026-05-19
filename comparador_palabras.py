#10. Comparador Inteligente. Desarrolla un programa que solicite dos palabras diferentes e indique si son idénticas, ignorando por completo la presencia de mayúsculas o minúsculas.

palabra_1 = input('Ingresa palabra clave 1: ')
palabra_2 = input('Ingresa palabra clave 2: ')


if palabra_1.lower() == palabra_2.lower():
    print(f'las palabras {palabra_1} y {palabra_2} son identicas en estructura')
else:
    print(f'Las palabras {palabra_1} y {palabra_2} son diferentes en estructura')
