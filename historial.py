# historial.py

def agregar_al_historial(lista_historial, entrada, base_origen_nombre, base_destino_nombre, resultado):
    """Agrega un nuevo registro como diccionario o lista a la lista de historial."""
    registro = {
        "entrada": entrada,
        "origen": base_origen_nombre,
        "destino": base_destino_nombre,
        "resultado": resultado
    }
    lista_historial.append(registro)


def mostrar_menu_historial(lista_historial):
    """Muestra y gestiona el submenú de historial."""
    while True:
        print("\n========================================================")
        print("HISTORIAL DE CONVERSIONES")
        print("========================================================")
        
        if len(lista_historial) == 0:
            print("El historial de conversiones está vacío.")
            input("\nPresione Enter para volver al menú principal...")
            return
            
        contador = 1
        for reg in lista_historial:
            print(f"\nRegistro {contador}")
            print(f"Entrada: {reg['entrada']}")
            print(f"Origen: {reg['origen']}")
            print(f"Destino: {reg['destino']}")
            print(f"Resultado: {reg['resultado']}")
            contador += 1
            
        print(f"\nTotal de registros: {len(lista_historial)}")
        print("\n1. Eliminar un registro")
        print("2. Vaciar historial")
        print("3. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            num_str = input("Ingrese el número de registro que desea eliminar: ").strip()
            # Validar que sea un entero válido
            es_numero = True
            if len(num_str) == 0:
                es_numero = False
            else:
                for c in num_str:
                    if c not in "0123456789":
                        es_numero = False
                        break
                        
            if not es_numero:
                print("Error: Debe ingresar un número entero válido.")
            else:
                indice_eliminar = int(num_str)
                if 1 <= indice_eliminar <= len(lista_historial):
                    eliminado = lista_historial.pop(indice_eliminar - 1)
                    print(f"Registro {indice_eliminar} ({eliminado['entrada']} de {eliminado['origen']} a {eliminado['destino']}) eliminado correctamente.")
                else:
                    print(f"Error: No existe el registro número {indice_eliminar}.")
            input("Presione Enter para continuar...")
            
        elif opcion == "2":
            lista_historial.clear()
            print("El historial ha sido vaciado por completo.")
            input("Presione Enter para volver al menú principal...")
            return
            
        elif opcion == "3":
            return
        else:
            print("Error: Opción no válida. Seleccione 1, 2 o 3.")