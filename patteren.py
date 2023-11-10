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


print(nums)
insertion(nums)
print(nums)
    