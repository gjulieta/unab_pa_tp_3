#NIVEL 4 / CREAR LA CLASE LIBRO
from src.persona import Persona

class Libro:
    
    def __init__(self, titulo="", autor=None, ISBN="", paginas=0, edicion="", editorial="", lugar="", fecha_edicion=""):
        self.titulo = titulo
        
        # TRUCO CLAVE: Si lo que nos pasaron es un texto (str), fabricamos la Persona acá adentro
        if isinstance(autor, str):
            self.autor = Persona(autor)
        else:
            self.autor = autor if autor is not None else Persona("")
            
        self.ISBN = ISBN    
        self.paginas = paginas
        self.edicion = edicion
        self.editorial = editorial
        self.lugar = lugar
        self.fecha_edicion = fecha_edicion

    def get_titulo(self):
        return self.titulo
    def get_autor(self):
        return self.autor
    def get_ISBN(self):
        return self.ISBN
    def get_paginas(self):
        return self.paginas
    def get_edicion(self):
        return self.edicion
    def get_editorial(self):
        return self.editorial
    def get_lugar(self):
        return self.lugar
    def get_fecha_edicion(self):
        return self.fecha_edicion
    
    def set_titulo(self, titulo):
        self.titulo = titulo
    def set_autor(self, autor):
        self.autor = autor
    def set_ISBN(self, ISBN):
        self.ISBN = ISBN
    def set_paginas(self, paginas):
        self.paginas = paginas
    def set_edicion(self, edicion):
        self.edicion = edicion
    def set_editorial(self, editorial):
        self.editorial = editorial
    def set_lugar(self, lugar):
        self.lugar = lugar
    def set_fecha_edicion(self, fecha_edicion):
        self.fecha_edicion = fecha_edicion

    def leer_informacion(self):
        print("--- Leyendo información del Libro ---")
        self.titulo = input("Ingrese el título: ")
        
        nombre_autor = input("Ingrese el nombre del autor: ")
        self.autor = Persona(nombre_autor) # Guardamos el objeto Persona
        
        self.ISBN = input("Ingrese el ISBN: ")
        self.paginas = int(input("Ingrese la cantidad de páginas: "))
        self.edicion = input("Ingrese la edición (ej: 3a. edición): ")
        self.editorial = input("Ingrese la editorial: ")
        self.lugar = input("Ingrese el lugar (Ciudad y País): ")
        self.fecha_edicion = input("Ingrese la fecha de edición: ")

    
    def mostrar_informacion(self):
        print(f"Título: {self.titulo} {self.edicion}")
        print(f"Autor: {self.autor.nombre}")
        print(f"ISBN: {self.ISBN}")
        print(f"{self.editorial}, {self.lugar}")
        print(f"{self.fecha_edicion}")
        print(f"{self.paginas} páginas")