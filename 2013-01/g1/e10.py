# encoding: utf-8 -*-

"""

Qué edad tengo
--------------

Este script es solución del ejercicio 10 de la guía 1 del curso
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

t0 = raw_input("¿Cuándo naciste? >> ")
t1 = raw_input("Fecha actual >> ")

y0,y1 = int(t0[0:4]),  int(t1[0:4])   # los años
m0,m1 = int(t0[5:7]),  int(t1[5:7])   # los meses
d0,d1 = int(t0[8:10]), int(t1[8:10])  # los días

edad = y1 - y0

if m1 < m0:
    edad -= 1
elif m1 == m0 and d1 < d0:
    edad -= 1

print "Tienes", edad, "años"
