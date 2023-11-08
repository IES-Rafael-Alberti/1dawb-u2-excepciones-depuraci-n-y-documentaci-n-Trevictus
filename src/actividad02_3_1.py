"""Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)."""

def preguntarEdad():
    edad= input("Intorduce tu edad: ")
    return int(edad)

def definirAnios(edad):
    cont = 1
    while cont <= edad:
        if cont != edad:
            print (cont, end=", ")
        else:
            print (cont)
        cont += 1

def main():
    edad = preguntarEdad()
    definirAnios(edad)

if __name__ == "__main__":
    main()