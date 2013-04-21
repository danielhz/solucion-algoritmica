# encoding: utf-8 -*-

"""

Jalisco juega al cachipún
-------------------------

Este script es solución del ejercicio 2 de la guía 1 del curso
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

x = raw_input("Juguemos al cachipún. ¿Qué escoges? >> ")

if x == "piedra":
    print "Ja, te gano con papel"
elif x == "papel":
    print "Ja, te gano con tijera"
elif x == "tijera":
    print "Ja, te gano con piedra"
else:
    print "Jugar ", x, " no vale. Puedes jugar piedra, papel o tijera"
