from socket_class import SOCKET_SIMPLE_TCP
from Crypto.Random import get_random_bytes
import funciones_aes
import json


def cifraPaso3(emisor, receptor, KET, E, t_ne):
    """ Cifra el mensaje del paso 1, y devuelve el cifrado """
    # Codifica el contenido (los campos binarios en una cadena) y contruyo el mensaje JSON
    mensaje_ET = [E, t_ne.hex()]
    json_ET = json.dumps(mensaje_ET)
    print(emisor + " -> " + receptor + " (descifrado): " + json_ET)

    # Cifra los datos con AES GCM
    motor_AES = funciones_aes.iniciarAES_GCM(KET)
    cifrado_T, mac_T, nonce_T = funciones_aes.cifrarAES_GCM(motor_AES, json_ET.encode("utf-8"))

    return cifrado_T, mac_T, nonce_T


# Lee clave KBT
KAT = open("KAT.bin", "rb").read()

# Crear el socket de conexion con T (5550)
print("Creando conexion con T...")

socket = SOCKET_SIMPLE_TCP('127.0.0.1', 5550)
socket.conectar()

# Paso 3) A->T: KAT(Alice, Na) en AES-GCM
num = get_random_bytes(16)

cifrado, cifrado_mac, cifrado_nonce = cifraPaso3("A", "T", KAT, "Alice", num)

socket.enviar(cifrado)
socket.enviar(cifrado_mac)
socket.enviar(cifrado_nonce)

# Paso 4
print("Comienza el paso 4 en A")

cifrado_Ta1 = socket.recibir()
mac_Ta1 = socket.recibir()
nonce_Ta1 = socket.recibir()

descifrado_ETa1 = funciones_aes.descifrarAES_GCM(KAT, nonce_Ta1, cifrado_Ta1, mac_Ta1)
json_ETa1 = descifrado_ETa1.decode("utf-8", "ignore")

print("T " + " -> A (descifrado): " + json_ETa1)
mensaje_ETa1 = json.loads(json_ETa1)

K1, K2, t_nA1 = mensaje_ETa1
K1 = bytearray.fromhex(K1)
K2 = bytearray.fromhex(K2)
t_nA1 = bytearray.fromhex(t_nA1)
