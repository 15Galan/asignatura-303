from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class AES_CIPHER_CBC:
    BLOCK_SIZE_AES = 16     # AES: Bloque de 128 bits

    def __init__(self, key):
        """Inicializa las variables locales"""

        self.key = key

    def cifrar(self, cadena, IV):
        """Cifra el parámetro cadena (de tipo String) con una
        IV específica, y devuelve el texto cifrado binario"""

        cifrador = AES.new(self.key, AES.MODE_CBC, IV)
        texto_cifrado = cifrador.encrypt(pad(cadena.encode("utf-8"), self.BLOCK_SIZE_AES))

        return texto_cifrado

    def descifrar(self, cifrado, IV):
        """Descifra el parámetro cifrado (de tipo binario) con una
        IV específica, y devuelve la cadena en claro de tipo String"""

        descifrador = AES.new(self.key, AES.MODE_CBC, IV)
        texto_claro = unpad(descifrador.decrypt(cifrado), self.BLOCK_SIZE_AES)

        return texto_claro


# Código de prueba
key = get_random_bytes(16)  # Clave aleatoria de 128 bits
IV = get_random_bytes(16)   # IV aleatorio de 128 bits
d = AES_CIPHER_CBC(key)

datos = "Hola Mundo con AES en modo CBC"

cifrado = d.cifrar(datos, IV)
descifrado = d.descifrar(cifrado, IV)


# Muestra por pantalla
print("Mensaje original: " + datos)
print("\tCifrado: " + cifrado.decode("utf-8", "ignore"))
print("\tDescifrado: " + descifrado.decode("utf-8", "ignore"))
