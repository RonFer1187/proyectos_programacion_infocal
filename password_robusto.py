#Escribe un validador de contraseñas. Debe verificar que el texto tenga al menos 8 caracteres y no contenga la palabra "clave" o "123" en su contenido.

password = (input('Crea tu password con mínimo 8 caracteres: '))

palabra_clave = 'clave'
numero_clave = '123'

if len(password) < 8 or palabra_clave in password.lower() or numero_clave in password:
    print('Su password debe tener mínimo 8 caracteres y no debe contener la palabra CLAVE o 123')
else:
    print('Creacion de password correcta')



