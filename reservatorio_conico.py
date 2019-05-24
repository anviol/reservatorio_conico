################################################################################
#                                                                              #
#                        Trabalho Pratico Final de ATR                         #
#                              Reservatorio Conico                             #
#                                                                              #
# Professor: Armando Alves Neto                                                #
#                                                                              #
# Nome: Andre Vinicius de Oliveira          Matricula: 2013065935              #
# Nome: Grabriel                                                               #
#                                                                              #
# Versão: 1.00                                                                 #
# Data: 22/05/2019                                                             #
#                                                                              #
#                                 Python 3.7.3                                 #
################################################################################

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  megasena.py
# 
#  Copyright 2017 Tavares <tavares@tavares-Inspiron-5558>
# 
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
# 
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
# 
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
# 
# 
 
import matplotlib.pyplot as plt
import numpy as np
import random as rand

Cv = 0.5

tam = input('Digite o range do array: ')

try:
   tam = int(tam)
except ValueError:
   print("O valor digitado não é um número")
   exit()

h = [0]*tam
Qout = [0]*tam

for i in range(tam):
    h[i] = i
    Qout [i] = Cv * (h[i]**0.5)

plt.plot( h, Qout)
plt.title("Volume X Altura")
plt.show()

################################ Fim do Programa ###############################
