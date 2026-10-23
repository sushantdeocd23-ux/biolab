import random

def f(x):
    return sum(i*i for i in x)       # Sphere function

n=10
pop=[[random.uniform(-5,5) for _ in range(2)] for _ in range(n)]

for _ in range(100):
    for i in range(n):
        a,b,c=random.sample([j for j in range(n) if j!=i],3)

        trial=[]
        for j in range(2):
            trial.append(pop[a][j]+0.8*(pop[b][j]-pop[c][j]))

        if f(trial)<f(pop[i]):
            pop[i]=trial

best=min(pop,key=f)

print("Best:",best)
print("Value:",f(best))