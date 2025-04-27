import numpy as np
import random as rd
import pandas as pd

def validar_num(entrada, min_valor, max_valor):
    if min_valor <= entrada <= max_valor:
        return entrada
    else:
        return None


def CrearMatriz(x):
    matriz = np.zeros((x, x+1), dtype=int)

    for i in range(x):
        for e in range(x):
            if e == i:
                continue  
            else:
                if np.sum(matriz[i]) == 5:  
                    continue
                else:
                    if np.sum(matriz[e]) == 5:  
                        continue
                    else:
                        if matriz[e][i] == 1:
                            continue  
                        elif matriz[e][i] == 0:
                            matriz[e][i] = rd.randint(0, 1)
                            if matriz[e][i] == 1:
                                matriz[i][e] = 1  

    return matriz


def ver_matriz(matriz):
    print(matriz)


min_valor = 60
max_valor = 120

#Inicializacion con el none

def Main():
    opcion = 0
    matriz = None

    while opcion != 9:
        print("\nBuen día, ingrese la opción:")
        print("[1] Crear matriz")
        print("[2] Simular infección")
        print("[3] Mostrar matriz")
        print("[4] Salir")

        try:
            opcion = int(input("Ingrese una opción: "))
        except ValueError:
            print("Ingrese un número válido.")
            continue

        if opcion == 1:
            matriz=None
            while matriz is None:
                try:
                    x = int(input("Ingrese el tamaño de la matriz (60-120): "))
                    if 60 <= x <= 120:
                        matriz = CrearMatriz(x)
                    else:
                        print("Número fuera de rango.")
                except ValueError:
                    print("Debe insertar un numero")   

        elif opcion == 2:
            if matriz is None:
                print("Debe crear una matriz primero.")
            else:
                print("Simulando... (pendiente)")
        
        elif opcion == 3:
            if matriz is None:
                print("Debe crear una matriz primero.")
            else:
                ver_matriz(matriz)
        
        elif opcion == 4:
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción inválida.")

np.set_printoptions(threshold=np.inf)
Main()