nums=[19,8,7,6,5,4,3,2,1]


def selecction(nums):
    n=len(nums)
    for i in range(n):
        min=i
        for j in range(1+i,n):
            if nums[i]>nums[j]:
                min=j
        temp=nums[i]
        nums[i]=nums[min]
        nums[min]=temp



def bubble(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

nums=[19,8,7,6,5,4,3,2,1]
def insertion (nums):
    n=len(nums)
    for i in range(1,n):
        curr=nums[i]
        pos=i
        while curr<nums[pos-1] and pos>0:
            nums[pos]=nums[pos-1]
            pos-=1
        nums[pos]=curr















def mergesort(lists):
    if len(lists)>1:
        mid=len(lists)//2
        left=lists[:mid]
        right=lists[mid:]
        mergesort(left)
        mergesort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                lists[k]=left[i]
                i+=1
                k+=1
            else:
                lists[k]=right[j]
                j+=1
                k+=1
        while i < len(left):
            lists[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            lists[k]=right[j]
            j+=1
            k+=1



            
def bubble_sortrec(arr):
    n = len(arr)
    count=0
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            count+=1
    if count==0:
        return arr
    else:
        bubble_sortrec(arr)

arr = [64, 34, 25, 12, 22, 11, 90]


print(arr)
bubble_sortrec(arr)
print(arr)