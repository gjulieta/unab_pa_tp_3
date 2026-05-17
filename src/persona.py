#CREAR LA CLASE PERSONA 
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad

    def get_nacionalidad(self):
        return self.nacionalidad
