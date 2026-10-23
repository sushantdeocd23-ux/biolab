import random

def fitness(s):
    n=len(s); total=n*(n-1)//2; attack=0
    for i in range(n):
        for j in range(i+1,n):
            if s[i]==s[j] or abs(s[i]-s[j])==abs(i-j):
                attack+=1
    return total-attack

def neighbors(s):
    n=len(s); N=[]
    for c in range(n):
        for r in range(n):
            if s[c]!=r:
                x=s[:]; x[c]=r; N.append(x)
    return N

def hill(s):
    f=fitness(s)
    while True:
        N=neighbors(s)
        x=max(N,key=fitness); xf=fitness(x)
        if xf<=f: return s,f
        s,f=x,xf

def restart(n, times=500):
    best,bf=None,-1
    for _ in range(times):
        s=[random.randrange(n) for _ in range(n)]
        s,f=hill(s)
        if f>bf: best,bf=s,f
        if f==n*(n-1)//2: break
    return best,bf

def print_board(s):
    for r in range(len(s)):
        print(" ".join("Q" if s[c]==r else "." for c in range(len(s))))

n=8
s,f=restart(n)
print("Solution:",s)
print("Fitness:",f)
print("Valid Solution" if f==n*(n-1)//2 else "Local Maxima")
print_board(s)