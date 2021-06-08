from math import gcd
def abc(k,n,l): # 2 0 3
    if n==0:
        return
    else:
        x=k+n**2
        if l==0:
            l=x
            return abc(k,n-1,l)
        s.append(gcd(x,l))
        l=x
        return abc(k,n-1,l)
for i in range(int(input("test cases: "))):
    k=int(input("value of k: "))
    n=2*k+1
    l=0
    s=[]
    abc(k,n,l)
    print(sum(s))