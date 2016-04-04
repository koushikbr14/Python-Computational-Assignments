# -*- coding: utf-8 -*-
# Uniform Distribution
def Uniform_rand(a,b,m,n):
    X = [14]
    for i in range(0,n-1):
        X.append((a*X[i] + b) % m) 
    U =[]
    U[:] = [(x + 0.5)/m for x in X]
    return U
    
#Mean and Standard Deviation
def mean(List):
    x = sum(List)/float(len(List))
    return x

def std(List):
    x = ((1/float(len(List)-1))*sum([(y-sum(List)/float(len(List)))**2 for y in List]))**0.5
    return x

#Discrete distribution function for any number of inputs
def Discrete_dist(Xi,P,U):
    Cum_P = []    
    Cum_P.append(0)
    X = []
    for i in range(1,len(P)+1):
        Cum_P.append(sum(P[:i]))
        
    print Cum_P
    
    if len(Xi) == len(P):
        for i in range(0,len(U)):
            for j in range(0,len(P)):
                #print i
                if U[i] < Cum_P[j+1] and U[i] > Cum_P[j]:
                    X.append(Xi[j])
    #print len(Xi),len(P)   
        else:
            print "lenght of discrete numbers and probability doesnt match, please check!"
    return X

# Counting numbers greater than a particular number in a list
def count_greater_k(List, k):
    x = [i for i in List if i > k]
    return(len(x))
    
#Exponential Distribution
import math
def Exp_dist(U,lamda):
    Y = [-lamda*math.log(x) for x in U]
    return Y
   
#Box Muller Method
def Normal_BM(U1,U2):
    Z1 = [(-2*math.log(x))**0.5*math.cos(2*math.pi*y) for x,y in zip(U1,U2)]
    Z2 = [(-2*math.log(x))**0.5*math.sin(2*math.pi*y) for x,y in zip(U1,U2)]
    Z = Z1 + Z2
    return Z
    
#Polar Marsaglia Method
def Normal_PM(U1,U2):
    V1 = [2*x-1 for x in U1]
    V2 = [2*x-1 for x in U2]
    w = [x**2+y**2 for x,y in zip(U1,U2)]
    W = [x for x in w if x <= 1]  #for w <= 1
    Z1 = [x*(-2*math.log(y)/y)**0.5 for x,y in zip(V1,W)]
    Z2 = [x*(-2*math.log(y)/y)**0.5 for x,y in zip(V2,W)]
    Z = Z1 + Z2 
    return Z

    
    
    
    