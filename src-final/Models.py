class Tipo:
    def __init__(self, tipo):
        self.tipo = tipo

    def __str__(self) -> str:
        return self.tipo.capitalize()
                
class Marca:
    def __init__(self, marca):
        self.marca = marca
    
    def __str__(self) -> str:
        return self.marca.capitalize()
    
class Panial:
    def __init__(self, marca, tipo, tamanio, cantidad, precio):
        self.marca = Marca(marca)
        self.tipo = Tipo(tipo)
        self.tamanio = tamanio
        self.cantidad = cantidad
        self.precio = precio
    
    def getPrecioPorUnidad(self) -> float:
        precioPorUn = float(self.precio) / int(self.cantidad)
        return f"{precioPorUn:.2f}"

    def __str__(self) -> str:
        return f"""{self.marca} - {self.tipo} - {self.tamanio}.
        {self.cantidad} unidades
        $ {self.precio}
        Precio por unidad: $ {self.getPrecioPorUnidad()}"""
    
    def listarContenido(self):
        return [self.marca, self.tipo, self.tamanio, self.cantidad, self.precio, self.getPrecioPorUnidad()]