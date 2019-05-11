import math

def func(t,w):
    numFunc=(-t)*w+4*t*(2**(-1))
    return numFunc

def AcutalFunc(t):
    ans=math.sqrt(4-3*(math.exp(-t)**2))
    return ans

def Heun(a,b,h,x):
    N=int((b-a)/h)
    t=a
    W=list()
    W.append(1)  #int(input("Enter IVP:")))
    for cl in range(1,N+1):
        W.append(0)

    for cl in range(1,N+1):
        W[cl]=W[cl-1]+(h/4)*(func(t,W[cl-1])+3*func(t+(2/3)*h,W[cl-1]+(2/3)*h*func(t+h/3,W[cl-1]+(h/3)*func(t,W[cl-1]))))
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
    a=0 #int(input("Enter a:"))
    b=1 #int(input("Enter b:"))
    h=0.1
    x=AcutalFunc(1)
    print("Actual Value is:",x)
    print("When h:",h)
    value1=Heun(a,b,h,x)
    h=0.01
    print()
    print("When h:",h)
    value2=Heun(a,b,h,x)
    print()
    print("Ratio:",value2,"/",value1,"=",value2/value1)

main()
