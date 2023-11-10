"""Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada"""


def verificarNum(num):
    num = int(input("Introduce un nº entero: "))
    if num == int:
        print(num, "es el numero entero que has seleccionado.")
        
    else: 
        print("ERROR")





# A partir de aquí se ejecuta el programa.

def main():
    num = int
    verificarNum(num)


if __name__ == "__main__":
    main()