def mostrar_bienvenida():
    print("\n=== SISTEMA DE PERFIL DEL DESARROLLADOR ===")


def obtener_nombre():
    nombre = input("\nIngresa tu nombre: ")
    return nombre


def obtener_edad():
    while True:
        try:
            edad = int(input("Ingresa tu edad: "))

            if edad <= 0:
                print("La edad debe ser mayor a cero.")
                continue

            return edad

        except ValueError:
            print("Debes ingresar un número válido.")


def obtener_meta():
    meta = input("¿Cuál es tu meta en tecnología? ")
    return meta


def analizar_disciplina(horas):

    if horas >= 3:
        print("Ritmo fuerte.")
    elif horas >= 1:
        print("Ritmo aceptable.")
    else:
        print("Necesitas más constancia.")

def analizar_perfil(edad):

    print("\n=== ANÁLISIS ===")

    if edad >= 30:
        print("Nunca es tarde para entrar a tecnología.")
    elif edad >= 25:
        print("Todavía tienes muchísimo tiempo para crecer.")
    else:
        print("Tienes una ventaja enorme si eres constante.")


def analizar_disciplina(horas):
    if horas >= 3:
        print("Ritmo fuerte.")
    elif horas >= 1:
        print("Ritmo aceptable.")
    else:
        print("Necesitas más constancia.")



def main():
    mostrar_bienvenida()

    nombre = obtener_nombre()
    edad = obtener_edad()
    meta = obtener_meta()
    while True:
        try:
            horas = int(input("¿Cuántas horas estudiarás al día? "))

            if horas < 0:
                print("Las horas no pueden ser negativas.")
                continue

            break

        except ValueError:
            print("Debes ingresar un número válido.")

    print("\n=== PERFIL ===")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Meta: {meta}")

    analizar_perfil(edad)
    analizar_disciplina(horas)

    print("\nSigue construyendo. La consistencia cambia vidas.")


main()