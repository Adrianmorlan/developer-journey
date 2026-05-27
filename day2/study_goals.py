metas = []


def mostrar_menu():
    print("""=== SISTEMA DE METAS ===)
    
                1. Agregar meta
                2. Ver metas
                3. eliminar meta
                4. contar metas
                5. salir
                """)


while True:

    mostrar_menu()

    opcion = input("\nSelecciona una opción: ")

    if opcion == "1":

        meta = input("Escribe una nueva meta: ")

        metas.append(meta)

        print("Meta agregada correctamente.")

    elif opcion == "2":

        print("\n=== TUS METAS ===")

        if len(metas) == 0:
            print("No tienes metas registradas.")

        else:
            for meta in metas:
                print(f"- {meta}")

    elif opcion == "3":

        print("\n=== ELIMINAR META ===")

        Bmeta = input("Escribe qué meta quieres eliminar: ")

        if Bmeta in metas:

            metas.remove(Bmeta)

            print("Meta eliminada correctamente.")


        else:

            print("Esa meta no existe.")


    elif opcion == "4":
        print("=== CONTADOR DE METAS ===")

        if len(metas) == 0:
            print("No tienes metas registradas.")

        else:
            total = len(metas)
            print(f"tienes - {total} metas registradas.")


    elif opcion == "5":

        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida.")