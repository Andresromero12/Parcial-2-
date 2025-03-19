from Cliente import Cliente

class UltraSonido(Cliente): 
    def __init__(self, cedula, edad, sexo, seguro, estudio):
        super().__init__(cedula, edad, sexo, seguro, "Ultrasonido")

        