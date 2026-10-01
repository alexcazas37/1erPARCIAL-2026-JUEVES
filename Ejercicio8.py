from datetime import date

class Nodo:
    def __init__(self, dato=None, prox=None):
        self.dato = dato
        self.prox = prox

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def append(self, dato):
        nuevo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo
            return
        actual = self.cabeza
        while actual.prox:
            actual = actual.prox
        actual.prox = nuevo

    def remover(self, dato):
        actual, anterior = self.cabeza, None
        while actual:
            if actual.dato == dato:
                if anterior:
                    anterior.prox = actual.prox
                else:
                    self.cabeza = actual.prox
                return True
            anterior, actual = actual, actual.prox
        return False

    def __iter__(self):
        actual = self.cabeza
        while actual:
            yield actual.dato
            actual = actual.prox


class KwikEMart:
    def __init__(self):
        self.pasillos = {"Bebidas": ListaEnlazada(),
                         "Snacks": ListaEnlazada(),
                         "Conveniencia": ListaEnlazada()}

    def agregar_producto(self, pasillo, producto):
        if pasillo in self.pasillos:
            self.pasillos[pasillo].append(producto)

    def remover_producto(self, pasillo, id_producto):
        for p in self.pasillos.get(pasillo, []):
            if p.id_producto == id_producto:
                self.pasillos[pasillo].remover(p)
                return

    def actualizar_stock(self, pasillo, id_producto, nuevo_stock):
        for p in self.pasillos.get(pasillo, []):
            if p.id_producto == id_producto:
                p.stock = nuevo_stock

    def desechar_proximos_a_expirar(self):
        hoy = date.today()
        for lista in self.pasillos.values():
            a_desechar = [p for p in lista
                          if (p.fecha_vencimiento - hoy).days <= 1]
            for p in a_desechar:
                print(f"Desechando: {p.descripcion}")
                lista.remover(p)