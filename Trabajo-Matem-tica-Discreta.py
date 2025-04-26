import numpy as np
import random as rd
import pandas as pd
def validar_num(entrada,min,max):

    if entrada > min or entrada < max:

        return entrada
    else:
        return None


def validar_l(entrada):
    try:

        return entrada

    except ValueError:
        return None

def CrearMatriz(x):

    matriz=np.zeros((x,x), dtype=int)
    i=1
    e=1
    for i in range(x):
        for e in range(x):
            if e==i:
                continue
            else:
                if np.sum(matriz[i])==5:
                    continue
                else:
                    if np.sum(matriz[e])==5:
                        continue
                    else:
                        if matriz[e][i]==1:
                            continue
                        elif matriz[e][i]==0:
                            matriz[e][i]=rd.randint(0,1)
                            if  matriz[e][i]==1:
                                matriz[i][e]=1
                                

    return matriz

def ver_matriz(matriz):

    print(matriz)


min = 60
max = 500

def Main():
    opcion=0
    while (opcion!=9):
        print("Buen dia, ingrese la opcion que desea realizazar hoy:")
        print("[1] Crear una nueva matriz de empleados")
        print("[2] Simular infeccion")
        print("[3] Mostrar grafico de infeccion") ##tema extra del proyecto##
        print("[4] Ver matriz")
        print("[5] Salir")

        try:
            opcion = int(input("Ingresa una opcion..."))

        except ValueError:
            print("No selecciono una opcion correcta, intente nuevamente...")

        match opcion:

                case 1:
                    x = int(input("Ingrese el tamaño de la matriz que este entre 60 y 500: "))
                    matriz = CrearMatriz(x)

                case 2: 
                    None

                case 3: 
                    None

                case 4:
                    ver_matriz(matriz)
                case 5: 
                    break
                case _:
                    print("No selecciono una opcion valida")



np.set_printoptions(threshold=np.inf)
Main()