from datetime import date

class KwikEMart:
    def __init__(self):
        self.pasillos = {"Bebidas": [], "Snacks": [], "Conveniencia": []}

    def agregar_producto(self, pasillo, producto):
        if pasillo in self.pasillos:
            self.pasillos[pasillo].append(producto)

    def remover_producto(self, pasillo, id_producto):
        if pasillo in self.pasillos:
            self.pasillos[pasillo] = [p for p in self.pasillos[pasillo]
                                      if p.id_producto != id_producto]

    def actualizar_stock(self, pasillo, id_producto, nuevo_stock):
        for p in self.pasillos.get(pasillo, []):
            if p.id_producto == id_producto:
                p.stock = nuevo_stock

    def buscar_por_id(self, id_producto):
        for lista in self.pasillos.values():
            for p in lista:
                if p.id_producto == id_producto:
                    return p
        return None

    def desechar_proximos_a_expirar(self):
        hoy = date.today()
        for pasillo, lista in self.pasillos.items():
            vigentes = []
            for p in lista:
                if (p.fecha_vencimiento - hoy).days > 1:
                    vigentes.append(p)
                else:
                    print(f"Desechando: {p.descripcion}")
            self.pasillos[pasillo] = vigentes