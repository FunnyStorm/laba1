from math import *
def formula1(alpha):
    z1 = 2 * sin(3*pi-2*alpha)*sin(3*pi-2*alpha)*cos(5*pi+2*alpha)*cos(5*pi+2*alpha)
    print("{0:.4f}".format(z1))

def formula2(alpha):
    z2 = 1/4-1/4*sin(5/2*pi-8*alpha)
    print("{0:.4f}".format(z2))

a = float(input("Введите параметр а: "))
formula1(a)
formula2(a)