def comb(n,x): # C(n,x) combination
    pay = 1
    payda = 1
    for i in range(1,n+1):
        pay*=i
    for i in range(1,n-x+1):
        payda*=i
    for i in range(1,x+1):
        payda*=i
    return pay/payda

def binom(n,p,x): # binomial distribution
    q = 1-p
    result = comb(n,x)*(p**x)*(q**(n-x))
    return result
    
def acceptance1(n,d,p):
    d = [i for i in range(d+1)]
    result = 0

    for i in d:
        result += binom(n,p,i)

    return round(result,4)

def acceptance2(n1,c1,n2,sinir,p): # two-fold acceptance sampling
    d1 = [i for i in range(c1+1)]
    result = 0

    for i in d1:
        result+=binom(n1,p,i)
    
    d1 = d1[-1]+1
    while(d1<=sinir):
        d2 = sinir-d1
        result+=binom(n1,p,d1)*acceptance1(n2,d2,p)
        d1+=1
    
    return round(result,6)

a = [0.01,0.05,0.1,0.2] # Probabilities
try:
    n1 = int(input("n1 sample size = "))
    c1 = int(input("c1 number of defective = "))
    n2 = int(input("n2 sample size = "))
    sinir = int(input("d1 + d2 <= ? "))

    print("{:<15} {:<15} {:<15} {:<15} {:<15}".format("P",*a))
    print(" "*15,end="")
    for i,v in enumerate(a):
        print("{:<15}".format(acceptance2(n1,c1,n2,sinir,a[i])),end="")
except ValueError:
    print("you should type integer only")
