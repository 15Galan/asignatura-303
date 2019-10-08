# Suponiendo que el mensaje/codigo no contenga
# otros simbolos que no sean letras o espacios.

def cifradoCesarAlfabetoInglesMAY(cadena):
    """Devuelve un cifrado Cesar tradicional (+3)"""

    # Definir la nueva cadena resultado
    resultado = ''

    # Realizar el "cifrado", sabiendo que A = 65, Z = 90, a = 97, z = 122
    i = 0

    while i < len(cadena):
        # Recoge el caracter a cifrar
        ordenClaro = ord(cadena[i])
        ordenCifrado = 0

        # Cambia el caracter a cifrar
        if (ordenClaro >= 65 and ordenClaro <= 90):
            ordenCifrado = (((ordenClaro - 65) + 3) % 26) + 65

        # Añade el caracter cifrado al resultado
        resultado = resultado + chr(ordenCifrado)
        i = i + 1

    # devuelve el resultado
    return resultado


# ----------------------------------------------------------------
# - Apartado a)
# ----------------------------------------------------------------
def descifradoCesarAlfabetoInglesMAY(codigo):
    """Devuelve un descifrado Cesar tradicional (-3)"""

    # Definicion de las variables.
    mensaje = ''        # Codigo descifrado.
    i = 0               # Contador.

    # Cifrado sabiendo que 'A' = 65, 'Z' = '90', 'a' = 97, 'z' = 122.
    while i < len(codigo):

        c = ord(codigo[i])      # Caracter del codigo.

        # Comprobacion de que es una letra.
        if 65 <= c <= 90:
            m = (((c - 65) - 3) % 26) + 65

        # Si no es una letra se sustituye por un espacio.
        else:
            m = 32

        # Formacion del mensaje descifrado.
        mensaje = mensaje + chr(m)
        i = i + 1

    return mensaje


# ----------------------------------------------------------------
# - Apartado b)
# ----------------------------------------------------------------
def cifradoCesarAlfabetoIngles(mensaje):
    """Devuelve un cifrado Cesar tradicional (+3)"""

    # Definicion de las variables.
    codigo = ''         # Mensaje cifrado.
    i = 0               # Contador.

    # Cifrado sabiendo que 'A' = 65, 'Z' = '90', 'a' = 97, 'z' = 122.
    while i < len(mensaje):

        m = ord(mensaje[i])     # Caracter del mensaje.

        # Comprobacion de que es una letra (mayuscula).
        if 65 <= m <= 90:
            c = (((m - 65) + 3) % 26) + 65

        # Comprobacion de que es una letra (minucsula).
        elif 97 <= m <= 122:
            c = (((m - 97) + 3) % 26) + 97

        # Si no es una letra se sustituye por un espacio.
        else:
            c = 32

        # Formacion del mensaje cifrado.
        codigo = codigo + chr(c)
        i = i + 1

    return codigo

def descifradoCesarAlfabetoIngles(codigo):
    """Devuelve un descifrado Cesar tradicional (-3)"""

    # Definicion de las variables.
    mensaje = ''        # Codigo descifrado.
    i = 0               # Contador.

    # Cifrado sabiendo que 'A' = 65, 'Z' = '90', 'a' = 97, 'z' = 122.
    while i < len(codigo):

        c = ord(codigo[i])      # Caracter del codigo.

        # Comprobacion de que es una letra (mayuscula).
        if 65 <= c <= 90:
            m = (((c - 65) - 3) % 26) + 65

        # Comprobacion de que es una letra (minuscula).
        elif 97 <= c <= 122:
            m = (((c - 97) - 3) % 26) + 97

        # Si no es una letra se sustituye por un espacio.
        else:
            m = 32

        # Formacion del mensaje descifrado.
        mensaje = mensaje + chr(m)
        i = i + 1

    return mensaje


# ----------------------------------------------------------------
# - Apartado c)
# ----------------------------------------------------------------
def cifradoCesarAlfabetoIngles_Generalizado(mensaje, i):
    """Devuelve un cifrado Cesar tradicional (+3)"""

    # Definicion de las variables.
    codigo = ''     # Mensaje cifrado.
    cont = 0        # Contador.

    # Cifrado sabiendo que 'A' = 65, 'Z' = '90', 'a' = 97, 'z' = 122.
    while cont < len(mensaje):

        m = ord(mensaje[cont])     # Caracter del mensaje.

        # Comprobacion de que es una letra (mayuscula).
        if 65 <= m <= 90:
            c = (((m - 65) + i) % 26) + 65

        # Comprobacion de que es una letra (minuscula).
        elif 97 <= m <= 122:
            c = (((m - 97) + i) % 26) + 97

        # Si no es una letra se sustituye por un espacio.
        else:
            c = 32

        # Formacion del mensaje cifrado.
        codigo = codigo + chr(c)
        cont = cont + 1

    return codigo

def descifradoCesarAlfabetoIngles_Generalizado(codigo, i):
    """Devuelve un descifrado Cesar tradicional (-3)"""

    # Definicion de las variables.
    mensaje = ''    # Codigo descifrado.
    cont = 0        # Contador.

    # Cifrado sabiendo que 'A' = 65, 'Z' = '90', 'a' = 97, 'z' = 122.
    while cont < len(codigo):

        c = ord(codigo[cont])       # Caracter del codigo.

        # Comprobacion de que es una letra (mayuscula).
        if 65 <= c <= 90:
            m = (((c - 65) - i) % 26) + 65

        # Comprobacion de que es una letra (minuscula).
        elif 97 <= c <= 122:
            m = (((c - 97) - i) % 26) + 97

        # Si no es una letra se sustituye por un espacio.
        else:
            m = 32

        # Formacion del mensaje descifrado.
        mensaje = mensaje + chr(m)
        cont = cont + 1

    return mensaje



"""Pruebas de las funciones"""

MENSAJE = "Veni Vidi Vinci Auria"
CODIGO = "Yhql Ylgl Ylqfl Dxuld"

# Apartado a)
print("Ejercicio 1.a)\n")
print("DESCIFRADO")
print("Codigo  : " + CODIGO.upper())
print("Mensaje : " + descifradoCesarAlfabetoInglesMAY(CODIGO.upper()))


# Apartado b)
print("\n\nEjercicio 1.b)\n")
print("CIFRADO")
print("Mensaje : " + MENSAJE)
print("Cifrado : " + cifradoCesarAlfabetoIngles(MENSAJE) + "\n")

print("DESCIFRADO")
print("Codigo  : " + CODIGO)
print("Mensaje : " + descifradoCesarAlfabetoIngles(CODIGO))


# Apartado c)
print("\n\nEjercicio 1.c)\n")
mensaje = input("Mensaje : ")
valor1 = int(input("Valor   : "))

cifrado = cifradoCesarAlfabetoIngles_Generalizado(mensaje, valor1)

print("CIFRADO")
print("\n\t" + mensaje)
print("\t" + cifrado + "\n")

codigo = input("Codigo : ")
valor2 = int(input("Valor  : "))

print("DESCIFRADO")
print("\n\t" + codigo)
print("\t" + descifradoCesarAlfabetoIngles_Generalizado(cifrado, valor2))
