"""
@author: Thomas GAUTHEY
Test function for optimization

Adjustement : Thomas LEMERCIER
"""
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from itertools import product


def lvl1(X, show=False, time_to_plot=5):
    """Dimension 1, minimum en 2"""
    if show:
        plt.ion()
        plt.figure('Dessin')
        plt.clf()
        plt.scatter(X, (X-2)**2)
        plt.plot((x:=np.linspace(-10,10,100)), [(z-2)**2 for z in x])
        plt.show()
        plt.pause(time_to_plot)
    return (X-2)**2


def lvl2(X, show=False, time_to_plot=5):
    """Dimension 1, minimum en -8"""
    if show:
        plt.ion()
        plt.figure('Dessin')
        plt.clf()
        plt.scatter(X, 1 + (X+8)**2 - np.cos(4*np.pi*(X+8)))
        plt.plot((x:=np.linspace(-10,10,100)), [1 + (z+8)**2 - np.cos(4*np.pi*(z+8)) for z in x])
        plt.show()
        plt.pause(time_to_plot)
    return 1 + (X+8)**2 - np.cos(4*np.pi*(X+8))


def lvl3(X, show=False, time_to_plot=5):
    """Dimension 1, minimum aux environs de 420, restreindre la zone de recherche dans [-500,500]"""
    if show:
        plt.ion()
        plt.figure('Dessin')
        plt.clf()
        plt.scatter(X, -X*np.sin(np.sqrt(abs(X))))
        plt.plot((x:=np.linspace(-500,500,100)), [-z*np.sin(np.sqrt(abs(z))) for z in x])
        plt.show()
        plt.pause(time_to_plot)
    return -X*np.sin(np.sqrt(abs(X)))


def lvl4(X, show=False, time_to_plot=5):
    """Dimension 2, minimum en (0, 0)"""
    if show: 
        plt.ion()
        fig = plt.figure()
        plt.clf()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter([X[0]], [X[1]], 20 + (X[0]**2 - 10*np.cos(2*np.pi*X[0])) + (X[1]**2 - 10*np.cos(2*np.pi*X[1])), c='r')
        M = np.arange(-5, 5, 0.05)
        N = np.arange(-5, 5, 0.05)
        M, N = np.meshgrid(M, N)
        ax.plot_wireframe(M, N, np.array([20 + (x**2 - 10*np.cos(2*np.pi*x)) + (y**2 - 10*np.cos(2*np.pi*y)) for x, y in zip(M,N)]), rstride=5, cstride=5)
        plt.show()
        plt.pause(time_to_plot)
    return 20 + (X[0]**2 - 10*np.cos(2*np.pi*X[0])) + (X[1]**2 - 10*np.cos(2*np.pi*X[1]))


def lvl5(X, show=False, time_to_plot=5):
    """Dimension 2, minimum en (0, 0)"""
    if show: 
        plt.ion()
        fig = plt.figure()
        plt.clf()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter([X[0]], [X[1]], 20 + (X[0]**2 - 10*np.cos(2*np.pi*X[0])) + (X[1]**2 - 10*np.cos(2*np.pi*X[1])), c='r')
        M = np.linspace(-5, 5, 150)
        N = np.linspace(-5, 5, 150)
        M, N = np.meshgrid(M, N)
        ax.plot_wireframe(M, N, np.array([1 - (1 + np.cos(12*np.sqrt(x**2 + y**2)))/(0.5*(x**2 + y**2)+2) for x, y in zip(M, N)]), rstride=15, cstride=15)
        plt.show()
        plt.pause(time_to_plot)
    return 1 - (1 + np.cos(12*np.sqrt(X[0]**2 + X[1]**2)))/(0.5*(X[0]**2 + X[1]**2)+2)


def lvl6(X, show=False, time_to_plot=5):
    """Dimension 2, minimum en (2, 1)"""
    a = [3, 5, 2, 1, 7]
    b = [5, 2, 1, 4, 9]
    c = [1, 2, 5, 2, 3]
    result = 0
    for i in range(len(a)):
        result += c[i]*np.exp(-(X[0]-a[i])**2/np.pi - (X[1]-b[i]) **
                              2/np.pi)*np.cos(np.pi*(X[0]-a[i])**2+np.pi*(X[1]-b[i])**2)
    return -result


def lvl7(X, show=False, time_to_plot=5):
    """Dimension minimale 10, la dimension doit toujours ??tre pair, minimum pour un cercle"""
    dist = 0
    nb_point = len(X)/2
    for i in range(0, len(X), 2):
        dist += abs(np.cos(np.pi*i/nb_point) - X[i])
        dist += abs(np.sin(np.pi*i/nb_point) - X[i+1])
    if show:
        plt.ion()
        plt.figure('Dessin')
        plt.clf()
        for i in range(0, len(X), 2):
            plt.scatter(X[i], X[i+1], color='r')
        theta = np.linspace(0, 2*np.pi, 100)
        plt.plot(np.cos(theta), np.sin(theta), color='white')
        plt.axis('equal')
        plt.show()
        plt.pause(time_to_plot)
    return dist


def lvl8(X, show=False, time_to_plot=5):
    """Dimension minimale 20, la dimension doit toujours ??tre pair"""
    dist = 0
    nb_point = len(X)/2
    for i in range(0, len(X), 2):
        dist += abs(np.cos(np.pi*i/nb_point) * (1+np.cos(np.pi*i/nb_point)) - X[i])
        dist += abs(np.sin(np.pi*i/nb_point) * (1+np.cos(np.pi*i/nb_point)) - X[i+1])
    if show:
        plt.ion()
        plt.figure('Dessin')
        plt.clf()
        for i in range(0, len(X), 2):
            plt.scatter(X[i], X[i+1], color='r')
        theta = np.linspace(0, 2*np.pi, 100)
        plt.plot(np.cos(theta)*(1+np.cos(theta)), np.sin(theta) * (1+np.cos(theta)), color='white')
        plt.show()
        plt.pause(time_to_plot)
    return dist


def lvl9(X, show=False, time_to_plot=5):
    """Dimension minimale 40, la dimension doit toujours ??tre pair"""
    dist = 0
    nb_point = len(X)/2
    for i in range(0, len(X), 2):
        s = np.pi*i/nb_point
        dist += abs(16*np.sin(s)**3 - X[i])
        dist += abs(13*np.cos(s)-6*np.cos(2*s)-2 * np.cos(3*s)-np.cos(4*s) - X[i+1])
    if show:
        plt.ion()
        plt.figure('Dessin')
        plt.clf()
        for i in range(0, len(X), 2):
            plt.scatter(X[i], X[i+1], color='r')
        theta = np.linspace(0, 2*np.pi, 100)
        plt.plot(16*np.sin(theta)**3, 13*np.cos(theta)-6*np.cos(2*theta)-2 * np.cos(3*theta)-np.cos(4*theta), color='white')
        plt.show()
        plt.pause(time_to_plot)
    return dist


def lvl10(X, show=False, time_to_plot=5):
    """Dimension minimale 80, la dimension doit toujours ??tre pair"""
    def f1(x): return (abs(x)/x)*(abs(x) - .5*abs(abs(x)-2) - .25*abs(abs(x)-2) - .25*abs(abs(x)-4) + (23/8)*(abs(abs(x)-8)-abs(abs(x)-12)) - (29/10)
                                  * (abs(abs(x)-16)-abs(abs(x)-21)) + .25*((abs(abs(x)-12)-abs(abs(x)-16)-2)**2) - 10*np.cos((np.pi/16)*(abs(abs(x)-4)-abs(abs(x)-8)+12)) - 10)
    def f2(y): return -((abs(y) - abs(abs(y)-1) + 1)/2)**2 + .25*(6*abs(abs(y)-1) - 11*abs(abs(y)-2) + 5*abs(abs(y)-4)) - 2*(abs(abs(y)-12) -
                                                                                                                             abs(abs(y)-16)) - (12/1e5)*(abs(abs(y)-16) - abs(abs(y)-21) + 5)**5 - 6*np.sin((np.pi/16)*(abs(abs(y)-4) - abs(abs(y)-8) + 12)) + 10
    dist = 0
    for i in range(0, len(X), 2):
        s = -21 + 42*i/len(X) + 1e-4
        dist += abs(((f1(s) - X[i])**2) * (2*np.sin(f1(s) - X[i])))
        dist += abs(((f2(s) - X[i+1])**2) * (2+np.sin(f2(s) - X[i+1])))
    if show:
        plt.ion()
        plt.figure('Dessin')
        plt.clf()
        for i in range(0, len(X), 2):
            plt.scatter(X[i], X[i+1], color='r')
        theta = np.linspace(-21, 21, 100)
        plt.plot(f1(theta), f2(theta), color='white')
        plt.show()
        plt.pause(time_to_plot)
    return dist
