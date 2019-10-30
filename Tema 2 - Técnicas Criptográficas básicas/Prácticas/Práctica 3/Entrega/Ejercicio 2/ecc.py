from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

# Ver https://pycryptodome.readthedocs.io/en/latest/src/public_key/ecc.html
# Ver https://pycryptodome.readthedocs.io/en/latest/src/signature/dsa.html


def crear_ECCKey():
    # Usa 'NIST P-256'

    return ECC.generate(curve="P-256")


def guardar_ECCKey_Privada(fichero, key, password):
    clave_cifrada = key.export_key(passphrase=password, pcks=8, protecction="PBKDF2WithHMAC-SHA1AndAES128-CBC")
    manejador = open(fichero, "wt")
    manejador.write(clave_cifrada)
    manejador.close()


def cargar_ECCKey_Privada(fichero, password):
    clave_cifrada = open(fichero, "rt").read()
    clavePRIVADA = ECC.import_key(clave_cifrada, passphrase=password)

    return clavePRIVADA


def guardar_ECCKey_Publica(fichero, key):
    clave_publica = key.publickey().export_key()
    manejador = open(fichero, "wt")
    manejador.write(clave_publica)
    manejador.close()


def cargar_ECCKey_Publica(fichero):
    clave_fichero = open(fichero, "rt").read()
    clavePUBLICA = ECC.import_key(clave_fichero)    # (...).clavePUBLICA()

    return clavePUBLICA


# def cifrarECC_OAEP(cadena, key):
#     # El cifrado con ECC (ECIES) aun no está implementado
#     # Por lo tanto, no se puede implementar este método aun en la versión 3.9.0
#
#
#     return cifrado
#
#
# def descifrarECC_OAEP(cifrado, key):
#     # El cifrado con ECC (ECIES) aun no está implementado
#     # Por lo tanto, no se puede implementar este método aun en la versión 3.9.0
#
#     return cadena


def firmarECC_PSS(texto, key_private):
    hash = SHA256.new(texto.encode("utf-8"))
    print(hash.hexdigest())
    firmador = DSS.new(key_private, "fips-186-3")
    firma = firmador.sign(hash)

    return firma


def comprobarECC_PSS(texto, firma, key_public):
    hash = SHA256.new(texto)
    verificador = DSS.new(key_public, "fips-186-3")

    try:
        verificador.verify(hash, firma)

        return True

    except (ValueError, TypeError):
        return False
