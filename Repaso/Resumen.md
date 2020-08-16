# Algoritmos Simétricos

## Ventajas y desventajas de los algoritmos simétricos
### Ventajas
* Alcanzan un alto rendimiento.
* Pueden componerse para producir mejores cifrados.
* Pueden usarse como base para otros mecanismos criptográficos (funciones hash, generadores...).
* Necesitan claves relativamente cortas

### Desventajas
* Usuarios de la misma comunicación deben usar la misma clave.
* Las redes grandes requieren tantas claves como comunicaciones.



## Algoritmo DES
Cifrado simétrico.
* Bloques de texto en claro de 64 bits.
* Bloques de texto cifrado de 64 bits.
* Clave de 64 bits (56 bits efectivos).

Diseñado por IBM como propuesta a un estándar para cifrado de datos en transmisión y en almacenamiento.

Partió de Lucifer, un algoritmo basado en la red de Feistel.

Este algoritmo consta de 16 etapas y en cada una de ellas usa una subclave generada a partir de la clave inicial.

### Variantes
* **Triple DES ó 3DES:** La etapa DES se ejecuta 3 veces, cada una con una clave distinta.
* **3DES con 2 claves:** La clave 1 y 3 son la misma.



## Efecto avalancha
Cambios pequeños en el texto en claro o en la clave producen cambios significativos en el texto cifrado.

Deriva de la tesis de Claude Shannon, en la que se definen los conceptos:
* Difusión: Cada carácter del texto cifrado debe depender de diferentes partes de la clave.
* Confusión: La relación entre el texto cifrado y la clave debe ser lo más complicada posible.



## Algoritmo AES
Cifrado simétrico.

* Bloques de texto en claro de 128 bits.
* Bloques de texto cifrado de 128 bits.
* Clave de 128 / 192 / 256 bits.

Fue publicado por NIST como el estándar de cifrado simétrico en bloque para sustituir al algoritmo DES.

Este algoritmo usa una red de sustitución-permutación, cuyo número de etapas varía según la longitud de la clave inicial...
* 128 bits -> 10 etapas.
* 192 bits -> 12 etapas.
* 256 bits -> 14 etapas.

...y cada etapa del algoritmo consta de 4 funciones:
* Sustitución de byte.
* Permutación.
* Operaciones aritméticas.
* Operación XOR.



## Modos de operación para algoritmos simétricos
Un modo de operación es una técnica que mejora el resultado final de un algoritmo criptográfico, modificando la forma en la que se opera con los bloques de datos.

NIST ha definido 5 modos de operación compatibles con cualquier algoritmo simétrico (DES, 3DES, AES...).
* **E.C.B** - Electronic Codebook
* **C.B.C** - Cipher Block Chaining
* **C.F.B** - Cipher Feedback
* **O.F.B** - Output Feedback
* **C.T.R** - Counter
