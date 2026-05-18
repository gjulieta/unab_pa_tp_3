from src.libro import Libro

# Le pasamos los datos directamente como querías (Clonando el ejemplo de la consigna)
mi_libro = Libro(
    titulo="PROGRAMACION AVANAZADA COMISION 4",
    autor="JULIETA , GOMEZZ",
    ISBN="0-13-031997-X",
    paginas=234,
    edicion="1a. edición",
    editorial="UNIVERSIDAD DE ALMIRANTE BROWN",
    lugar="BUENOS AIRES (ARG)",
    fecha_edicion="DOMINGO 17 de MAYO de 2016"
)

#METODO PARA MOSTRAE LA INFO
mi_libro.mostrar_informacion()