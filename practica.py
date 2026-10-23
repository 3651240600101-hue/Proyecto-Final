# practica.py
import random
from conversiones import obtener_nombre_base, desde_decimal
from validaciones import validar_numero_en_base, normalizar_mayusculas

def ejecutar_modo_practica(estadisticas):
    """
    Gestiona el menú y los ejercicios del modo de práctica.
    'estadisticas' es un diccionario con 'aciertos' y 'respondidos' que persiste en la sesión.
    """
    bases_disponibles = [2, 8, 10, 16]
    
    while True:
        aciertos = estadisticas["aciertos"]
        respondidos = estadisticas["respondidos"]
        if respondidos > 0:
            porcentaje = (aciertos / respondidos) * 100.0
        else:
            porcentaje = 0.0
            
        print("\n========================================================")
        print("MODO DE PRÁCTICA")
        print("========================================================")
        print(f"Aciertos: {aciertos}")
        print(f"Ejercicios respondidos: {respondidos}")
        print(f"Porcentaje de aciertos: {porcentaje:.1f}%\n")
        print("1. Resolver un nuevo ejercicio")
        print("2. Reiniciar puntuación")
        print("3. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            # Elegir base de origen y base de destino distintas
            base_origen = random.choice(bases_disponibles)
            opciones_destino = []
            for b in bases_disponibles:
                if b != base_origen:
                    opciones_destino.append(b)
            base_destino = random.choice(opciones_destino)
            
            # Generar valor aleatorio entre 0 y 255
            valor_decimal = random.randint(0, 255)
            
            # Representar el número en la base de origen
            if base_origen == 10:
                numero_pregunta = str(valor_decimal)
            else:
                numero_pregunta, _ = desde_decimal(valor_decimal, base_origen)
                
            # Calcular la respuesta correcta en la base de destino
            if base_destino == 10:
                respuesta_esperada = str(valor_decimal)
            else:
                respuesta_esperada, _ = desde_decimal(valor_decimal, base_destino)
                
            nombre_orig = obtener_nombre_base(base_origen)
            nombre_dest = obtener_nombre_base(base_destino)
            
            print("\n========================================================")
            print("EJERCICIO DE PRÁCTICA")
            print("========================================================")
            print(f"Convierta {numero_pregunta} de {nombre_orig} a {nombre_dest}.\n")
            print("Ingrese únicamente el número de la respuesta.")
            
            # Ciclo para pedir una respuesta con formato válido para la base destino
            while True:
                respuesta_usuario = input("Su respuesta: ").strip()
                es_valido, msg_error = validar_numero_en_base(respuesta_usuario, base_destino)
                if not es_valido:
                    print(msg_error)
                    print("Intente nuevamente (este error de formato no afecta su puntuación).\n")
                else:
                    break
                    
            # Normalizar respuesta (quitar ceros a la izquierda innecesarios salvo que sea "0")
            resp_norm = normalizar_mayusculas(respuesta_usuario).lstrip("0")
            if resp_norm == "":
                resp_norm = "0"
                
            estadisticas["respondidos"] += 1
            if resp_norm == respuesta_esperada:
                estadisticas["aciertos"] += 1
                print("\n¡Respuesta correcta!")
            else:
                print(f"\nRespuesta incorrecta. La respuesta esperada era: {respuesta_esperada}")
                
            # Mostrar estadísticas actualizadas
            aciertos_act = estadisticas["aciertos"]
            resp_act = estadisticas["respondidos"]
            porc_act = (aciertos_act / resp_act) * 100.0
            print(f"\nAciertos: {aciertos_act}")
            print(f"Ejercicios respondidos: {resp_act}")
            print(f"Porcentaje de aciertos: {porc_act:.1f}%")
            input("\nPresione Enter para continuar...")
            
        elif opcion == "2":
            estadisticas["aciertos"] = 0
            estadisticas["respondidos"] = 0
            print("\nLa puntuación ha sido reiniciada a cero.")
            input("Presione Enter para continuar...")
            
        elif opcion == "3":
            return
        else:
            print("\nError: Opción inválida. Por favor seleccione 1, 2 o 3.")