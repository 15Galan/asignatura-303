import CodeA

# Apartado c)
clave_pri_ALICE = CodeA.cargar_RSAKey_Privada("Alice.pri", "12345")
clave_pub_BOB = CodeA.cargar_RSAKey_Privada("Bob.pub", "54321")

# Apartado d)
mensaje = "Hola amigos de la seguridad"

cifrado = CodeA.cifrarRSA_OAEP(mensaje, clave_pub_BOB)

# Apartado e)
firma = CodeA.firmarRSA_PSS(mensaje, clave_pri_ALICE)

# Apartado f)
manejador_cifrado = open("Texto cifrado.txt", "wb")
manejador_cifrado.write(cifrado)
manejador_cifrado.close()

manejador_firma = open("Firma.txt", "wb")
manejador_firma.write(firma)
manejador_firma.close()
