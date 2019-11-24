from Crypto.Random import get_random_bytes
from socket_class import SOCKET_SIMPLE_TCP
import funciones_aes as aes
import json


def cifrar12(clave, mensaje):
    mensaje[2] = mensaje[2].hex()   # Ra

    # Codificar el mensaje
    mensaje_json = json.dumps(mensaje)

    # Cifrar el mensaje con AES (GCM)
    motor_AES = aes.iniciarAES_GCM(clave)
    cifrado, cifrado_mac, cifrado_nonce = aes.cifrarAES_GCM(motor_AES, mensaje_json.encode("utf-8"))

    return cifrado, cifrado_mac, cifrado_nonce


def descifrar23(clave, cifrado, mac, nonce):
    # Descifrar y decodificar el mensaje obtenido
    descifrado = aes.descifrarAES_GCM(clave, nonce, cifrado, mac)
    json_AT = descifrado.decode("utf-8", "ignore")

    # Extraer los datos del mensaje
    random, receptor, clave, cifrado_mensaje, cifrado_mac, cifrado_nonce = json.loads(json_AT)

    print("\t\tMensaje de", "TTP", ": ", json_AT, "\n")

    return random, receptor, clave, cifrado_mensaje, cifrado_mac, cifrado_nonce


# 0 - Obtener la clave entre Alice y TTP
Kat = open("KAT.bin", "rb").read()


# 1.1 - Generar un valor aleatorio Ra
Ra = get_random_bytes(16)

# 1.2 - Enviar el mensaje cifrado a TTP
mensaje = ["Alice", "Bob", Ra]

datos_AT, mac_AT, nonce_AT = cifrar12(Kat, mensaje)

print("Creando conexión con TTP...")
socket = SOCKET_SIMPLE_TCP('127.0.0.1', 5550)
socket.conectar()
print("Conexión establecida.\n")

print("\tEnviando...")
socket.enviar(datos_AT)
socket.enviar(mac_AT)
socket.enviar(nonce_AT)
print("\tMensaje enviado.\n")


# 2.3 - Esperar la respuesta de TTP
print("\tRecibiendo...")
datos_TA = socket.recibir()
mac_TA = socket.recibir()
nonce_TA = socket.recibir()
print("\tMensaje recibido.")

random, receptor, Kab, cifrado_mensaje, cifrado_mac, cifrado_nonce = descifrar23(Kat, datos_TA, mac_TA, nonce_TA)

if Ra.decode("utf-8", "ignore") != random:
    print("Valores aleatorios incorrectos")

socket.cerrar()


# 3 - Enviar el mensaje a Bob
print("Creando conexión con", receptor, "...")
socket = SOCKET_SIMPLE_TCP('127.0.0.1', 5551)
socket.conectar()
print("Conexión establecida.\n")

print("\tEnviando...")
socket.enviar(cifrado_mensaje.encode("utf-8"))
socket.enviar(cifrado_mac.encode("utf-8"))
socket.enviar(cifrado_nonce.encode("utf-8"))
print("\tEnviado.\n")


# 4.2 - Challenge-response (challenge)
print("\tRecibiendo...")
datos_BA = socket.recibir()
mac_BA = socket.recibir()
nonce_BA = socket.recibir()
print("\tMensaje recibido.")


# 5 - Challenge-response (response)
