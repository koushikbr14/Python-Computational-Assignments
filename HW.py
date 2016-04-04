# -*- coding: utf-8 -*-
"""
Created on Sun Apr 03 16:29:03 2016

@author: Koushik
"""
###Problem 1
import Homework_1_module as HW1mod
a = 7**5
b = 0    
m = 2**31 - 1
n = 10000
Uniform_LGM = HW1mod.Uniform_rand(a,b,m,n)

# Calculating Mean and Standard deviation of this sample
mean_LGM = HW1mod.mean(Uniform_LGM)
std_LGM  = HW1mod.std(Uniform_LGM)

print mean_LGM
print std_LGM

#Comparing with python default uniform random functions
import numpy
python_uniform_rand = numpy.random.uniform(0.0,1.0,10000)

mean_python_uniform_rand = numpy.mean(python_uniform_rand)
std_python_uniform_rand = numpy.std(python_uniform_rand)

print mean_python_uniform_rand
print std_python_uniform_rand

#As we can see they are close 


### Problem 2

p = [0.3,0.35,0.2,0.15]
x = [-1,0,1,2]
n = 10000
U = Uniform_LGM
print len(p),len(x)

Discrete_rand = HW1mod.Discrete_dist(x,p,U)

print Discrete_rand

import matplotlib.pyplot as plt

plt.hist(Discrete_rand)
plt.show()

n = 44000

Uniform_LGM_44 = HW1mod.Uniform_rand(a,b,m,n)

p = [0.36,0.64]
x = [0,1]

U_44 = Uniform_LGM_44

Discrete_rand = HW1mod.Discrete_dist(x,p,U_44)

Binomial_dist = []

n = 1000
for i in range(0,n):
    Binomial_dist.append(sum(Discrete_rand[44*i:44*(i+1)])) 

#print Binomial_dist

print len(Binomial_dist)

import matplotlib.pyplot as plt
plt.hist(Binomial_dist)
plt.show()

#Calculating Probability
count = HW1mod.count_greater_k(Binomial_dist,40)
prob = float(count)/n
print prob

#Exponential Distribution
n = 10000
lamda = 1.5
Exp_dist = HW1mod.Exp_dist(U,lamda)
print Exp_dist

count_x_1 = HW1mod.count_greater_k(Exp_dist,1)
count_x_4 = HW1mod.count_greater_k(Exp_dist,4)

prob_x_greater_1 = float(count_x_1)/n
prob_x_greater_4 = float(count_x_4)/n

print prob_x_greater_1
print prob_x_greater_4

exp_mean = HW1mod.mean(Exp_dist)
exp_std =  HW1mod.std(Exp_dist)

print exp_mean,exp_std

plt.hist(Exp_dist)
plt.show()

#Normal Distribution
import time
n = 5000

U1 = HW1mod.Uniform_rand(a,b,m,n)
U2 = HW1mod.Uniform_rand(a,b,m,n)

# Box muller Method
start_time_BM = time.time()
Normal_BM_rand = HW1mod.Normal_BM(U1,U2)
end_time_BM = time.time()

mean_norm_bm = HW1mod.mean(Normal_BM_rand)
std_norm_bm = HW1mod.std(Normal_BM_rand)

print mean_norm_bm,std_norm_bm

#Polar Marsaglia
start_time_PM = time.time()
Normal_PM_rand = HW1mod.Normal_PM(U1,U2)
end_time_PM = time.time()

mean_norm_pm = HW1mod.mean(Normal_PM_rand)
std_norm_pm = HW1mod.std(Normal_PM_rand)

print mean_norm_pm,std_norm_pm

#time taken by both the methods
time_BM = end_time_BM - start_time_BM
time_PM = end_time_PM - start_time_PM

print "Time taken by Box Muller method is %r seconds and time taken by Polar Marsaglia method is %r seconds " % (time_BM, time_PM)
