from Crypto.Random import get_random_bytes
from socket_class import SOCKET_SIMPLE_TCP
import funciones_aes as aes
import json


def CIFRAR(clave, mensaje):
    # Codificar el contenido del mensaje
    mensaje_json = json.dumps(mensaje)

    # Cifrar los datos con AES (GCM)
    motor_AES = aes.iniciarAES_GCM(clave)
    cifrado, cifrado_mac, cifrado_nonce = aes.cifrarAES_GCM(motor_AES, mensaje_json.encode("utf-8"))

    return cifrado, cifrado_mac, cifrado_nonce


def DESCIFRAR(clave, cifrado):
    # Extraer los datos del mensaje cifrado
    cifrado_mensaje, cifrado_mac, cifrado_nonce = cifrado

    # Descifrar y decodificar el mensaje obtenido
    descifrado = aes.descifrarAES_GCM(clave, cifrado_nonce, cifrado_mensaje, cifrado_mac)
    json_AT = descifrado.decode("utf-8", "ignore")
    mensaje = json.loads(json_AT)

    print("\t\tMensaje de", emisor, ": ", json_AT, "\n")

    return mensaje


def descifrar3(clave, cifrado, mac, nonce):
    # Descifrar y decodificar el mensaje obtenido
    descifrado = aes.descifrarAES_GCM(clave, nonce, cifrado, mac)
    json_AT = descifrado #.decode("utf-8", "ignore")

    # Extraer los datos del mensaje
    clave, emisor = json.loads(json_AT)

    print("\t\tMensaje de", emisor, ": ", json_AT, "\n")

    return clave, emisor


# 0 - Obtener la clave entre Alice y TTP
Kbt = open("KBT.bin", "rb").read()


# 3 - Recibir mensaje cifrado desde el TTP
print("Abriendo conexión...")
socket = SOCKET_SIMPLE_TCP('127.0.0.1', 5551)
socket.escuchar()
print("Conexión establecida.\n")

print("\tRecibiendo...")
datos_AB = socket.recibir()
mac_AB = socket.recibir()
nonce_AB = socket.recibir()
print("\tMensaje recibido.")

Kab, emisor = descifrar3(Kbt, datos_AB, mac_AB, nonce_AB)


# 4.1 - Generar un valor aleatorio Rb
Rb = get_random_bytes(16)


# 4.2 - Challenge-response
challenge, challenge_mac, challenge_nonce = CIFRAR(Kab, Rb)

print("\t[CR] Enviando...")
socket.enviar(challenge)
socket.enviar(challenge_mac)
socket.enviar(challenge_nonce)
print("\t[CR] Mensaje enviado.\n")

print("\t[CR] Recibiendo...")
response = socket.recibir()
response_mac = socket.recibir()
response_nonce = socket.recibir()
print("\t[CR] Mensaje recibido.\n")

mensaje = DESCIFRAR(Kab, [response, response_mac, response_nonce])

print(mensaje)
