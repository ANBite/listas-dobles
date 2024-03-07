class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.nodo_anterior = None
        self.nodo_siguiente = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.nodo_siguiente = self.cabeza
            self.cabeza.nodo_anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

    def agregar_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cola is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.nodo_siguiente = nuevo_nodo
            nuevo_nodo.nodo_anterior = self.cola
            self.cola = nuevo_nodo

    def eliminar(self, valor):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.valor == valor:
                if nodo_actual == self.cabeza:
                    self.cabeza = nodo_actual.nodo_siguiente
                    if self.cabeza is not None:
                        self.cabeza.nodo_anterior = None
                elif nodo_actual == self.cola:
                    self.cola = nodo_actual.nodo_anterior
                    if self.cola is not None:
                        self.cola.nodo_siguiente = None
                else:
                    nodo_actual.nodo_anterior.nodo_siguiente = nodo_actual.nodo_siguiente
                    nodo_actual.nodo_siguiente.nodo_anterior = nodo_actual.nodo_anterior
                return
            nodo_actual = nodo_actual.nodo_siguiente

    def recorrer_adelante(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(nodo_actual.valor)
            nodo_actual = nodo_actual.nodo_siguiente

    def recorrer_atras(self):
        nodo_actual = self.cola
        while nodo_actual is not None:
            print(nodo_actual.valor)
            nodo_actual = nodo_actual.nodo_anterior

    def previous(self):
        if self.cola is None:
            raise StopIteration("No hay elementos en la lista")

        data = self.cola.valor
        self.cola = self.cola.nodo_anterior
        if self.cola is None:
            raise StopIteration("Llegaste al inicio de la lista")

        return data

# Ejemplo de uso
lista = ListaDoblementeEnlazada()
lista.agregar_inicio(1)
lista.agregar_inicio(2)
lista.agregar_final(3)
print("Recorriendo hacia adelante:")
lista.recorrer_adelante()  # Salida esperada: 2, 1, 3
print("Recorriendo hacia atrás:")
try:
    while True:
        print(lista.previous())
except StopIteration as e:
    print(e)

