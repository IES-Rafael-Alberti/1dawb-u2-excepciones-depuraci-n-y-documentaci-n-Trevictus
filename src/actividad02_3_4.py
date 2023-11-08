"""Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada"""


def pedirNum(num):
    if num == int:
        return "Está bien."
    
def verificarNum(num):
    while num != int:
        return "La entrada no es correcta."
    
def main():
    numeroCorrecto = False
    while not numeroCorrecto:
        try:
            input("Introduce nº entero y positivo: ")
            pedirNum(num)
            verificarNum(num)
            num = int
            numeroCorrecto = True
        except ValueError:   #si no es un numero int
            if num == str:
                print("Debe de ser un nº entero.")
            elif num == None:
                print("Introduce un nº por favor.")
    