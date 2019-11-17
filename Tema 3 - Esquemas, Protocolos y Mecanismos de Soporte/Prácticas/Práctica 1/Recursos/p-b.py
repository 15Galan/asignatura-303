from Crypto.Hash import SHA256, HMAC
import base64
import json
import sys
from socket_class import SOCKET_SIMPLE_TCP
import funciones_aes
from Crypto.Random import get_random_bytes

def cifraPaso1(emisor, receptor, KET, E, t_ne):
    """ Cifra el mensaje del paso 1, y devuelve el cifrado """
    # Codifica el contenido (los campos binarios en una cadena) y contruyo el mensaje JSON
    msg_TE = []
    msg_TE.append(E)
    msg_TE.append(t_ne.hex())
    json_ET = json.dumps(msg_TE)
    print(emisor + "->" + receptor + " (descifrado): " + json_ET)

    # Cifra los datos con AES GCM
    aes_engine = funciones_aes.iniciarAES_GCM(KET)
    t_cifrado, t_mac, t_nonce = funciones_aes.cifrarAES_GCM(aes_engine,json_ET.encode("utf-8"))

    return t_cifrado, t_mac, t_nonce

# Lee clave KBT
KBT = open("KBT.bin", "rb").read()

# Crear el socket de conexion con T (5551)
print("Creando conexion con T...")
socket = SOCKET_SIMPLE_TCP('127.0.0.1', 5551)
socket.conectar()

# Paso 1) B->T: KAT(Alice, Na) en AES-GCM
t_n = get_random_bytes(16)
cifrado, cifrado_mac, cifrado_nonce = cifraPaso1("B", "T", KBT, "Bob", t_n)
socket.enviar(cifrado)
socket.enviar(cifrado_mac)
socket.enviar(cifrado_nonce)

# Paso 2) T->B: KBT(K1, K2, Nb) en AES-GCM
# A empezar a resolver!!!!!!!

# Espero a Alice para el paso 5)

# Paso 5) A->B: KAB(Nombre) en AES-CTR con HMAC

# Paso 6) B->A: KAB(Apellido) en AES-CTR con HMAC

# Termina la comunicacion
socket.cerrar()
