from modelos.Biblioteca import Biblioteca
from modelos.Socios import Socio
from modelos.Libro import Libro
from modelos.Revista import Revista
def menu():

    biblioteca = Biblioteca()

    while True:

        print("1- Agregar socio")
        print("2- Agregar libro")
        print("3- Agregar revista")
        print("4- Buscar material")
        print("5- Listar materiales")
        print("6- Prestar material")
        print("7- Devolver material")
        print("8- Listar prestamos")
        print("9- Salir")
        
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            nombre=input("Nombre:")
            apellido =input("Apellido: ")
            telefono =input("Telefono: ")
            correo = input("Correo: ")
            id_socio = input("ID del socio: ")
            
            nuevo_socio = Socio(nombre,
                  apellido,
                  telefono,
                  correo,
                  id_socio)

            biblioteca.agregar_socio(nuevo_socio)

            print ("Socio agregado correctamente")
            
        elif opcion == 2:
            titulo=input("Titulo:")
            idioma =input("Idioma: ")            
            categoria =input("Categoria: ")
            disponible =True
            estado ="Disponible"
            anio =input("Anio: ")
            editorial =input("Editorial: ")
            hoja =input("Hoja: ")
            autores =input("Autores: ")
            nuevo_libro = Libro(titulo,idioma,categoria,disponible,estado,anio,editorial,hoja,autores)
            biblioteca.agregar_material(nuevo_libro)    
            
        elif opcion == 3:
            titulo=input("Titulo:")
            idioma =input("Idioma: ")            
            categoria =input("Categoria: ")
            disponible =input("Disponible: ")
            estado =input("Estado: ")
            anio =input("Anio: ")
            editorial =input("Editorial: ")
            dia =input("Dia: ")
            mes =input("Mes: ")
            numero =input("Numero: ")
            imagen_tapa =input("Imagen de la tapa: ")
            nueva_revista = Revista(titulo,idioma,categoria,disponible,estado,anio,editorial,dia,mes,numero,imagen_tapa)
            biblioteca.agregar_material(nueva_revista)
         
        elif opcion == 4:
            titulo=input("Titulo:")
            material_encontrado = biblioteca.buscar_material(titulo)
            if material_encontrado:
                material_encontrado.mostrar_info()
            else:
                print("Material no encontrado")
                
        elif opcion == 5:
            biblioteca.listar_materiales()
                    
        elif opcion == 6:
            titulo= input("Titulo del material a prestar:")
            id_socio= input("Ingrese el ID del socio:")
            
            material= biblioteca.buscar_material(titulo)
            socio= biblioteca.buscar_socio(id_socio)
            
            if material!=None and socio!=None:
                fecha_prestamo=input("Ingrese la fecha de prestamo:")
                fecha_vencimiento=input("Ingrese la fecha de vencimiento:")
                biblioteca.prestar_material(material,socio,fecha_prestamo,fecha_vencimiento)
                print ("Material prestado correctamente")
            else:
                print("Material o socio no encontrado")           
                 
        elif opcion == 7:      
            titulo= input("Titulo del material a devolver:")
            if biblioteca.devolver_material(titulo):
                print("Material devuelto correctamente")
            else:
                print("Material no encontrado") 
        
        elif opcion == 8:
            print("Estos son los prestamos activos:")
            biblioteca.listar_prestamo_activo()
         
        elif opcion == 9:
            print("Saliendo...")
            break