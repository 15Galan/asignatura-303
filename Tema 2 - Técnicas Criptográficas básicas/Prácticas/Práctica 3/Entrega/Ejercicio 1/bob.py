import CodeA

# Apartado g)
clave_pri_BOB = CodeA.cargar_RSAKey_Privada("Bob.pri", "54321")
clave_pub_ALICE = CodeA.cargar_RSAKey_Publica("Alice.pub")

# Apartado h)
cifrado = open("Texto cifrado.txt", "rb").read()
firma = open("Firma.txt", "rb").read()

# Apartado i)
descifrado = CodeA.descifrarRSA_OAEP(cifrado, clave_pri_BOB)
print("Mensaje descifrado: " + descifrado)

# Apartado j)
verificacion = CodeA.comprobarRSA_PSS(descifrado, firma, clave_pub_ALICE)
print("La firma es correcta: " + str(verificacion))
