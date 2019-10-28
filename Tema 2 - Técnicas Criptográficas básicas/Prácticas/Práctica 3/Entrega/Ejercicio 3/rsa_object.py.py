from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pss
from Crypto.Hash import SHA256


class RSA_OBJECT:

    """Inicializa un objeto RSA, sin ninguna clave"""
    def __init__(self):
        # Nota: Para comprobar si un objeto (no) ha sido inicializado,
        # hay que hacer "if self.objeto is None:"

        self.clavePUBLICA = None
        self.clavePRIVADA = None


    """Crea un par de claves publico/privada,
    y las almacena dentro de la instancia"""
    def create_KeyPair(self):
        self.clavePRIVADA = RSA.generate(2048)
        self.clavePUBLICA = self.clavePRIVADA.publickey()


    """Guarda la clave privada self.clavePRIVADA en
    un fichero file, usando una contraseña password"""
    def save_PrivateKey(self, file, password):
        clave_cifrada = self.clavePRIVADA.export_key(passphrase=password)
        manejador = open(file, "wb")
        manejador.write(clave_cifrada)
        manejador.close()


    """Carga la clave privada self.clavePRIVADA de un
    fichero file, usando una contraseña password"""
    def load_PrivateKey(self, file, password):
        clave_cifrada = open(file, "rb").read()
        self.clavePRIVADA = RSA.import_key(clave_cifrada, passphrase=password)


    """Guarda la clave publica self.clavePUBLICA en un fichero file"""
    def save_PublicKey(self, file):
        clave_publica = self.clavePUBLICA.export_key()
        manejador = open(file, "wb")
        manejador.write(clave_publica)
        manejador.close()


    """Carga la clave publica self.clavePUBLICA de un fichero file"""
    def load_PublicKey(self, file):
        archivo = open(file, "rb").read()
        self.clavePUBLICA = RSA.import_key(archivo)


    """Cifra el parámetro datos (de tipo binario) con la clave self.clavePUBLICA,
    y devuelve el resultado. En caso de error, se devuelve None"""
    def cifrar(self, datos):
        if self.clavePUBLICA is not None:
            cifrador = PKCS1_OAEP.new(self.clavePUBLICA)

            return cifrador.encrypt(datos)

        else:
            return None


    """Descrifra el parámetro cifrado (de tipo binario) con la clave self.clavePRIVADA,
    y devuelve el resultado (de tipo binario). En caso de error, se devuelve None"""
    def descifrar(self, cifrado):
        if self.clavePRIVADA is not None:
            descifrador = PKCS1_OAEP.new(self.clavePRIVADA)

            return descifrador.decrypt(cifrado).decode("utf-8", "ignore")


    """Firma el parámetro datos (de tipo binario) con la clave self.clavePRIVADA,
    y devuelve el resultado. En caso de error, se devuelve None."""
    def firmar(self, datos):
        if self.clavePRIVADA is not None:
            hash = SHA256.new(datos)
            firma = pss.new(self.clavePRIVADA).sign(hash)

            return firma

        else:
            return None


    """Comprueba el parámetro text (de tipo binario) con respecto a una firma
    signature (de tipo binario), usando para ello la clave self.clavePUBLICA.
    Devuelve True si la comprobacion es correcta, o False en caso contrario
    o en caso de error."""
    def comprobar(self, texto, firma):
        if self.clavePUBLICA is not None:
            hash = SHA256.new(texto)
            verificador = pss.new(self.clavePUBLICA)

            try:
                verificador.verify(hash, firma)
                return True

            except (ValueError, TypeError):
                return False

        else:
            return False


# # # # # # # # # # #
# Código de prueba  #
# # # # # # # # # # #

# Crear clave RSA y guardar en ficheros
# la clave privada (protegida) y pública
password = "password"

private_file = "rsa_key.pem"
public_file = "rsa_key.pub"

RSA_key_creator = RSA_OBJECT()
RSA_key_creator.create_KeyPair()
RSA_key_creator.save_PrivateKey(private_file, password)
RSA_key_creator.save_PublicKey(public_file)

# Crea dos clases, una con la clave privada y otra con la clave publica
RSA_private = RSA_OBJECT()
RSA_public = RSA_OBJECT()

RSA_private.load_PrivateKey(private_file, password)
RSA_public.load_PublicKey(public_file)

# Cifrar y descifrar con PKCS1 OAEP
cadena = "Lo desconocido es lo contrario de lo conocido. Pasalo."
print("Mensaje: ", cadena)

cifrado = RSA_public.cifrar(cadena.encode("utf-8"))
print("Cifrado: ", cifrado, "\n")

descifrado = RSA_private.descifrar(cifrado)
print("Descifrado: ", descifrado, "\n")

# Firmar y comprobar con PKCS PSS
firma = RSA_private.firmar(cadena.encode("utf-8"))
print("Firma: ", firma.hex(), "\n")

if RSA_public.comprobar(cadena.encode("utf-8"), firma):
    print("La firma es válida")
else:
    print("La firma es inválida")
