#!/usr/bin/python
lista = ['abcd', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']
print lista # Imprime lista completa
print lista [0] # Imprime el primer elemento de la lista
print lista [1: 3] # Imprime elementos desde el 2 hasta el 3
print lista [2:] # Imprime elementos a partir del 3er elemento
print tinylist * 2 # Imprime la lista dos veces
nuevalista = lista + tinylist
print lista + tinylist # Imprime listas concatenadas
