#link - https://practice.geeksforgeeks.org/problems/second-largest3735/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=second-largest
# Brute force 
# t.c -O(nlogn) s.c-O(1)
def secondLargestElement(arr,n):
    arr.sort()
    largest=arr[n-1]
    for i in range(n-1,-1,-1):
        if(arr[i]!=largest):
            second_largest=arr[i]
            return second_largest

#better solution
# t.c -O(n)+O(n)  s.c-O(1)
def secondLargestElement(arr,n):
    largest=arr[0]
    for i in range(1,len(arr)):
        if(arr[i]>largest):
            largest=arr[i]
    second_largest=-1
    for i in range(len(arr)):
        if(arr[i]>second_largest and arr[i]!=largest):
            second_largest=arr[i]
    return second_largest

#optimal Solution
#T.c.- O(n)  S.c-O(1)
def secondLargestElement(arr,n):
    largest=arr[0]
    second_largest=-1
    for i in range(len(arr)):
        if(arr[i]>largest):
            second_largest=largest 
            largest=arr[i]
        elif(arr[i]>second_largest and largest>arr[i]):
            second_largest=arr[i]
    return [largest,second_largest]



arr=[100, 10, 40, 30, 100]
n=len(arr)
res=secondLargestElement(arr,n)
print(res)


