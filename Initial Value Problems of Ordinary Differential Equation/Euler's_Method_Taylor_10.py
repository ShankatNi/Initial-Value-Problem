import math

def func(t,w):
    numFunc=(t-w*(t**2)-(w**2)*(t**3)-0.075+0.075*(w**2)*(t**2)+0.05*(w**3)*(t**3))/t**3
    return numFunc




def main():
    a=1 #int(input("Enter a:"))
    b=2 #int(input("Enter b:"))
    h=0.05
    N=int((b-a)/h)
    t=a
    W=list()
    W.append(-1)  #int(input("Enter IVP:")))
    for cl in range(1,N+1):
        W.append(0)

    print("t","     w")
    print("------------------")
    for cl in range(0,N+1):
        W[cl]=W[cl-1]+h*func(t,W[cl-1])
        t=a+cl*h
        print(format(t,".2f"),W[cl])
    print()
 



main()
