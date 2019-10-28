from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

# Ver https://pycryptodome.readthedocs.io/en/latest/src/public_key/ecc.html
# Ver https://pycryptodome.readthedocs.io/en/latest/src/signature/dsa.html

def crear_ECCKey():
    # Use 'NIST P-256'

    return key


def guardar_ECCKey_Privada(fichero, key, password):
    # ...


def cargar_ECCKey_Privada(fichero, password):
    # ...

    return key


def guardar_ECCKey_Publica(fichero, key):
    # ...


def cargar_ECCKey_Publica(fichero):
    # ...

    return key_pub


def cifrarECC_OAEP(cadena, key):
    # El cifrado con ECC (ECIES) aun no está implementado
    # Por lo tanto, no se puede implementar este método aun en la versión 3.9.0

    return cifrado


def descifrarECC_OAEP(cifrado, key):
    # El cifrado con ECC (ECIES) aun no está implementado
    # Por lo tanto, no se puede implementar este método aun en la versión 3.9.0

    return cadena


def firmarECC_PSS(texto, key_private):
    # ...

    return signature


def comprobarECC_PSS(texto, firma, key_public):
    # ...

    try:
        # ...

        return True

    except (ValueError, TypeError):
        return False
