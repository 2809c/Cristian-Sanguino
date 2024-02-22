class Person:
    def __init__(self, nombre="nombre", apellido="apellido", correo="correo", telefono="telefono"):
      self.nombre = nombre
      self.apellido = apellido
      self.correo = correo
      self.telefono = telefono
      
    def Obtenerinfo(self):
      print("Mi nombre es", self.nombre, self.apellido, "Mi correo es", self.correo, "Y mi telefono es", self.telefono)