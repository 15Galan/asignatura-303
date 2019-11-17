from socket_class import SOCKET_SIMPLE_TCP
from Crypto.Random import get_random_bytes
import funciones_aes
import json


def cifraPaso1(emisor, receptor, KET, E, t_ne):
    """ Cifra el mensaje del paso 1, y devuelve el cifrado """
    # Codifica el contenido (los campos binarios en una cadena) y contruyo el mensaje JSON
    msg_TE = [E, t_ne.hex()]
    json_ET = json.dumps(msg_TE)
    print(emisor + " -> " + receptor + " (descifrado): " + json_ET)

    # Cifra los datos con AES GCM
    motor_AES = funciones_aes.iniciarAES_GCM(KET)
    cifrado_T, mac_T, nonce_T = funciones_aes.cifrarAES_GCM(motor_AES, json_ET.encode("utf-8"))

    return cifrado_T, mac_T, nonce_T


# Lee clave KBT
KBT = open("KBT.bin", "rb").read()

# Crear el socket de conexion con T (5551)
print("Creando conexion con T...")

socket = SOCKET_SIMPLE_TCP('127.0.0.1', 5551)
socket.conectar()

# Paso 1) B->T: KAT(Alice, Na) en AES-GCM
num = get_random_bytes(16)

cifrado, cifrado_mac, cifrado_nonce = cifraPaso1("B", "T", KBT, "Bob", num)

socket.enviar(cifrado)
socket.enviar(cifrado_mac)
socket.enviar(cifrado_nonce)

# Paso 2) T -> B : KBT(K1, K2, Nb) en AES-GCM
# A empezar a resolver!!!!!!!
print("Comienza el paso 2 en B")

cifrado_Tb1 = socket.recibir()
mac_Tb1 = socket.recibir()
nonce_Tb1 = socket.recibir()

descifrado_ETb1 = funciones_aes.descifrarAES_GCM(KBT, nonce_Tb1, cifrado_Tb1, mac_Tb1)
json_ETb1 = descifrado_ETb1.decode("utf-8", "ignore")

print("T " + " -> B (descifrado): " + json_ETb1)

mensaje_ETb1 = json.loads(json_ETb1)

K1, K2, t_nB1 = mensaje_ETb1
K1 = bytearray.fromhex(K1)
K2 = bytearray.fromhex(K2)
t_nB1 = bytearray.fromhex(t_nB1)

# Espero a Alice para el paso 5)

# Paso 5) A->B: KAB(Nombre) en AES-CTR con HMAC

# Paso 6) B->A: KAB(Apellido) en AES-CTR con HMAC

# Termina la comunicacion
socket.cerrar()
