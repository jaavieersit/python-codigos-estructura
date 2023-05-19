import random

#Item 1
print("ITEM I")
filas_Matrices = int(input ("Introduzca el numero de filas de sus matrices 1 y 2: ")) 
columnas_Matrices = int(input ("Introduzca el numero de columnas de sus matrices 1 y 2: "))
matriz_1 = []
matriz_2 = []
matriz_3 = []

for i in range (filas_Matrices):
    matriz_1.append( [0] * columnas_Matrices)
    matriz_2.append( [0] * columnas_Matrices)
    
    

for i in range(filas_Matrices):
	for j in range(columnas_Matrices):
		matriz_1[i][j] = int((random.randint(2, 5)))
print('La primera matriz es\n', matriz_1)

print("________")

for i in range(filas_Matrices):
	for j in range(columnas_Matrices):
		matriz_2[i][j] = int((random.randint(2, 5)))

print('La segunda matriz es\n', matriz_2)

print("______________________________________________")
print("______________________________________________")



RestaMatrices = matriz_1[i][j] - matriz_2[i][j]
print(f"la resta entre esta dos matrices es :{RestaMatrices}")

print("______________________________________________")
print("______________________________________________")


filas_3 = int(input ("Introduzca el numero de filas para matriz 3: ")) 
columnas_3 = int(input ("Introduzca el numero de columnas para matriz 3: "))

for i in range(filas_3):
    matriz_3.append( [0] * columnas_Matrices)


for i in range(filas_3):
    for j in range(columnas_3):
        matriz_3[i][j] = int(random.randint(2, 5))
print('La Tercera matriz la cual es la que multiplica es\n', matriz_3)        

MatrizMultiplica = int(RestaMatrices * matriz_3[i][j])
print(f"El resultado de este es :{MatrizMultiplica}")

print("______________________________________________")
print("______________________________________________")


print("Item 1 parte 2")
import numpy as np

mz3 = np.array(matriz_3)
print(f"La matriz suma transpuesta (A + B)T, es {np.transpose(mz3)}")
mz2 = np.array(matriz_2)
mz1 = np.array(matriz_1)
mz1_m_2 = np.transpose(mz1) + np.transpose(mz2)
print(f"La operación AT + BT es {mz1_m_2}")