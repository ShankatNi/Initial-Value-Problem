import math

def func(t,w):
    numFunc=((0.00004166667*t**4-0.00166666667*t**3+0.04975*t**2-0.995*t-0.049875)*w+(0.006666666668*t**3+0.001*t**2+4*t+0.2)*w**6+(-0.0066666667*t**4-0.080*t**3-0.812*t**2-0.8*t-0.002)*w**4+(0.32*t**3+0.064*t**4+0.048*t**2)*w**2-0.16*t**4)/(w**7)
    return numFunc

def func2(t,w):
    numFunc=(1/w**7)*((4.166666667*10**-8*t**4-0.0000166667*t**3+0.00499975*t**2-0.99995*t-0.004999875)*w**8+(0.0000666666668*t**3+1*10**-6*t**2+4*t+0.02*w**6+(-6.666666667*10**-6*t**4-0.0008*t**3-0.080012*t**2-0.0008*t-2*10**-6)*w**4+(0.0032*t**3+0.000064*t**4+0.000048*t**2)*w**2-0.00016*t**4))
    return numFunc
    
def AcutalFunc(t):
    ans=math.sqrt(4-3*(math.exp(-t)**2))
    return ans


def Taylor_4(a,b,h,x):
    N=int((b-a)/h)
    t=a
    W=list()
    W.append(1)  #int(input("Enter IVP:")))
    for cl in range(1,N+1):
        W.append(0)
    if h==0.1:
        for cl in range(1,N+1):
            W[cl]=W[cl-1]+h*func(t,W[cl-1])
            t=a+cl*h
    else:
       for cl in range(1,N+1):
            W[cl]=W[cl-1]+h*func2(t,W[cl-1])
            t=a+cl*h                                                                                                                                                                    
        #print(t,W[cl])
    print("T         W")
    print("----------------------")
    print(format(t,".2f"),"    ",W[len(W)-1])
    print()
    

    for cl in range(1,N+1):
        t=a+h*cl
    x=AcutalFunc(1)
    print("Actual Value is:",x)
    print()
    print("Actual Error")
    print(format(t,".2f"),"Value: |",x,"-",W[len(W)-1],"| =",abs(x-W[len(W)-1]))
    return abs(x-W[len(W)-1])

def main():
    a=0
    b=1
    h=0.1
    x=AcutalFunc(1)
    print("Actual Value is:",x)
    print("When h:",h)
    value1=Taylor_4(a,b,h,x)
    h=0.01
    print()
    print("When h:",h)
    value2=Taylor_4(a,b,h,x)
    print()
    print("Ratio:",value2,"/",value1,"=",value2/value1)



main()
