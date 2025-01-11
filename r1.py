'''
for i in range(1,4):
    print(i)
    fa=float(input("fa="))
    ce=5*(fa-32)/9
    print("fa=%f,ce=%f"%(fa,ce))
'''
'''
i=1
while i<=3:
    print(i)
    fa=float(input("fa="))
    ce=5*(fa-32)/9
    print("fa=%f,ce=%f"%(fa,ce))
    i=i+1
while i==4:
    print("End")
    i=i+1
while i<=3:
    print(i)
    fa=float(input("fa="))
    ce=5*(fa-32)/9
    print("fa=%f,ce=%f"%(fa,ce))
    i=i+1
while i==4:
    print("End")
    i=i+1
    '''
'''
def f1(x):
    result = 1
    for i in range(1,x+1):
        result = result * i
    return result
for i in range(0,9):
    num=int(input("num="))
    print("f1(%d)=%d"%(num,f1(num)))
'''
'''
def f1(x):
    return 5*(x-32)/9
for i in range(1,6):
    fa=float(input("fa="))
    ce=f1(fa)
    print("fa=%f,ce=%f"%(fa,ce))
'''
'''
def f1(x):
    if x <0:
        return -1
    elif x==0 or x==1:
        return 1
    else:
        return f1(x-1) * x
for i in range(0,9):
    num=int(input("num="))
    if num>=0:
        print("f1(%d)=%d"%(num,f1(num)))
    else:
        print("Error")
        '''
'''
original_price=float(input("original price="))
discount=float(input("discount="))
current_price=original_price*(discount)
print("current price=%f"%current_price)
'''
'''
import math
accumulate=math.pow(1+0.01,365)
lazy=math.pow(1-0.01,365)
print("accumulate=%f,lazy=%f"%(accumulate,lazy))
'''
'''
import math
accumulatelazy=math.pow(1+0.01,3)*math.pow(1-0.01,2)
print("accumulatelazy=%f"%math.pow(accumulatelazy,365/5))
'''
'''
def hamster_grain(N, n):
    if n == 0:
        return N
    else:
        if N % 2 == 0:
            return hamster_grain(N/2, n-1)
        else:
            if N==1:
                return hamster_grain(0, n+1)
            else:
            return hamster_grain(N-(N+1)/2, n-1)
while True:
    N = int(input("N="))
    n = int(input("n="))
    print("left=%d" % hamster_grain(N, n))
'''
def test(i,j,m,n):
    if i-m==j-n or i+j==n+m:
            return False
    if j==n:
        return False
    if i+j==m+n:
        return False
    return True
def Test(row,col):
    for i in range(0,row):
        U=test(i,queen[i],row,col)
        if U==False:
            return False
    return True
row = 0
col = 0
queen=[]
sum=0
n=int(input("n="))
while row>=0:
    if col==n:
        if row==0:
            break
        col=queen[-1]+1
        queen.pop()
        row=row-1
        if col>=n:
            continue
    u=Test(row,col)
    if u==False:
        col=col+1
    if u==True: 
        queen.append(col)
        row=row+1
        col=0
        if row==n:
            print(queen)
            sum=sum+1
            col=queen[-1]+1
            queen.pop()
            row=row-1

print("sum=%d"%sum)