
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


    def mostrar_info (self):
        print (self.titulo) 
        print (self.idioma)
        print (self.categoria)
        print (self.disponible)
        print (self.estado)
        print (self.anio)
        print (self.editorial)
