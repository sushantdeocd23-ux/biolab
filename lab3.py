import random

def f(x):
    return x*x + 10*(1) - 10*__import__('math').cos(2*__import__('math').pi*x)

n=20
p=[random.uniform(-5,5) for _ in range(n)]
v=[0]*n
best=min(p,key=f)
pb=p[:]

for _ in range(100):
    for i in range(n):
        v[i]=v[i]+2*random.random()*(pb[i]-p[i])+2*random.random()*(best-p[i])
        p[i]+=v[i]
        if f(p[i])<f(pb[i]): pb[i]=p[i]
    best=min(pb,key=f)

print("Best position:",best)
print("Best value:",f(best))