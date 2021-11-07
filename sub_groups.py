def subGroup(arr,arr1 = [[]]):
    for i in range(len(arr)):
        for j in range(len(arr1)):
            arr1.append(arr1[j][:len(arr1[j])]+arr[i:i+1])

def main():
    #     0   1   2   3   4 
    arr=['1','2','3','4','5']
    s = [[]]
   
    subGroup(arr,s)
    print(s,len(s))

main()































