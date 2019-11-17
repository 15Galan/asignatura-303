from socket_class import SOCKET_SIMPLE_TCP
import funciones_aes
import json


def descifraPasos1y3(emisor, KET, t_cifrado, t_mac, t_nonce):
    """ Descifra el mensaje del paso 1/3, y devuelve los campos"""
    # Descifro los datos con AES GCM
    datos_descifrado_ET = funciones_aes.descifrarAES_GCM(KET, t_nonce, t_cifrado, t_mac)

    # Decodifica el contenido: Alice, Na
    json_ET = datos_descifrado_ET.decode("utf-8", "ignore")
    print(emisor + " -> T (descifrado): " + json_ET)
    msg_ET = json.loads(json_ET)

    # Extraigo el contenido, y lo devuelvo
    t_emisor, t_ne = msg_ET
    t_ne = bytearray.fromhex(t_ne)
    return t_emisor, t_ne


# Crear Clave KAT, guardar a fichero
KAT = funciones_aes.crear_AESKey()

FAT = open("KAT.bin", "wb")
FAT.write(KAT)
FAT.close()

# Crear Clave KBT, guardar a fichero
KBT = funciones_aes.crear_AESKey()

FBT = open("KBT.bin", "wb")
FBT.write(KBT)
FBT.close()

# Crear el socket de escucha de Bob (5551)
print("Esperando a Bob...")

socket_Bob = SOCKET_SIMPLE_TCP('127.0.0.1', 5551)
socket_Bob.escuchar()

# Crea la respuesta para B y A: K1 y K2
K1 = funciones_aes.crear_AESKey()
K2 = funciones_aes.crear_AESKey()

# Paso 1) B->T: KBT(Bob, Nb) en AES-GCM
cifrado = socket_Bob.recibir()
cifrado_mac = socket_Bob.recibir()
cifrado_nonce = socket_Bob.recibir()

_, t_nb = descifraPasos1y3("B", KBT, cifrado, cifrado_mac, cifrado_nonce)

# Paso 2) T -> B : KBT(K1, K2, Nb) en AES-GCM
# A empezar a resolver!!!!!!!
print("Comienza el paso 2 en T")

mensaje_B1 = [K1.hex(), K2.hex(), t_nb.hex()]
json_EB = json.dumps(mensaje_B1)

print(" T -> B (descifrado): " + json_EB)

motorB_AES = funciones_aes.iniciarAES_GCM(KBT)
cifrado_B1_T, mac_B1_T, nonce_B1_T = funciones_aes.cifrarAES_GCM(motorB_AES, json_EB.encode("utf-8"))

socket_Bob.enviar(cifrado_B1_T)
socket_Bob.enviar(mac_B1_T)
socket_Bob.enviar(nonce_B1_T)

# Crear el socket de escucha de Alice (5550)
print("Esperando a Alice...")

socket_Alice = SOCKET_SIMPLE_TCP('127.0.0.1', 5550)
socket_Alice.escuchar()

# Paso 3) A -> T : KAT(Alice, Na) en AES-GCM
cifrado_A = socket_Alice.recibir()
mac_A = socket_Alice.recibir()
nonce_A = socket_Alice.recibir()

_, t_na = descifraPasos1y3("A", KAT, cifrado_A, mac_A, nonce_A)

# Paso 4) T->A: KAT(K1, K2, Na) en AES-GCM
print("Comienza el paso 4 en T")

msg_a1 = [K1.hex(), K2.hex(), t_na.hex()]
json_EA = json.dumps(mensaje_B1)

print(" T -> A (descifrado): " + json_EA)

motorA_AES = funciones_aes.iniciarAES_GCM(KAT)
cifrado_A_T, mac_A_T, nonce_A_T = funciones_aes.cifrarAES_GCM(motorA_AES, json_EA.encode("utf-8"))

socket_Alice.enviar(cifrado_A_T)
socket_Alice.enviar(mac_A_T)
socket_Alice.enviar(nonce_A_T)

# T termina su trabajo :-)
socket_Bob.cerrar()
socket_Alice.cerrar()
