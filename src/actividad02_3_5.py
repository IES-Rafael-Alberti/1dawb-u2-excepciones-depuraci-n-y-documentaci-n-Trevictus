"""Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError con el mensaje, "Incorrect Password!!"""


def solicitarContrasenia(contrasenia):   
    clave = input("Introduce: 'contraseña'"+"\n")

    if clave.lower() != contrasenia:
        raise ValueError 
    
    print("ole")

    print("Accediendo. Se cierra el programa.")

    

def solicitarContrasenia2(contrasenia):   
    error = True
    while error:
        clave = input("Introduce: 'contraseña'"+"\n")
        try:
            if clave.lower() != contrasenia:
                raise ValueError
            error = False
        except ValueError:
            print("La clave no coincidee con la contraseña")           


    print("ole")

    print("Accediendo. Se cierra el programa.")




def main():
    contrasenia = "contraseña"

    #Opción 1
    error = True
    while error:
        try:
            solicitarContrasenia(contrasenia)
            error = False
        except ValueError:
            print("La clave no coincidee con la contraseña")


    #Opción 2
    solicitarContrasenia2(contrasenia)


if __name__ == "__main__":
    main()