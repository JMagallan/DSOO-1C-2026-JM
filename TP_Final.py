class IDError (Exception):
    pass
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
            

class Libro (Material):
    def __init__(self, titulo, idioma, categoria,disponible,estado,anio,editorial,hoja,autores):
        super().__init__(titulo, idioma, categoria,disponible,estado,anio,editorial)
        self.hoja = hoja
        self.autores = autores
        
class Revista (Material):
    def __init__(self, titulo, idioma, categoria,disponible,estado,anio,editorial,dia,mes,numero,imagen_tapa):
        super().__init__(titulo, idioma, categoria,disponible,estado,anio,editorial)
        self.dia = dia
        self.mes = mes
        self.numero = numero
        self.imagen_tapa = imagen_tapa

libro1 = Libro("El Señor de los Anillos","Español", "Literatura",True,"Disponible",2020,"Editorial 1",300,"JRR Tolkien")
print(libro1.id)
libro2 = Libro("El Señor de los Anillos","Español", "Literatura",True,"Disponible",2020,"Editorial 1",300,"JRR Tolkien")
print(libro2.id)

revista=Revista("caras","Español", "Literatura",True,"Disponible",2020,"Editorial 1",20,10,1,"imagen")
print(revista.id)
revista2=Revista("caras","Español", "Literatura",True,"Disponible",2020,"Editorial 1",20,10,1,"imagen")
print(revista2.id)