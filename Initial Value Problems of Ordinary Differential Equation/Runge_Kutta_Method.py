import math

def func(t,w):
    numFunc=(-t)*w+4*t*(2**(-1))
    return numFunc

def AcutalFunc(t):
    ans=math.sqrt(4-3*(math.exp(-t)**2))
    return ans

def Runge(a,b,h,x):
    N=int((b-a)/h)
    t=a
    W=list()
    W.append(1)  #int(input("Enter IVP:")))
    for cl in range(1,N+1):
        W.append(0)

    for cl in range(1,N+1):
        k1=h*func(t,W[cl-1])
        k2=h*func(t+h/2,W[cl-1]+k1/2)
        k3=h*func(t+h/2,W[cl-1]+k2/2)
        k4=h*func(t+h,W[cl-1]+k3)
        W[cl]=W[cl-1]+(1/6)*(k1+2*k2+2*k3+k4)
        t=a+cl*h
        #print(format(t,".2f"),W[cl])
    print("T         W")
    print("----------------------")
    print(format(t,".2f"),"    ",W[len(W)-1])
    print()

    for cl in range(1,N+1):
        t=a+h*cl

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
    value1=Runge(a,b,h,x)
    h=0.01
    print()
    print("When h:",h)
    value2=Runge(a,b,h,x)
    print()
    print("Ratio:",value2,"/",value1,"=",value2/value1)



main()
