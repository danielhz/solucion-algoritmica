# encoding: utf-8 -*-

"""

Sillas
------

Este script es solución del ejercicio 7 de la guía 1 del curso
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

# Anotamos los precios
precio_clavos = 1000    # paquete de 100 unidades
precio_barniz = 5000    # frasco
precio_madera = 5000    # listón
precio_mimbre = 500     # varilla

# Pedimos la cantidad de sillas
n = int(raw_input("Número de sillas a construir >> "))

# Calculamos los clavos que necesitaremos
# (cada silla necesita 10 clavos)
clavos = n*10                  # clavos que se necesitan
paquetes_clavos = clavos/100   # paquetes que se usan completamente
if clavos % 100 > 0:
    paquetes_clavos += 1       # sumamos paquete a medio usar

# Calculamos la cantidad de barniz que neceistaremos
# (cada frasco nos alcanza para 20 sillas)
frascos_barniz = n/20          # frascos que se gastan completamente
if n % 20 > 0:
    frascos_barniz += 1        # sumamos frasco a medio usar

# Calculamos la cantidad madera que necesitaremos
# (Cada listón nos sirve para fabricar 3 sillas)
listones_madera = n/3          # listones que se gastan completamente
if n % 3 > 0:
    listones_madera += 1       # sumamos listón a medio usar

# Calculamos la cantidad mimbre que necesitaremos
# (Cada silla requiere 3 varillas)
varillas_mimbre = n*3          # varillas que se necesitan

print "Costo:", \
    precio_clavos * paquetes_clavos + \
    precio_barniz * frascos_barniz + \
    precio_madera * listones_madera + \
    precio_mimbre * varillas_mimbre
