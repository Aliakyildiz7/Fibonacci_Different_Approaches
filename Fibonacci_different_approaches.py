#Source: https://www.youtube.com/watch?v=Qk0zUZW-U_M
from time import time
#Calculates the nth term of Fibonacci Series with different approaaches
#First two terms of Fibonacci Series is taken as 0 and 1


#Iterative Method
def fibo_iter(n):
    liste = [0, 1]
    for x in range(2, n):
        liste.append(liste[x-1] + liste[x-2])

    return liste[-1]



#Recursive Method
def fibo_recur(n):
    if n == 1 or n == 0:
        return n
    else:
        return (fibo_recur(n-1) + fibo_recur(n-2))




#Recursive Method with Memoization
Cache = {}
def fibo_memo(n):

    if n in Cache:
        return Cache[n]
    elif n == 0 or n == 1:
        return n
    else:
        value = fibo_memo(n-1) + fibo_memo(n-2)
        Cache[n] = value
        return value

#Memoization is faster than even iteration. Recursion without memoization is useless in this case.




#Memoization from the library
from functools import lru_cache
@lru_cache(maxsize = 1000) #default is 128
def fibo_lru(n):

    if n == 1 or n == 0:
        return n
    else:
        return (fibo_lru(n-1) + fibo_lru(n-2))





n = 1001 #Upper Limit + 1
#When n=10001 iteration took 19 seconds. Memoization took less than 1.




time1 = time()
for x in range(n):

    fibo_iter(x)

time2 = time()
print(f"Iterative method  time for {n-1}th term is", time2 - time1, "seconds")


time1 = time()
for x in range(n):

    fibo_memo(x)

time2 = time()
print(f"Memoization method  time for {n-1}th term is", time2 - time1, "seconds")


"""
#Recursion without memoization is useless
n = 40
time1 = time()
for x in range(n):

    fibo_recur(x)

time2 = time()
print(f"Recursive method  time for {n-1}th term is", time2 - time1, "seconds")
"""



time1 = time()
for x in range(n):

    fibo_lru(x)

time2 = time()
print(f"Library memoization method  time for {n-1}th term is", time2 - time1, "seconds")

"""
#Recursion without memoization is useless
n = 40
time1 = time()
for x in range(n):

    fibo_recur(x)

time2 = time()
print(f"Recursive method  time for {n-1}th term is", time2 - time1, "seconds")
"""

