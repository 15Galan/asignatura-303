from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES

def crear_AESKey():
    """Devuelve un número aleatorio de 16 bytes - 128 bits"""
    return get_random_bytes(16)

def iniciarAES_GCM(key_16):
    """Inicia el engine de cifrado AES CTR"""
    nonce_16 = get_random_bytes(16)
    aes_cifrado = AES.new(key_16, AES.MODE_GCM, nonce = nonce_16, mac_len = 16)
    return aes_cifrado

def cifrarAES_GCM(aes_cifrado, datos):
    """Cifra el parametro datos (de tipo array de bytes), y devuelve el texto cifrado binario Y el mac Y el nonce """
    # En escenarios reales, el objeto AES se inicializa una vez, y luego vamos llamando a aes_cifrado
    datos_cifrado, mac_cifrado = aes_cifrado.encrypt_and_digest(datos)
    return datos_cifrado, mac_cifrado, aes_cifrado.nonce

def descifrarAES_GCM(key_16, nonce_16, datos, mac):
    """Descifra el parametro datos (de tipo binario), y devuelve los datos descrifrados de tipo array de bytes.
       También comprueba si el mac es correcto"""
    try:
        aes_descifrado = AES.new(key_16, AES.MODE_GCM, nonce = nonce_16)
        datos_claro = aes_descifrado.decrypt_and_verify(datos, mac)
        return datos_claro
    except (ValueError, KeyError) as e:
        return False
        
def iniciarAES_CTR(key_16):
    """Inicia el engine de cifrado AES CTR"""
    nonce_16 = get_random_bytes(8) # nonce aleatorio de 64 bits
                                   # --64 nonce--|--64 contador--
    ctr_16 = 0                     # contador, empezando desde 0
    aes_cifrado = AES.new(key_16, AES.MODE_CTR, nonce = nonce_16, initial_value = ctr_16)
    return aes_cifrado

def cifrarAES_CTR(aes_cifrado, datos):
    """Cifra el parametro datos (de tipo array de bytes), y devuelve el texto cifrado binario Y el mac"""
    # En escenarios reales, el objeto AES se inicializa una vez, y luego vamos llamando a aes_cifrado
    datos_cifrado = aes_cifrado.encrypt(datos)
    return datos_cifrado, aes_cifrado.nonce

def descifrarAES_CTR(key_16, nonce_16, datos):
    """Descifra el parametro datos (de tipo binario), y devuelve los datos descrifrados de tipo array de bytes"""
    aes_descifrado = AES.new(key_16, AES.MODE_CTR, nonce = nonce_16)
    datos_claro = aes_descifrado.decrypt(datos)
    return datos_claro