class Prestamo (object):
    def __init__(self,material,socio,fecha_prestamo,fecha_vencimiento):
        self.material = material
        self.socio = socio
        self.fecha_prestamo = fecha_prestamo
        self.fecha_vencimiento = fecha_vencimiento
        self.fecha_devolucion = None