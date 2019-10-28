class RSA_OBJECT:

    def __init__(self):
        """Inicializa un objeto RSA, sin ninguna clave"""
        # Nota: Para comprobar si un objeto (no) ha sido inicializado, hay
        # que hacer "if self.clavePUBLICA is None:"


    def create_KeyPair(self):
        """Crea un par de claves publico/privada,
        y las almacena dentro de la instancia"""


    def save_PrivateKey(self, file, password):
        """Guarda la clave privada self.clavePRIVADA en un fichero file,
        usando una contraseña password"""


    def load_PrivateKey(self, file, password):
        """Carga la clave privada self.clavePRIVADA de un fichero file,
        usando una contraseña password"""


    def save_PublicKey(self, file):
        """Guarda la clave publica self.clavePUBLICA en un fichero file"""


    def load_PublicKey(self, file):
        """Carga la clave publica self.clavePUBLICA de un fichero file"""


    def cifrar(self, datos):
        """Cifra el parámetro datos (de tipo binario) con la clave self.clavePUBLICA,
        y devuelve el resultado. En caso de error, se devuelve None"""


    def descifrar(self, cifrado):
        """Descrifra el parámetro cifrado (de tipo binario) con la clave self.clavePRIVADA,
        y devuelve el resultado (de tipo binario). En caso de error, se devuelve None"""


    def firmar(self, datos):
        """Firma el parámetro datos (de tipo binario) con la clave self.clavePRIVADA,
        y devuelve el resultado. En caso de error, se devuelve None."""


    def comprobar(self, text, signature):
        """Comprueba el parámetro text (de tipo binario) con respecto a una firma
        signature (de tipo binario), usando para ello la clave self.clavePUBLICA.
        Devuelve True si la comprobacion es correcta, o False en caso contrario
        o en caso de error."""
