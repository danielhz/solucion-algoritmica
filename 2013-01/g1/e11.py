# encoding: utf-8 -*-

"""

Qué nota necesito
-----------------

Este script es solución del ejercicio 11 de la guía 1 del curso
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

a = float(raw_input("Nota 1 >> "))
b = float(raw_input("Nota 2 >> "))
c = float(raw_input("Nota 3 >> "))

print "Necesitas un", 16 - (a+b+c)
