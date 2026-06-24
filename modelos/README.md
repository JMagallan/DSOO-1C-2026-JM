# Sistema de gestion de Biblioteca

Trabajo de Diseño de sistemas orientado a objetos 

## Funcionalidades
- Alta de socio
- Alta libro
- Alta de revista
- Busqueda de material
- Listar materiales
- Registrar un prestamo
- Devolver un material
- Listar un prestamo

## Estructura del proyecto

- modelos
    biblioteca.py
    Biblioteca.py
    Materiales.py
    Libro.py
    Revista.py
    Prestamos.py
    Socios.py
    Menu.py
    Main.py

- Diagrama poo.drawio

## decisiones de diseño 

- Se utlizo una clase base "Material"
- Las clases "Libro" y "Revista" heredan de material 
- La clase "Biblioteca" centraliza la gestion de materiales socios y prestamos
- La clase "Prestamo" relaciona un material con un socio 
- Se aplican los conceptos de encapsulacion, herencia y asociacion 

## Ejecucion
ubicarse dentro de la carpeta del proyecto y ejecutar  el archivo Main.py

## Autor

- Joel Magallan
- Diseño de sistemas orientado a objetos 
- 24/06/2026

