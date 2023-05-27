#link - https://practice.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=check-if-an-array-is-sorted
def checkSortedArray(arr,n):
    if(n==0 or n==1):
        return True
    for i in range(1,n):
        if(arr[i-1]>arr[i]):
            return False
    return True 

arr=[1,4,2,5,6,7,8]
n=len(arr)
res=checkSortedArray(arr,n) 
print(res)
        

