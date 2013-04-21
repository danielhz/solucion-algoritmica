# encoding: utf-8 -*-

"""

Lleve 3 pague 2
---------------

Este script es solución del ejercicio 6 de la guía 1 del curso
Solución Algorítmica de Problemas de la Universidad de Talca,
semestre 2013-01.

El enunciado se encuentra en:
http://daniel.degu.cl/cursos/solucion-algoritmica/ejercicios-01

Profesor: Daniel Hernández

Ayudantes:
  - Alex Muñoz
  - Diego Rodríguez
  - Ivan Martínez
  - Manuel Hoffhein

"""

a = float(raw_input("Precio prenda 1 >> "))
b = float(raw_input("Precio prenda 2 >> "))
c = float(raw_input("Precio prenda 3 >> "))
d = min(a, min(b,c))
s = a+b+c

print "Precio:", s
print "Descuento:", d
print "Total a pagar", s-d
