from modelos.prestamos import prestamo

class Biblioteca (object):
    def __init__(self):
        self.materiales = []
        self.socios = []
        self.prestamos = []
        
        
    def agregar_material(self,material):
        self.materiales.append(material)
        
    def agregar_socio(self,socio):
        self.socios.append(socio)
        
    def listar_materiales(self):
        for material in self.materiales:
            print(material.titulo)
            
    def buscar_material(self,titulo):
        for material in self.materiales:
            if material.titulo.lower() == titulo.lower():
                return material
        return None
    
    def devolver_material(self, titulo):
        i = 0

        while i < len(self.materiales):
         material_devuelto = self.materiales[i]

        if material_devuelto.titulo.lower() == titulo.lower():
                if not material_devuelto.disponible:
                 material_devuelto.disponible = True
                return True

        i += 1

        return False    
    
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