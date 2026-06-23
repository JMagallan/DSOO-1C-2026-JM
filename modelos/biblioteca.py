from modelos.Prestamos import prestamo

class Biblioteca (object):
    def __init__(self):
        self.materiales = []
        self.socios = []
        self.prestamos = []
        
        
    def agregar_material(self,material):
        self.materiales.append(material)
        
        
    def listar_materiales(self):
        for material in self.materiales:
            print(material.titulo)
            
    def buscar_material(self,titulo):
        for material in self.materiales:
            if material.titulo.lower() == titulo.lower():
                return material
        return None
    
    def listar_disponibles(self,material):
        for material in self.materiales:
            if material.disponible == True:
                print(material.titulo)
    
    def registrar_prestamo(self,prestamo):
        self.prestamos.append(prestamo)

    def listar_prestamo(self,socio):
        for prestamo in self.prestamos:
            if prestamo.id_socio == socio.id_socio:
                print(prestamo.id_material)
                
    def agregar_socio(self,socio):
        self.socios.append(socio)