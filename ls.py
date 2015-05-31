from random import randint
import math


def ls(X,Y,k):
    t = to2D(X,Y)
    return localSearch(t,k)


def localSearch(X,k):
    rp = set()
    while len(rp) < k:
        rp.add(randint(0,len(X)-1))
    M = []
    for i in rp:
        M.append(X[i])
    change = True
    while change:
        change = False
        for x in X:
            if is_in(M,x) == False:
                for m in M:
                    M1 = []
                    M1.extend(M)
                    M1[M.index(m)] = x
                    if cost(X, M1) < (1-0.01)*cost(X, M):
                        M = M1
                        change = True
    return {"M":M,'radius':radius(X,M,k)}



def radius(X,C,k):
    rad = []
    for i in range(k):
        rad.append(0)
    for x in X:
        counter = 0
        b = 0
        dc = 1<<32 #assigned a big number
    
        for c in C:
            dis = distance(c,x)
            if dis < dc:
                b = counter
                dc = dis
            counter+=1
        if rad[b] < dc:
            rad[b]=dc
    return rad


def to2D(X,Y):
    result = []
    i = 0
    for x in X:
        result.append([x,Y[i]])
        i+=1
    return result


def is_in(M,x):
    for m in M:
        if distance(m,x) == 0:
            return True
    return False




def cost(X,M):
    sum = 0
    for x in X:
        md = 1 << 32
        for m in M:
            d = distance(x,m)
            if d < md:
                md = d
        sum += md
    return sum
            




def distance(a, b):
    l = len(a)
    d = 0
    for i in range(l):
        d =d + (a[i]-b[i])*(a[i]-b[i])
    d = math.sqrt(d)
    return d
