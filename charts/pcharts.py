import matplotlib.pyplot as pt
import statistics as st

def pchart(data,sampsize): # p chart
    if not type(data) is list or len(data) <= 1 or sampsize <= 1:
        print("data you entered must be a list ")
        print("length of list must be at least 1")
        print("sample size must be at least 2")
        quit()
    xlin = [(i+1) for i in range(len(data))]
    ylin = [i/sampsize for i in data]
    pcap = st.mean(ylin)
    q = 1-pcap

    ucl = pcap + 3*(pcap*q)**1/2
    lcl = pcap - 3*(pcap*q)**1/2

    print(ucl,pcap,lcl,sep="\n")
    
    pt.scatter(xlin,ylin)
    pt.plot(xlin,ylin)
    pt.axhline(color="red",linewidth=1,y=ucl)
    pt.axhline(color="red",linewidth=1,y=pcap)
    pt.axhline(color="red",linewidth=1,y=lcl)
    pt.show()

def npchart(data,sampsize): # np chart
    if not type(data) is list or len(data) <= 1 or sampsize <= 1:
        print("data you entered must be a list")
        print("length of list must be at least 1")
        print("sample size must be at least 2")
        quit()

    xlin = [(i+1) for i in range(len(data))]
    ylin = [i for i in data]

    np = st.mean(ylin)
    pcap = np/sampsize

    ucl = np + 3*(sampsize*pcap*(1-pcap))**1/2
    lcl = np - 3*(sampsize*pcap*(1-pcap))**1/2

    pt.scatter(xlin,ylin)
    pt.plot(xlin,ylin)
    pt.axhline(color="red",linewidth=1,y=ucl)
    pt.axhline(color="red",linewidth=1,y=np)
    pt.axhline(color="red",linewidth=1,y=lcl)
    pt.show()

import random as rd

pchart([12,6,8,9,10,12,11,16,10,6],100) # Sample Data