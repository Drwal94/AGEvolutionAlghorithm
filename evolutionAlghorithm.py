import random
import numpy as np
import matplotlib.pyplot as plt

N = 10
ilosc = 100
x1 = [[0 for i in xrange(N)] for i in xrange(ilosc)]
x2 = [[0 for i in xrange(N)] for i in xrange(ilosc)]
u = []
J = []
sum_u = []
adaptation = []
distribution = []
parents = []
childs = [[] for i in xrange(ilosc)]
Jmax = []


def prepareU():
    for i in range(0,ilosc):
        randomNumbers = []
        for x in range(0,N):
            randomNumbers.append(random.uniform(0,10))
        u.append(randomNumbers)
    return u

def calculateVariables(u):
    x1 = [[0 for i in xrange(N)] for i in xrange(ilosc)]
    x2 = [[0 for i in xrange(N)] for i in xrange(ilosc)]
    del J[:]
    del sum_u[:]
    del adaptation[:]
    del distribution[:]
    for i in range(0,ilosc):
        uPower = []
        for j in range(0,N):
            uPower.append(u[i][j]**2)
        for k in range(0,N-1):
            x1[i][k+1] = x2[i][k]
            x2[i][k+1] = 2*x2[i][k]-x1[i][k]+ u[i][k]/(N**2)
        sum_u.append(sum(uPower))
        J.append(x1[i][N-1]-(1/(2*N))*sum_u[i])
    sum_J = sum(J)
    for i in xrange(len(J)):
        adaptation.append(J[i]/sum_J)
        distribution.append(sum(adaptation))


def roulette():
    del parents[:]
    for i in range(0,ilosc):
        r = random.uniform(0,1)
        for j in xrange(len(distribution)):
            if r<=distribution[j]:
                parents.append(u[j])
                break

def crossover():
    childs = [[] for i in xrange(ilosc)]
    for i in xrange(len(parents)/2):
        for j in range(0,int(N/3)):
            childs[2*i].append(parents[2*i][j])
            childs[2*i+1].append(parents[2*i+1][j])
        for j in range(int(N/3),N):
            childs[2*i].append(parents[2*i+1][j])
            childs[2*i+1].append(parents[2*i][j])
    return childs

def run():
    u = prepareU()
    for i in range(0, 1000):
        calculateVariables(u)
        roulette()
        childs = crossover()
        u = childs
        Jmax.append(max(J))
    plt.plot(xrange(len(Jmax)),Jmax)
    plt.show()


#calculateVariables()
#roulette()
#crossover()
run()
#print childs[1]
