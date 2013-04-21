# encoding: utf-8 -*-

"""

Convertir segundos a HH:MM:SS
-----------------------------

Este script es solución del ejercicio 8 de la guía 1 del curso
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

Obseración: Para imprimir el resultado se utilizó el operador %
entre un string y varios parámetros numéricos. Este operador no
se ha enseñado, por lo que no es necesario usarlo en la corrección.
Aquí se usa para imprimir que todos los números nos queden con dos
dígitos.

La siguente solución basta para que se considere bueno el ejercicio:

    print str(h) + ":" + str(m) + ":" + str(s)

"""

s = int(raw_input("Segundos >> "))

h = s/3600         # las horas
s %= 3600          # nota: también sirve s -= h*3600
m = s/60           # los minutos
s %= 60            # nota: también sirve s -= m*60

print "%02i:%02i:%02i" % (h,m,s)   # Ver observación arriba
