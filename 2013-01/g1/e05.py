# encoding: utf-8 -*-

"""

Pitágoras
---------

Este script es solución del ejercicio 5 de la guía 1 del curso
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

from math import sqrt

a = float(raw_input("Cateto a >> "))
b = float(raw_input("Cateto b >> "))

print "Hipotenusa:", sqrt(a*a + b*b)
