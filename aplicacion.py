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
