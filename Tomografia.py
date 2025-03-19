from Cliente import Cliente

class Tomografia(Cliente): 
    def __init__(self, cedula, edad, sexo, seguro, estudio):
        super().__init__(cedula, edad, sexo, seguro,"Tomografía")

        