from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64


class AES_CIPHER:
    TAM_BLOQUE_AES = 16  # AES: Bloque de 128 bits

    def __init__(self, key):  # Constructor de la clase
        self.clave = key


    def cifrar(self, cadena, modo, IV, nonce):
        global cifrador
        op = modo.upper()

        # Detectar el modo elegido por el usuario
        if op == "CBC":
            cifrador = AES.new(self.clave, AES.MODE_CBC, IV)

        elif op == "ECB":
            cifrador = AES.new(self.clave, AES.MODE_ECB)

        elif op == "CTR":
            cifrador = AES.new(self.clave, AES.MODE_CTR, nonce=nonce)

        elif op == "OFB":
            cifrador = AES.new(self.clave, AES.MODE_OFB, IV)

        elif op == "CFB":
            cifrador = AES.new(self.clave, AES.MODE_CFB, IV)

        elif op == "GCM":
            cifrador = AES.new(self.clave, AES.MODE_GCM, nonce=nonce)   # 'mac_len = 16' por defecto

        else:
            return -1

        # Elegir entre cifrado con ó sin padding
        if op == "CTR":
            return cifrador.encrypt(cadena.encode("utf-8"))

        else:
            return cifrador.encrypt(pad(cadena.encode("utf-8"), self.TAM_BLOQUE_AES))


    def descifrar(self, cifrado, modo, IV, nonce):
        global descifrador
        op = modo.upper()

        # Detectar el modo elegido por el usuario.
        if op == "CBC":
            descifrador = AES.new(self.clave, AES.MODE_CBC, IV)

        elif op == "ECB":
            descifrador = AES.new(self.clave, AES.MODE_ECB)

        elif op == "CTR":
            descifrador = AES.new(self.clave, AES.MODE_CTR, nonce=nonce)

        elif op == "OFB":
            descifrador = AES.new(self.clave, AES.MODE_OFB, IV)

        elif op == "CFB":
            descifrador = AES.new(self.clave, AES.MODE_CFB, IV)

        elif op == "GCM":
            descifrador = AES.new(self.clave, AES.MODE_GCM, nonce=nonce)    # 'mac_len = 16' por defecto

        else:
            return -1

        # Elegir entre descifrado con ó sin padding
        if op == "CTR":
            return descifrador.decrypt(cifrado).decode("utf-8", "ignore")

        else:
            return unpad(descifrador.decrypt(cifrado), self.TAM_BLOQUE_AES).decode("utf-8", "ignore")


# Datos necesarios
clave = get_random_bytes(16)    # Clave aleatoria de 128 bit
IV = get_random_bytes(16)       # Vector de Inicializacion aleatorio de 128 bits
nonce = get_random_bytes(8)     # Nonce para el modo CTR
d = AES_CIPHER(clave)           # Objeto de la clase AES_CIPHER con la clave 'clave'

mensaje = input("Texto en claro: ")                     # Cadena para cifrar y descifrar
modo = input("Modo (CBC, ECB, CTR, OFB, CFB, GCM): ")   # Modo de operación para el cifrado / descifrado


# Muestra de datos por pantalla
cifrado = d.cifrar(mensaje, modo, IV, nonce)

if cifrado != -1:
    descifrado = d.descifrar(cifrado, modo, IV, nonce)

    print("\nTexto cifrado (binario):")
    print(cifrado.decode("utf-8", "ignore"), "\n")

    print("Texto cifrado (base 64):")
    print(base64.b64encode(cifrado), "\n")

    print("Texto descifrado:")
    print(descifrado)

else:
    print("\nModo incorrecto")
