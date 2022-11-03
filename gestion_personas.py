def agregar_personas(nombreArchivo, contenido):
    archivo = open(nombreArchivo + ".txt", "at")
    archivo.write(contenido)
    archivo.close()

def listar_personas(nombreArchivo):
    archivo = open(nombreArchivo + ".txt", encoding="utf8")
    datos_archivo = archivo.readlines()

    return datos_archivo
