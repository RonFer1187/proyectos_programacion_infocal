
nombre_institucion = input("Ingresa el nombre completo de la organización: ")

palabras = nombre_institucion.split()

siglas = ""

for palabra in palabras:

    if len(palabra) > 3:
        
        siglas += palabra[0].upper()


print(f"Las siglas correspondientes son: {siglas}")