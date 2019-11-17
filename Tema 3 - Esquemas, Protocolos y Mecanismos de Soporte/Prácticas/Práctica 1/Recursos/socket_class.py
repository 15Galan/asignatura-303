"""
Clase de ejemplo para el envio y la recepcion de mensajes en un canal TCP
No utilizar en un entorno de produccion
"""

import socket
import struct
import sys

class SOCKET_SIMPLE_TCP:

    def __init__(self, host, puerto):
        """Inicializa un objeto socket TCP, proporcionando un host y a un puerto"""
        self.host = host
        self.puerto = puerto
        self.server = None

    def conectar(self):
        """Convierte el objeto socket en un cliente, y se conecta a un servidor"""
        self.socket = socket.create_connection((self.host, self.puerto))

    def escuchar(self):
        """Convierte el objeto socket en un servidor, y recibe la peticion de un cliente"""
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (self.host, self.puerto)
        self.server.bind(server_address)
        self.server.listen(1)
        self.socket, dir_cliente = self.server.accept()
        return dir_cliente

    def __recvall(self, count):
        """PRIVADO: Recibe "count" bytes del buffer de entrada"""
        buffer = b''
        while count:
            # Puede que no reciba "count", asi que tengo que leer hasta recibirlo todo
            newbuf = self.socket.recv(count)
            if not newbuf: return None
            buffer += newbuf
            count -= len(newbuf)
        return buffer

    def enviar(self, datos):
        """Envia un array de bytes "datos" del origen al destino."""
        longitud = len(datos)
        self.socket.sendall(struct.pack('!I', longitud)) # unsigned int en formato de red(!)
        self.socket.sendall(datos)

    def recibir(self):
        """Recibe un array de bytes "datos" del destino al destino."""
        lenbuf = self.__recvall(4)
        longitud, = struct.unpack('!I', lenbuf)
        return self.__recvall(longitud)

    def cerrar(self):
        """Cierra la conexion"""
        if self.socket != None:
            self.socket.close()
        if self.server != None:
            self.server.close()

