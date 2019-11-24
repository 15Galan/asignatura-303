from socket_class import SOCKET_SIMPLE_TCP
import funciones_aes as aes
import json


def cifrar22(clave, mensaje):
    mensaje[0] = mensaje[0].decode("utf-8", "ignore")

    # Codificar el contenido del mensaje
    mensaje_json = json.dumps(mensaje)

    # Cifrar los datos con AES (GCM)
    motor_AES = aes.iniciarAES_GCM(clave)
    cifrado, cifrado_mac, cifrado_nonce = aes.cifrarAES_GCM(motor_AES, mensaje_json.encode("utf-8"))

    return cifrado, cifrado_mac, cifrado_nonce


def cifrar23(random, receptor, clave, cifrado):
    mensaje = [random.decode("utf-8", "ignore"),
               receptor,
               clave.decode("utf-8", "ignore"),
               cifrado[0].decode("utf-8", "ignore"),
               cifrado[1].decode("utf-8", "ignore"),
               cifrado[2].decode("utf-8", "ignore")]

    # Codificar el contenido del mensaje
    mensaje_json = json.dumps(mensaje)

    # Cifrar los datos con AES (GCM)
    motor_AES = aes.iniciarAES_GCM(clave)
    cifrado, cifrado_mac, cifrado_nonce = aes.cifrarAES_GCM(motor_AES, mensaje_json.encode("utf-8"))

    return cifrado, cifrado_mac, cifrado_nonce


def descifrar12(clave, cifrado, mac, nonce):
    # Descifrar y decodificar el mensaje obtenido
    descifrado = aes.descifrarAES_GCM(clave, nonce, cifrado, mac)
    json_AT = descifrado.decode("utf-8", "ignore")

    # Extraer los datos del mensaje
    emisor, receptor, random = json.loads(json_AT)
    random = bytearray.fromhex(random)

    print("\t\tMensaje de", emisor, ": ", json_AT, "\n")

    return emisor, receptor, random


# 0 - Crear la clave entre Alice/Bob y TTP
Kat = aes.crear_AESKey()

fichero_Kat = open("KAT.bin", "wb")     # La clave entre Alice y TTP
fichero_Kat.write(Kat)                  # se escribe en un fichero
fichero_Kat.close()                     # (simulando el intercambio)

Kbt = aes.crear_AESKey()

fichero_Kbt = open("KBT.bin", "wb")     # La clave entre Bob y TTP
fichero_Kbt.write(Kbt)                  # se escribe en un fichero
fichero_Kbt.close()                     # (simulando el intercambio)

# 1.2 - Escuchar conexiones
print("Esperando conexión con Alice...")
socket = SOCKET_SIMPLE_TCP('127.0.0.1', 5550)
socket.escuchar()
print("Conexión establecida.\n")

print("\tRecibiendo...")
datos_AT = socket.recibir()
mac_AT = socket.recibir()
nonce_AT = socket.recibir()
print("\tMensaje recibido.")

emisor, receptor, random = descifrar12(Kat, datos_AT, mac_AT, nonce_AT)

# 2.1 - Crear clave entre el emisor (Alice) y el receptor (Bob)
Kab = aes.crear_AESKey()

print("\tClave entre", emisor, "y", receptor, "creada.")

# 2.2 - Cifrar la clave Kab y el emisor (Alice), con la clave Kbt
mensaje = [Kab, emisor]
datos_TB, mac_TB, nonce_TB = cifrar22(Kbt, mensaje)

print("\tClave entre", emisor, "y", receptor, "cifrada.\n")

# 2.3 - Enviar
mensaje = [datos_TB, mac_TB, nonce_TB]
datos_TA, mac_TA, nonce_TA = cifrar23(random, receptor, Kat, mensaje)

print("\tRespondiendo...")
socket.enviar(datos_TA)
socket.enviar(mac_TA)
socket.enviar(nonce_TA)
print("\tMensaje enviado.\n")

# Fin del servicio del TTP
socket.cerrar()

print("Fin del servicio.")
