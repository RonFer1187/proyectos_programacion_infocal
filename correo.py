#Diseña un sistema que extraiga únicamente el nombre del dominio de un correo electrónico (por ejemplo, de "juan@empresa.com" debe obtener "empresa.com").

correo = input('Ingresa el email de tu empresa: ')
extraccion = correo.split('@')
dominio = extraccion[1]

print(f'El dominio empresarial es: {dominio}')

