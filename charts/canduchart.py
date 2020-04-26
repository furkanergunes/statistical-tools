from matplotlib import pyplot as pt
import math as mt 

def cchart(c,n): # C chart
    cbar = sum(c)/len(c)
    ucl = cbar + 3*(cbar)**1/2
    lcl = cbar - 3*(cbar)**1/2

    xlin = [*range(1,len(c)+1)]

    pt.scatter(xlin,c)
    pt.plot(xlin,c)
    pt.axhline(color="red",linewidth=1,y=ucl)
    pt.axhline(color="red",linewidth=1,y=cbar)
    pt.axhline(color="red",linewidth=1,y=lcl)
    pt.show()



def uchart(c,n): # U chart
    ubar = sum(c)/(len(c)*n)
    ucl = ubar + 3*mt.sqrt(ubar/n)
    lcl = ubar - 3*mt.sqrt(ubar/n)
    print(ubar,ucl,lcl)
    
    xlin = [*range(1,len(c)+1)]
    c = [i/n for i in c]

    pt.scatter(xlin,c)
    pt.plot(xlin,c)
    pt.axhline(color="red",linewidth=1,y=ucl)
    pt.axhline(color="red",linewidth=1,y=ubar)
    pt.axhline(color="red",linewidth=1,y=lcl)
    pt.show()


liste = [21,24,16,12,15,5,28,20,31,25,20,24] # Sample Data
uchart(liste,100)