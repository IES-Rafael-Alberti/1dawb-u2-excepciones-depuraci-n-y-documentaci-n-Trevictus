"""Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas."""



def pedirNum(num):
    cont = 1
        
    while cont <= num:
        if (cont == num or cont == num -1) and cont%2 != 0:
            print(cont, end = ".")
        
        elif cont%2 != 0:
            print(cont, end=", ")
        cont += 1
        

    if num < 0:
        print("ERROR")


            
def main():
    num = int(input("Introduce un nº positivo entero: "))
    pedirNum(num)




if __name__ == "__main__":
    main()