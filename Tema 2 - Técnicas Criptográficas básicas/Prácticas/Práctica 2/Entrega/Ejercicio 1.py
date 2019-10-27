from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Datos necesarios
clave = get_random_bytes(16)    # Clave aleatoria de 128 bits
IV = get_random_bytes(16)       # IV aleatorio de 128 bits para CBC
TAM_BLOQUE_AES = 16             # Bloque de 128 bits

# Mensajes que van a ser cifrados
mensaje1 = "Hola amigos de la seguridad"
mensaje2 = "Hola amigas de la seguridad"

# CIFRADO #######################################################################

# Mecanismo de cifrado AES en modo CBC con un vector de inicialización IV
cifrador = AES.new(clave, AES.MODE_CBC, IV)

# Cifrado haciendo que los mensajes sean múltiplo del tamaño de bloque
cifrado1 = cifrador.encrypt(pad(mensaje1.encode("utf-8"), TAM_BLOQUE_AES))
cifrado2 = cifrador.encrypt(pad(mensaje2.encode("utf-8"), TAM_BLOQUE_AES))


# DESCIFRADO #######################################################################

# Mecanismo de (des)cifrado AES en modo CBC con un vector de inicialización IV
descifrador = AES.new(clave, AES.MODE_CBC, IV)

# Desciframos, eliminamos el padding, y recuperamos la cadena
descifrado1 = unpad(descifrador.decrypt(cifrado1), TAM_BLOQUE_AES).decode("utf-8", "ignore")
descifrado2 = unpad(descifrador.decrypt(cifrado2), TAM_BLOQUE_AES).decode("utf-8", "ignore")


# Muestra del proceso
print("Mensaje: " + mensaje1)
print("\tCifrado   : " + cifrado1.decode("utf-8", "ignore"))
print("\tDescifrado: " + descifrado1)
print()
print("Mensaje: " + mensaje2)
print("\tCifrado   : " + cifrado2.decode("utf-8", "ignore"))
print("\tDescifrado: " + descifrado2)


"""Si se observan los textos cifrados, es posible ver que ese cambio de una “o” por
una “a” (amigos → amigas) impacta en ambos textos, ¿a qué se debe ese cambio?"""

# Se debe a que se produce un cambio en el primer bloque del texto en claro
# 'Hola amigXs de l', por tanto, se cifra de forma diferente para ambos mensajes
# y esto produce que dicho cambio se propague al resto de la ejecución.
