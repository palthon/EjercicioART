# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 11:40:40 2022

@author: Paloomm
"""

from random import randint


print("Este código generará números enteros entre 1 y 7.")


""" Partimos de una función que genera números aleatorios entre 1 y 5; esta
función puede ser radint(1,5)

 Como la función va a generar enteros entre 1 y 5 y buscamos enteros
entre 1 y 7, una posibilidad es establecer una matriz 5x5 de números enteros
entre 1 y 7. La funcion gen5 se utilizará para obtener de forma aleatoria
las coordenadas de la componente de la matriz que sea elegida. 

Hay que tener en cuenat que Python cuenta las componentes de vectores y 
matrices desde 0, por tanto, para poder utilizar la función gen5,
es necesario que la matriz de números enteros sea en realidad 6x6, siendo
la primera fila y la primera columna de 0, que nunca será elegida"""

numbers = [[0,0,0,0,0,0],
          [0,1,2,3,4,5],
          [0,6,7,1,2,3],
          [0,4,5,6,7,1],
          [0,2,3,4,5,6],
          [0,7,1,2,3,4]]

chosen=0; #Esta es la variable donde se almacenará el resultado

i = randint(1,5); #i representa la primera coordenada de la matriz

j = randint(1,5); #j representa la segunda coordenada de la matriz


chosen = numbers[i][j];

print("El número elegido es:")
print(chosen);
