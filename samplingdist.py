import random

def comb(n,x):
    pay = 1
    payda = 1
    for i in range(1,n+1):
        pay*=i
    for i in range(1,n-x+1):
        payda*=i
    for i in range(1,x+1):
        payda*=i
    return pay/payda

def expvalue(sample):
    return sum(sample)/len(sample)

def variance(sample):
    return sum([(i-expvalue(sample))**2 for i in sample])/(len(sample))

def variancesamp(sample):
    return sum([(i-expvalue(sample))**2 for i in sample])/(len(sample)-1)

def makexbar(sample):
    return [expvalue(i) for i in sample]

def sampvariance(sample):
    for i in range(len(sample)):
        print(sample[i],end=" ")
        sample[i] = round(variancesamp(sample[i]),4)
        print(sample[i])
    prb = 1/len(sample)
    result = 0
    for i in sample:
        result += i*prb
    return result

def sampwr(sample,n):
    samp = []
    while len(samp) < len(sample)**n:
        temp = random.choices(sample,k=n)
        if not temp in samp:
            samp.append(temp)
        else:
            temp.clear()
    return samp

def sampwor(sample,n):
    tsamp = list(sample)
    samp = []

    times = int(comb(len(sample),n))
    print(times,"possible outcome :")
    i = 0
    b = 0
    j = []
    kontrol = True

    while i < times:
        for x in range(n):
            temp = random.choice(tsamp)
            j.append(temp)
            del tsamp[tsamp.index(temp)]
            #print(tsamp)
        for x in samp:
            for c in x:
                if c in j:
                    b+=1
            if b == n:
                b = 0
                kontrol = False
                break
            b = 0
        if not kontrol:
            kontrol = True
            j = []
            tsamp = list(sample)
            continue
        else:
            samp.append(j[::])
            tsamp = list(sample)
            j = []
            b = 0
            i+=1
    #print(*samp,sep="\n")
    return samp


n = int(input("örneklem boyutunu giriniz : "))
population = [2,0,-1,4]

sample = sampwr(population,n)
print(*sample,sep="\n")

print("******************")
print("XBARS")
for i in makexbar(sample[::]):
    print(round(i,4))
print("******************")
print("SBARS")

print("E(s**2) =",round(sampvariance(sample[::]),4))
print("e(xbar) =",round(expvalue(makexbar(sample[::])),4))
print("e(xbar**2) =",round(expvalue([i**2 for i in makexbar(sample[::])]),4))
print("V(xbar) =",round(variance(makexbar(sample[::])),4))
print("variance pop",variance(population))

