from Cliente import Cliente
from UltraSonido import UltraSonido
from Tomografia import Tomografia
from Resonancia import Resonancia

def main(): 
    cliente = []

def agregar_cliente(): 
    cedula = int(input("Introduzca su número de cedula : "))
    edad = int(input("Introduzca su edad: "))
    sexo = input("Introduzca si es hombre 'H' o mujer 'M': ")
    while not sexo == 'H'.upper() or sexo == 'M'.upper(): 
        sexo =  input("Introduzca si es hombre 'H' o mujer 'M': ")
    tipo = ["UltraSonido","Resonancia", "Tomografía"]
    for i,v in enumerate(tipo): 
        print(i+1,v)
    opcion= input("inttroduzca el número segun su opcion correspondiente:  ")
    while not opcion.isnumeric(): 
        opcion= input("inttroduzca el número segun su opcion correspondiente:  ")
    
    if int(opcion == 1) : 
        