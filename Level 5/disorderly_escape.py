# Disorderly Escape
from collections import Counter

def count(c, n):
    cnt = factorial(n)
    for a, b in Counter(c).items():
        cnt //= (a**b)*factorial(b)
    return cnt

# All possible partitions of the integer
def partitions(n, i=1):
    yield(n,)
    for i in range(i, n//2 + 1):
        for p in partitions(n-i, i):
            yield(i,) + p

# faster gcd approach - Looked up the internet for Shen Algo.  
def gcd(u, v):
    shift = 0
    if u ==0:
        return v
    if v == 0:
        return u
    while(((u|v)&1)==0):
        shift += 1
        u >>= 1
        v >>= 1
    while((u&1)==0):
        u>>=1
    while (True):
        while (v&1)==0:
            v>>=1
        if u>v:
            u, v = v, u
        v -= u
        if(v==0):
            break
    return u<<shift

# Dp approach for factorial - Increasing Effectiveness
fact_dp = [0]*100000
fact_dp[0] = 1
fact_dp[1] = 1
def factorial(n):
    if fact_dp[n]!= 0:
        return fact_dp[n]
    else:
        
        for i in range(2, n+1):
            if fact_dp[i] == 0:
                break
        for j in range(i, n+1):
            fact_dp[j] = fact_dp[j-1]*j
        return fact_dp[n]
    
    
def solution(w, h, s):
    grid = 0
    for pw in partitions(w):
        for ph in partitions(h):
            m = count(pw, w)*count(ph, h)
            grid+=m*(s**sum([sum([gcd(i, j) for i in pw]) for j in ph]))

    return str(grid//(factorial(w)*factorial(h)))# Took me 20 mins in this single sentence

# Sample
print(solution(2,3,4))






















    

