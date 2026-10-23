import numpy as np

def f(x):
    return sum(x*x)

n,d,g=20,5,100
p=np.random.uniform(-5,5,(n,d))

for _ in range(g):
    fit=np.array([f(x) for x in p])
    best=p[np.argmin(fit)].copy()

    for i in range(n):
        for j in range(d):
            if np.random.rand()<0.5:
                p[i,j]=best[j]

        if np.random.rand()<0.05:
            p[i]=np.random.uniform(-5,5,d)

    fit=np.array([f(x) for x in p])
    p=p[np.argsort(fit)[:n]]

best=p[np.argmin([f(x) for x in p])]

print("Best Solution:",best)
print("Best Fitness:",f(best))