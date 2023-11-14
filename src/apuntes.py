


def funcion_que_NO_pide_variable():
    print("FURULA!!!")

def funcion_que_pide_variable(variable):
    print(variable)

def funcion_que_pide_y_devuelve_una_variable(variableDeVenida):# <--
    #variableDeVenida                                               |
    variableDevuelta = "pong" #                                     |
    return variableDevuelta #--------------------------------------------------------
                                                            #       |               |
# A partir de aqui se inicia la ejecución del programa      #       |               |
                                                            #       |               |
funcion_que_NO_pide_variable()                              #       |               |
                                                            #       |               |
variable = "Aqui estoy"                                     #       |               |
funcion_que_pide_variable(variable)                         #       |               |
                                                            #       |               |
variableQueLePaso = "ping"                                  #       |               |
variableDeVuelta = funcion_que_pide_y_devuelve_una_variable(variableQueLePaso)  # <--
print(variableDeVuelta)

def condicionales():
    condicion_1 = 0
    condicion_2 = 1
    if condicion_1 < condicion_2:
        print("hi")
    elif condicion_2 >condicion_1:
        print("hello")
    else:
        print("LoQueTuQuieras")

def bucles():
    condicion = 0

    # a2 = input("aqui")

    while condicion < 1:
        condicion += 1

    for i in [0]:

        print(i)

    for a, b in [(1,2),(3,4)]:
        print("a:", a, "b:", b)


bucles()

