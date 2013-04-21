# encoding: utf-8 -*-

"""

Convertir HH:MM:SS a segundos
-----------------------------

Este script es solución del ejercicio 9 de la guía 1 del curso
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

t = raw_input("Tiempo (HH:MM:SS) >> ")

h = int(t[0:2])         # las horas
m = int(t[3:5])         # los minutos
s = int(t[6:8])         # los segundos

print 3600*h + 60*m + s
