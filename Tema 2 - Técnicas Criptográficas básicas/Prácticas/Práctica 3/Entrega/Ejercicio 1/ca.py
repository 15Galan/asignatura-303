import CodeA

# Apartado a)
clave_ALICE = CodeA.crear_RSAKey()

CodeA.guardar_RSAKey_Publica("Alice.pub", clave_ALICE)
CodeA.guardar_RSAKey_Privada("Alice.pri", clave_ALICE, "12345")

# Apartado b)
clave_BOB = CodeA.crear_RSAKey()

CodeA.guardar_RSAKey_Publica("Bob.pub", clave_BOB)
CodeA.guardar_RSAKey_Privada("Bob.pri", clave_BOB, "54321")
