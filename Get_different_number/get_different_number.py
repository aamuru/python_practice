
def get_different_number(arr):
    l = len(arr)
    # print(l)

    for i in range(l):
    
        temp = arr[i]
        print(temp)
        while(temp < l and arr[temp] != temp):
            arr[temp], temp = temp, arr[temp]

    for i in range(l):
        if i != arr[i]:
            return i

    return l


arr = [7, 1, 2, 3, 8, 0]



#ans=4

print(get_different_number(arr))
