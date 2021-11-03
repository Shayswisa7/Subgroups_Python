def v(arr,arr1,a,a1,b,b1,c):
    arr1.append(f(arr,a1))
    if a//b!=2 or  a1//b1!=1:
        if a//b > a1//b1+1:
            v(arr, arr1, a, a1+b1, b, b1, c)
        elif a//b == a1//b1+1:
            v(arr, arr1, a1, a1+b1*c, b*c, b1*c, c) 
def fun(arr,arr1,a,a1,b,b1,c,c1):
    arr1.append(f(arr,a))
    if c1 < c:
        if a//a1>=2:
            v(arr, arr1, a, a+b1, a1, b1, a1)
        fun(arr, arr1, a+1, a1, b, b1, c, c1+1)
    elif c!=0:
        if a//a1>=2:
            v(arr, arr1, a, a+b1, a1, b1, a1)
        fun(arr, arr1, a+b, a1, b+1,b1, c-1, 0)
    else:
        if a//a1>1:
            v(arr, arr1, a, a+b1, a1, b1, a1)
        arr1.append([])
def f(arr1,a):
    if isinstance(arr1[0], int):
        return a
    if a<=10:
        return arr1[a%10-1]
    return f'{arr1[a%10-1]}'+f(arr1,a//10)
arr=['@','*','&','$']
arr1=[]
#              a  a1         b         b1        c     c1
fun(arr, arr1, 1, 10, 10-(len(arr)-2), 100, len(arr)-1, 0)

print(arr1)




































