
#brute force 
def largestElement(arr,n):
    arr.sort()
    return arr[n-1]

#Optimal solution.
def largestElement(arr,n):
    largest=arr[0]
    for i in range(n):
        if(arr[i]>largest):
            largest=arr[i]
    return largest

arr=[20, 10, 20, 4, 100]
n=len(arr)
res=largestElement(arr,n)
print(res)