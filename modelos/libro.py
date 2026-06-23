from Materiales import Material
class Libro (Material):
    def __init__(self, titulo, idioma, categoria,disponible,estado,anio,editorial,hoja,autores):
        super().__init__(titulo, idioma, categoria,disponible,estado,anio,editorial)
        self.hoja = hoja
        self.autores = autores
        
    def mostrar_info (self):
         Material.mostrar_info(self)
         print(self.titulo)
         print(self.disponible)   