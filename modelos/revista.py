from Materiales import Material
class Revista (Material):
    def __init__(self, titulo, idioma, categoria,disponible,estado,anio,editorial,dia,mes,numero,imagen_tapa):
        super().__init__(titulo, idioma, categoria,disponible,estado,anio,editorial)
        self.dia = dia
        self.mes = mes
        self.numero = numero
        self.imagen_tapa = imagen_tapa
        
    def mostrar_info (self):
         Material.mostrar_info(self)
         print(self.numero)
              