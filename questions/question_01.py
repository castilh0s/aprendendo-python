#!/usr/bin/python
# -*- coding: utf-8 -*-

# 1. Dado o tamanho da base e da altura de um retângulo, calcular a sua área e o
# seu perímetro.

base = input("Informe a base: ")
altura = input("Informe a altura: ")

area = (int(base) * int(altura))
perimetro = (int(base) * 2) + (int(altura) * 2)

print("\nÁrea: " + str(area))
print("Perímetro: " + str(perimetro))
