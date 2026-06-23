from modelos.Prestamos import Prestamo
from Materiales import Material
class Biblioteca (object):
    def __init__(self):
        self.Material = []
        self.Socio = []
        self.Prestamo = []
        
    def prestar_material(self,Material,socio):
      if Material.disponible == True: 
        nuevo_prestamo = Prestamo(Material, socio, Prestamo.fecha_prestamo, Prestamo.fecha_devolucion, prestamo.fecha_vencimiento)
        self.Prestamo.append(nuevo_prestamo)
        Material.disponible=False
      else:

       print("Material no disponible")
        
    def devolver_material(self, titulo):
        i = 0

        while i < len(self.Material):
         material_devuelto = self.Material[i]

        if material_devuelto.titulo.lower() == titulo.lower():
                if not material_devuelto.disponible:
                 material_devuelto.disponible = True
                return True

        i += 1

        return False       
        
    def agregar_material(self,material):
        self.Material.append(material)
        
        
    def listar_materiales(self):
        for Material in self.Material:
            print(Material.titulo)
            
    def buscar_material(self,titulo):
        for material in self.Material:
            if material.titulo.lower() == titulo.lower():
                return material
        return None
    
    def listar_disponibles(self,material):
        for Material in self.Material:
            if Material.disponible == True:
                print(material.titulo)
    
    def registrar_prestamo(self,prestamo):
        self.Prestamo.append(prestamo)

    def listar_prestamo(self,socio):
        for prestamo in self.Prestamo:
            if prestamo.id_socio == socio.id_socio:
                print(prestamo.id_material)
                
    def agregar_socio(self,socio):
        self.Socio.append(socio)
        
    def buscar_socio(self,id_socio):
        for socio in self.socios:
            if socio.id_socio== id_socio:
                return socio    