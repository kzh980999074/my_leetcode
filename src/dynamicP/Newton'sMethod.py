

def newton_method(n,k):
    j=1
    p=1
    t=1
    if n>100:
        for i in range(3,100):
            if n<10**i:
                t=10**((i-1)//2)-1
                break
    s=n/t
    for i in range(k):
        s=s-(s*s-n)/(2*s)
    return s
print(newton_method(10000000000,10))
