"""Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. Deberá solicitar el número hasta introducir uno correcto."""

def pedirNum(num):
    cont = num
    while cont >= 0:
        if cont != 0:
            print(cont, end = ", ")
        else:
            print(f"{cont}" + ".")
        cont = cont -1
        
    if num < 0:
        print("ERROR")




def main():
    num = int(input("Introduce un nº positivo y entero: "))
    pedirNum(num)


if __name__ == "__main__":
    main()