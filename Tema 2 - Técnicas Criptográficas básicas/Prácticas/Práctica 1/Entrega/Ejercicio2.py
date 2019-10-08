# Suponiendo que el mensaje/codigo no contenga
# otros simbolos que no sean letras o espacios.

def cifradoMonoalfabetico(mensaje, clave):
    """Devuelve un cifrado Monoalfabetico"""

    # Definición de las variables.
    codigo = ''     # Mensaje cifrado.
    cadena = ''     # Mensaje en claro sin espacios.
    crypto = ''     # Clave repetida sin espacios.
    i = 0           # Contador para crear 'cadena'.
    j = 0           # Contador para crear 'crypto'.

    # Suprimir espacios del mensaje
    # Suprimir espacios y repetir la clave.
    while i < len(mensaje):
        if mensaje[i] != ' ':
            cadena = cadena + mensaje[i].upper()
            crypto = crypto + clave[j % len(clave)].upper()
            j = j + 1

        i = i + 1

    i = 0

    print("\nMensaje a cifrar : " + cadena)
    print("Clave de cifrado : " + crypto)

    # Cifrado sabiendo que 'A' = 65, 'Z' = '90', 'a' = 97, 'z' = 122.
    while i < len(cadena):

        # Variables internas.
        m = ord(cadena[i]) - 65                     # Caracter del mensaje (alfabeto 0 - 25).
        e = ord(crypto[i % len(clave)]) - 65 + 1    # Caracter de la clave (alfabeto 1 - 26).
        c = (m + e) % 26 + 65                       # Caracter cifrado (alfabeto 0 - 25).

        # Formacion del codigo (alfabeto ASCII).
        codigo = codigo + chr(c)

        i = i + 1

    return codigo

def descifradoMonoalfabetico(codigo, clave):
    """Devuelve un descifrado Monoalfabetico"""

    # Definición de las variables.
    mensaje = ''    # Mensaje en claro.
    cadena = ''     # Mensaje cifrado sin espacios.
    crypto = ''     # Clave repetida sin espacios.
    i = 0           # Contador para crear 'cadena'.
    j = 0           # Contador para crear 'crypto'.

    # Suprimir espacios del mensaje
    # Suprimir espacios y repetir la clave.
    while i < len(codigo):
        if codigo[i] != ' ':
            cadena = cadena + codigo[i].upper()
            crypto = crypto + clave[j % len(clave)].upper()
            j = j + 1

        i = i + 1

    i = 0

    print("\nCadena a descifrar  : " + cadena)
    print("Clave de descifrado : " + crypto)

    # Cifrado sabiendo que 'A' = 65, 'Z' = '90', 'a' = 97, 'z' = 122.
    while i < len(cadena):

        # Variables internas.
        c = ord(cadena[i]) - 65                     # Caracter del codigo (alfabeto 0 - 25).
        e = ord(crypto[i % len(clave)]) - 65 + 1    # Caracter de la clave (alfabeto 1 - 26).
        m = (c - e) % 26 + 65                       # Caracter descifrado (alfabeto 0 - 25).

        # Formacion del codigo (alfabeto ASCII).
        mensaje = mensaje + chr(m)

        i = i + 1

    return mensaje



"""Pruebas de las funciones"""

print("CODIFICACIÓN")
mensaje = input("Mensaje : ")
clave = input("Clave   : ")
print("Mensaje cifrado  : " + cifradoMonoalfabetico(mensaje, clave) + "\n\n")

print("DESCODIFICACION")
mensaje = input("Codigo : ")
clave = input("Clave  : ")
print("Mensaje descifrado  : " + descifradoMonoalfabetico(mensaje, clave) + "\n")
