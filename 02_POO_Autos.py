class Auto:
    # La creacion de un constructor
    # REGLA DE ORO: Toda funcion dentro de una clase
    # su primer argumento es el self
    def __init__(self, marca, color, precio, combustible):
        self.marca = marca
        self.color = color
        self.precio = precio 
        self.combustible = combustible



deportivo = Auto("Mazda","Verde", "30 mil dolares", "Gasolina")
clasico = Auto("Ford","Negro", "20 mil dolares", "Disel")
sedan = Auto("Toyota", "Azul", "10 mil dolares", "Electrico")

print(f"El auto {deportivo.marca} - {deportivo.color} cuesta $ {deportivo.precio} y usa {deportivo.combustible}")
print(f"El auto {clasico.marca} -{clasico.color} cuesta $ {clasico.precio} y usa {clasico.combustible}")
print(f"El autos {sedan.marca} -{sedan.color} cuesta $ {sedan.precio} y es {sedan.combustible}")