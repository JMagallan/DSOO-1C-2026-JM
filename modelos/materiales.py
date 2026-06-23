
class Material (object):
    contador_id = 0
    def __init__(self,titulo, idioma, categoria,disponible,estado,anio,editorial):
        self.titulo = titulo
        self.idioma = idioma
        self.categoria = categoria
        self.disponible = disponible
        self.estado = estado
        self.anio = anio
        self.editorial = editorial
        
        Material.contador_id += 1
        self.id = Material.contador_id



    def prestar_material(self,material,socio):
        prestamo = Prestamos(material, socio, prestamo.fecha_prestamo, prestamo.fecha_devolucion, prestamo.fecha_vencimiento)
        self.prestamos.append(prestamo)
        material.dispoible=False
    
        
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