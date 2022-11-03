import gestion_personas

def validar_login():
    login = open("login.txt", encoding="utf8")
    usr = login.read()

    return usr

def validar_clave():
    clave = open("clave.txt", encoding="utf8")
    pssw = clave.read()

    return pssw

def menu():
    print("\t\t\tDATOS DE PERSONAS")
    print("1. Listar personas"
          + "\n2. Agregar personas"
          + "\n3. Salir")
    opcion = int(input("Digite la opción: "))

    if opcion == 1:
        dni = gestion_personas.listar_personas("dni")
        nombres = gestion_personas.listar_personas("nombre")
        apellidos = gestion_personas.listar_personas("apellido")

        print("\t\t\t\t\tLISTADO DE PERSONAS")
        print("\nOrden\t\t\t\tN° de DNI\t\t\t\tNombres\t\t\t\tApellidos")
        for n in range(len(dni)):
            print("  " + str(n+1) + "  \t\t\t\t" + dni[n].strip() + "\t\t\t\t" + nombres[n].strip() + "\t\t\t\t" + apellidos[n].strip())

    if opcion == 2:
        print("\n\tAGREGAR DATOS DE PERSONAS")
        nuevo_dni = input("Digite el nuevo N° de DNI: ")
        nuevo_nombres = input("Digite los nuevos nombres: ")
        nuevo_apellidos = input("Digite los nuevos apellidos: ")

        gestion_personas.agregar_personas("dni", nuevo_dni)
        gestion_personas.agregar_personas("nombre", nuevo_nombres)
        gestion_personas.agregar_personas("apellido", nuevo_apellidos)

    if opcion == 3:
        print("\nPROGRAMA FINALIZADO CON ÉXITO")
        return

def iniciar_sesion(intentos = 0):
    user = input("\nDigite el nombre de usuario: ")
    password = input("Digite la contraseña: ")

    if user == validar_login() and password == validar_clave():
        print()
        menu()
    else:
        print("DATOS INCORRECTOS. VUELVA A INTENTARLO")
        print(f"Intento número: {intentos + 1}")
        intentos += 1
        if intentos > 2:
            print("\n\nCANTIDAD DE INTENTOS EXCEDIDA"
                  "\nPROGRAMA FINALIZADO")
            return
        else:
            iniciar_sesion(intentos)

print("\n\t\t\t¡BIENVENIDO!")
iniciar_sesion()