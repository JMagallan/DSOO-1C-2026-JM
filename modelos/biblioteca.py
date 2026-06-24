from modelos.Prestamos import Prestamo
class Biblioteca (object):
    def __init__(self):
        self.material = []
        self.socio = []
        self.prestamo = []
        
    def prestar_material(self,material,socio,fecha_prestamo,fecha_vencimiento):
      if material.disponible == True: 
        nuevo_prestamo = Prestamo(material, socio, fecha_prestamo, fecha_vencimiento)
        self.prestamo.append(nuevo_prestamo)
        material.disponible=False
      else:

       print("Material no disponible")
        
    def devolver_material(self, titulo,socio):
       material=self.buscar_material(titulo)
       if material != None:
            material.disponible=True   
            return True 
        return False    
        
    def agregar_material(self,material):
        self.material.append(material)
        
        
    def listar_materiales(self):
        for material in self.material:
            print(material.titulo)
            
    def buscar_material(self,titulo):
        for material in self.material:
            if material.titulo.lower() == titulo.lower():
                return material
        return None
    
    def listar_disponibles(self):
        for material in self.material:
            if material.disponible == True:
                print(material.titulo)
    
    def registrar_prestamo(self,prestamo):
        self.prestamo.append(prestamo)

    def listar_prestamo(self,socio):
        for prestamo in self.prestamo:
            if prestamo.socio.id_socio == socio.id_socio:
                print(prestamo.material.titulo)
                
    def listar_prestamo_activo (self):
        for prestamo in self.prestamo:
            if prestamo.fecha_devolucion == None:
                print(prestamo.material.titulo)
                print(prestamo.socio.nombre)
                print(prestamo.fecha_vencimiento)           
    def agregar_socio(self,socio):
        self.socio.append(socio)
        
    def buscar_socio(self,id_socio):
        for socio in self.socio:
            if socio.id_socio== id_socio:
                return socio    
        return None
    