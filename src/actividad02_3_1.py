"""Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)."""

def preguntarEdad():
        edad = int(input("Intorduce tu edad: "))
        if edad > 0:
            return edad
        else:
            print("El nº introducido debe ser entero y positivo.")




def definirAnios(edad):
    
    cont = 1
    while cont <= edad: 
        if cont == edad:
            print(f"{cont}" + ".")
        else:
            print (f"{cont}" + ", " )
        cont += 1



# A partir de aquí se ejecuta el programa      
def main():
    
    edad = preguntarEdad()
    definirAnios(edad)

    

if __name__ == "__main__":
    main()