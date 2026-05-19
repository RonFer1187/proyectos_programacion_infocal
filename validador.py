#Crea u n validador que determine si la palabra "Python" (insensible a mayúsculas) existe dentro de un bloque de texto q u e el usuario ingrese voluntariamente.

frase = input('Ingresa una frase sobre programar en Python: ')

palabra_clave = 'python'

if palabra_clave in frase.lower():
    print("Encontramos la palabra clave: Python")
else:
    print('No encontramos la palabra clave: Python')

