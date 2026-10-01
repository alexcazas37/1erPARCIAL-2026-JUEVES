def __str__(self):
        return (f"Producto: {self.descripcion} | ID: {self.id_producto} "
                f"| Precio: ${self.precio:.2f} | Stock: {self.stock}")

    def __eq__(self, otro):
        if not isinstance(otro, ProductoKwikE):
            return False
        return (self.id_producto == otro.id_producto
                and self.descripcion == otro.descripcion)