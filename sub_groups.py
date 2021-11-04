def v(arr,arr1,a,a1,b,b1,c,c1):
    arr1.append(f(arr,a1))
    if a//b!=2 or  a1//b1!=1:
        if a//b > a1//b1+1:
            v(arr, arr1, a, a1+b1, b, b1, c, c1)
        elif a//b == a1//b1+1:
            v(arr, arr1, a1, a1+b1*c, b*c, b1*c, c, c1) 
def f(arr1,a):
    if isinstance(arr1[0], int):
        return a
    if a<=10:
        return arr1[a%10-1]
    return f(arr1,a//10)+f'{arr1[a%10-1]}'

def fun(arr,arr1,a,a1,b,b1,c,c1):
    arr1.append(f(arr,a))
    if c1 < c:
        if a//a1>=2:
            v(arr, arr1, a, a+b1, a1, b1, a1, b)
        fun(arr, arr1, a+1, a1, b, b1, c, c1+1)
    elif c!=0:
        if a//a1>=2:
            v(arr, arr1, a, a+b1, a1, b1, a1, b)
        fun(arr, arr1, a+b, a1, b+1,b1, c-1, 0)
    else:
        if a//a1>1:
            v(arr, arr1, a, a+b1, a1, b1, a1, b)
def add1(arr3,arr1,l,i,i1,j,j1):
    for i in range(len(arr3)):
        ls = len(arr1)
        arr1.append(arr3[i])
        for j in range(ls):
            arr1.append(str(arr1[j])+str(arr3[i]))
    arr1.append([])
        
def main():
    #     0   1   2   3   4   5   6   7   8    9   10   11   12
    arr=['~','!','@','#','$','%','^','&','*', '(',')' ,'_' , '+']
    arr1=[]
    arr3=[]
    if len(arr)>3:
        arr3 =arr[3:len(arr)]
        arr= arr[0:3]
    #              a  a1         b         b1        c     c1
    fun(arr, arr1, 1, 10, 10-(len(arr)-2), 100, len(arr)-1, 0)
    add1(arr3,arr1,len(arr)+len(arr3),0,len(arr3),0,len(arr1))
    print(arr1)
    print(len(arr1))

main()
































