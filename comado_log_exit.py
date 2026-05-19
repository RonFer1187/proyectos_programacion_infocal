

print("--- Inicio de Comandos ---")
print("Comandos disponibles: 'LOG:[tu texto]' o 'EXIT' para salir.")


while True:
  
    comando = input("Ingrese Comando:  ")
    
  
    if comando.strip() == "EXIT":
        print("Terminando la ejecución. ¡Adiós!")
        break  
    elif comando.startswith("LOG:"):
        contenido_restante = comando[4:]
        print(f"[LOG PROCESADO]: {contenido_restante}")
    else:
        print("Comando no reconocido. Intenta con 'LOG:texto' o 'EXIT'.")

        