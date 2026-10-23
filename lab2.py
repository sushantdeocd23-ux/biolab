import random, math

def cost(r):
    return sum(abs(r[i]-r[i+1]) for i in range(len(r)-1)) + abs(r[-1]-r[0])

def sa(n):
    r=list(range(n))
    random.shuffle(r)
    best=r[:]
    T=100

    for _ in range(5000):
        x=r[:]
        a,b=random.sample(range(n),2)
        x[a],x[b]=x[b],x[a]

        d=cost(x)-cost(r)
        if d<0 or random.random()<math.exp(-d/T):
            r=x
        if cost(r)<cost(best):
            best=r[:]
        T*=0.995

    return best,cost(best)

r,c=sa(10)
print("Best Tour:",r)
print("Tour Length:",c)