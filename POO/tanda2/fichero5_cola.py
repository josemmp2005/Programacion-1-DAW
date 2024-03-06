"""
Crea una clase que represente una estructura de datos tipo pila (stack) y otra tipo cola (queue).

La pila y la cola permitirán estas operaciones:

- Crear la pila o la cola con o sin valores iniciales o a partir de otra cola o pila.
- Obtener el número de elementos almacenados (tamaño).
- Saber si la pila o la cola está vacía.
- Vaciar completamente la pila o la cola.

Para el caso de la pila:
- Apilar (push): se añade un elemento a la pila. Se añade al principio de esta.
- Desapilar (pop): se saca (debe devolverse) un elemento de la pila y se elimina.
- Leer el elemento superior de la pila sin retirarlo (top).

Para el caso de la cola:
- Encolar (enqueue): se añade un elemento a la cola. Se añade al final de esta.
- Desencolar (dequeue): se saca (debe devolverse) y se elimina el elemento frontal de la cola, es decir, el primer
elemento que entró.
- Leer el elemento frontal de la cola, es decir, el primer elemento que entró, sin retirarlo (front).
"""


class Queue:
    def __init__(self, *params):
        self.__value = list(params)

    @property
    def value(self):
        return self.__value

    def __str__(self):
        return str(self.__value)

    def length(self):
        return len(self.__value)

    def is_empty(self):
        if len(self.__value) <= 0:
            return True
        else:
            return False

    def empty(self):
        self.__value = []

    def enqueue(self, element):
        self.__value.append(element)

    def dequeue(self):
        return self.__value.pop(0)

    def front(self):
        return self.__value[0]
