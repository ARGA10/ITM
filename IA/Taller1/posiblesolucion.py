# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 22:50:56 2017

@author: ARGA
"""


import matplotlib.pyplot as plt
"""ESTADOS"""

ax=20 
ay=5
bx=30
by=10
cx=40
cy=15

cx1=([140, 20]) 
cy1=([5, 5])
bx1=([80, 40]) 
by1=([5, 5])

cx3=([90, 20]) 
cy3=([10, 5])
ax1=([120, 60]) 
ay1=([5, 5])
cx4=([40, 20]) 
cy4=([5, 5])
bx2=([130, 40]) 
by2=([10, 5])
cx5=([140, 20]) 
cy5=([15, 5])

fig, ax = plt.subplots()
ax.broken_barh([(50, 2), (100, 2),(150, 2)], (5, 20), facecolors='blue')
ax.broken_barh([(ax,60)], (ay,5),facecolors=('yellow'))
ax.broken_barh([(bx,40)], (by,5),facecolors=('blue'))
ax.broken_barh([(cx,20)], (cy,5),facecolors=('red'))
ax.set_ylim(5, 30)
ax.set_xlim(0, 200)
ax.grid(True)



def Hanoi(discos, poste):
    if poste <=3 and poste>=1:
        if discos=="c" and poste==3:
            fig, ax = plt.subplots()
            ax.broken_barh([(50, 2), (100, 2),(150, 2)], (5, 20), facecolors='blue')
            ax.broken_barh([(ax,60)], (ay,5),facecolors=('yellow'))
            ax.broken_barh([(bx,40)], (by,5),facecolors=('blue'))
            ax.broken_barh([(cx+100,20)], (cy,5),facecolors=('red'))
            ax.set_ylim(5, 30)
            ax.set_xlim(0, 200)
            ax.grid(True)

        if discos=="c" and poste==2:
            fig, ax = plt.subplots()
            ax.broken_barh([(50, 2), (100, 2),(150, 2)], (5, 20), facecolors='blue')
            ax.broken_barh([(ax,60)], (ay,5),facecolors=('yellow'))
            ax.broken_barh([(bx,40)], (by,5),facecolors=('blue'))
            ax.broken_barh([(cx+50,20)], (cy,5),facecolors=('red'))
            ax.set_ylim(5, 30)
            ax.set_xlim(0, 200)
            ax.grid(True)        
        if poste==3:
            fig, ax = plt.subplots()
            ax.broken_barh([(50, 2), (100, 2),(150, 2)], (5, 20), facecolors='blue')
            ax.broken_barh([(ax,60)], (ay,5),facecolors=('yellow'))
            ax.broken_barh([(bx,40)], (by,5),facecolors=('blue'))
            ax.broken_barh([(cx,20)], (cy,5),facecolors=('red'))
            ax.set_ylim(5, 30)
            ax.set_xlim(0, 200)
            ax.grid(True)
if ndiscos > 0:
        ndiscos = int(input("Movimiento de discos:"))
        Hanoi(ndiscos-1, inicial, final, temporal)
        print 'Se mueve de la torre', inicial, 'a la torre', final
        Hanoi(ndiscos-1, temporal, inicial, final)


discos = int(input("Seleccione dico a mover:"))
poste = int(input("Seleccione Poste:"))


Hanoi(discos,poste, 2, 3)


  
     
















