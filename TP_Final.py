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

class socio (object):
    def __init__(self,nombre,apellido,telefono,correo,id_socio):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.id_socio = id_socio
        
    def __reservar__ (self,material):
        if  matrial.disponible == True:
            material.disponible = False
            print("Material reservado")
        else:
            print("Material no disponible")
           

class prestamo (object):
    def __init__(self,id_material,id_socio,fecha_prestamo,fecha_devolucion,fecha_vencimiento):
        self.id_material = id_material
        self.id_socio = id_socio
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.fecha_vencimiento = fecha_vencimiento