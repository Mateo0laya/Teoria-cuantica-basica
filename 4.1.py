'''Teoria cuantica basica, observables y medidas
    Mateo Olaya Garzon
    Septiembre 2021'''
import math

#1.El sistema debe calcular la probabilidad de encontrarlo en una posición en particular.

def probPos(p, ket):
    '''Funcion que calcula la probabilidad de que la particula se encuentre en la posicion p del vector ket
        ( int, list ) -> float'''
    x = (abs(ket[p]))**2                #modulo cuadrado de la posicion p
    y = 0
    for i in range(len(ket)):
        y += (abs(ket[i])**2)           #modulo cuadrado del vector ket
    z = x/y
    w = round(z*100, 2)
    return w

#2. El sistema si se le da otro vector Ket debe buscar la probabilidad de transitar del primer vector al segundo.

def probtrans(ket1, ket2):
    '''Funcion que calcula la propabilidad de tansitar del primer vector (ket1) al segundo vector(ket2)
        ( lis, list ) -> float'''
    x = 0
    for i in range(len(ket1)):
        x += (abs(ket1[i])**2)
    y = 
    
def main():
    p = 7
    ket = [2+1j,-1+2j,1j,1,3-1j,2,-2j,-2+1j,1-3j,-1j]
    x = probPos(p, ket)
    print(x)
main()