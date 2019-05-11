import math

def func(t,w):
    numFunc=-t*w+(4*t/w)+(0.05*((t**2-1)*w**4+4*w**2-16*t**2))/(w**3)
    return numFunc

def func2(t,w):
    numFunc=-t*w+(4*t/w)+(0.005*((t**2-1)*w**4+4*w**2-16*t**2))/(w**3)
    return numFunc
    
def AcutalFunc(t):
    ans=math.sqrt(4-3*(math.exp(-t)**2))
    return ans
    
def Taylor(a,b,h,x):
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
            #print(t,W[cl])
    else:
        for cl in range(1,N+1):
            W[cl]=W[cl-1]+h*func2(t,W[cl-1])
            t=a+cl*h
    print("T         W")
    print("----------------------")
    print(format(t,".2f"),"    ",W[len(W)-1])
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
    print()
    value1=Taylor(a,b,h,x)
    h=0.01
    print()
    print("When h:",h)
    value2=Taylor(a,b,h,x)
    print()
    print("Ratio:",value2,"/",value1,"=",value2/value1)
main()
