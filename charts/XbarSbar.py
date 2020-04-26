import matplotlib.pyplot as pt
import statistics as st
import random

def makesamp(n,x):
    data=[[]]
    samp=0
    say=0
    if (n < 2 or x < 1):
        print("sample sayısı en az bir sample boyutu 2 den küçük olmamalıdır")
        quit()

    while samp<x:
        if(say==n):
            data.append([])
            say=0
            samp+=1
            continue
        try:
            print((samp+1),". sample",(say+1),". eleman :",end="")
            girilen = input()
            if(girilen == "b" and say != 0):
                say-=1
                print(say)
                continue
            data[samp].append(int(girilen))
        except ValueError as hata:
            print(hata)
            continue
        say+=1
    del data[-1]
    return data

def xbar(data):
    stddata = []

    xlın = [(i+1) for i in range(len(data))]
    for i,v in enumerate(data):
        data[i]=round(st.mean(v),4)
        stddata.append(round(st.stdev(v),4))

    xbarbar = st.mean(data)
    sbar = st.mean(stddata)
    a3 = 1.954
    
    pt.scatter(xlın,data)
    pt.plot(xlın,data,"xb-")
    pt.axhline(color="r",linewidth="1",y=xbarbar+sbar*a3)
    pt.axhline(color="r",linewidth="1",y=xbarbar)
    pt.axhline(color="r",linewidth="1",y=xbarbar-sbar*a3)
    pt.show()

def sbart(data):
    xlin = [(i+1) for i in range(len(data))]
    
    for i,v in enumerate(data):
        data[i]=round(st.stdev(v),4)
    sbarbar = st.mean(data)


 
try: # X : number of sample , N : Sample Size , this code block creates samples for chart
    n = int(input("sample size ?"))
    x = int(input("number of sample ?"))
    data = []
    temp = []
    for i in range(x):
        for i in range(n):
            temp.append(random.randint(1,100))
        data.append(temp)
        temp = []
    xbar(data)
except ValueError as hata:
    print(hata)