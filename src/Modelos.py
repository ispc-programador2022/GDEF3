SIN_DESC = "S/D"

class AtributosComunes:
    def __init__(self, alto = SIN_DESC, ancho = SIN_DESC, color = SIN_DESC, 
                garantia = SIN_DESC, origen = SIN_DESC, peso = SIN_DESC, 
                profundidad = SIN_DESC):
        self.alto = alto
        self.ancho = ancho
        self.color = color
        self.garantia = garantia
        self.origen = origen
        self.peso = peso
        self.profundidad = profundidad
                
class CaracteristicasTelefonos:
    def __init__(self, ram = SIN_DESC, bluetooth = SIN_DESC, camPpal = SIN_DESC, 
                camFrontal = SIN_DESC, procesador = SIN_DESC, 
                almacenamiento = SIN_DESC, radio = SIN_DESC, 
                tamanioPantalla = SIN_DESC, tipoPantalla = SIN_DESC, 
                capacidadBateria = SIN_DESC, gps = SIN_DESC, so = SIN_DESC, 
                usb = SIN_DESC, wifi = SIN_DESC):
        self.ram = ram
        self.bluetooth = bluetooth
        self.camPpal = camPpal
        self.camFrontal = camFrontal
        self.procesador = procesador
        self.almacenamiento = almacenamiento
        self.radio = radio
        self.tamanioPantalla = tamanioPantalla
        self.tipoPantalla = tipoPantalla
        self.capacidadBateria = capacidadBateria
        self.gps = gps
        self.so = so
        self.usb = usb
        self.wifi = wifi
    
class Celular:
    def __init__(self, marca, nombre, codigo = 0, precio = 0, 
                atributosComunes = AtributosComunes(),
                caracteristicasTelefono = CaracteristicasTelefonos()):
        self.marca = marca
        self.nombre = nombre
        self.codigo = codigo
        self.precio = precio
        self.atributosComunes = atributosComunes
        self.caracteristicasTelefono = caracteristicasTelefono
    
    def __str__(self) -> str:
        return f"""{self.nombre}, {self.marca}, {self.precio}."""
