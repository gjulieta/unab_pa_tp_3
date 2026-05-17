from src.punto import Punto

# Creamos un punto de prueba
p1 = Punto(5, -3)

# Probamos los métodos que programaste
print("X es:", p1.eje_x())
print("Y es:", p1.eje_y())
print("Formateado:", p1.impresion())

# Probamos el opuesto
p_opuesto = p1.opuesto()
print("Su opuesto es:", p_opuesto.impresion())