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


'''s = [[],
       ['1'],
       ['2'], ['1', '2'],
       ['3'], ['1', '3']['2', '3'], ['1', '2', '3'],
       ['4'], ['1', '4'],['2', '4'], ['1', '2', '4'], ['3', '4'], ['1', '3', '4'], ['2', '3', '4'], ['1', '2', '3', '4'],
       ['5'], ['1', '5'],['2', '5'], ['1', '2', '5'], ['3', '5'], ['1', '3', '5'],['2', '3', '5'], ['1', '2', '3', '5'], ['4', '5'], ['1', '4', '5'],['2', '4', '5'],
       ['1', '2', '4', '5'], ['3', '4', '5'], ['1', '3', '4', '5'],['2', '3', '4', '5'], ['1', '2', '3', '4', '5']] len(s) = 32'''




























