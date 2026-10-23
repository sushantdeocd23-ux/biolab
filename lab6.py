import numpy as np

def f(x):
    return 10*len(x)+sum(x*x-10*np.cos(2*np.pi*x))

n,d=20,5
x=np.random.uniform(-5,5,(n,d))

for _ in range(100):
    for i in range(n):
        for j in range(n):
            if f(x[j])<f(x[i]):
                r=np.linalg.norm(x[i]-x[j])
                b=np.exp(-r*r)
                x[i]+=b*(x[j]-x[i])+0.2*(np.random.rand(d)-.5)
                x[i]=np.clip(x[i],-5,5)

best=min(x,key=f)

print("Best solution:",best)
print("Best fitness:",f(best))