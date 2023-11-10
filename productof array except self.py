def productExceptSelf(nums):
    ans=[0]*len(nums)
    pre=1
    for i in range(len(nums)):
        ans[i]=pre
        pre=pre*nums[i]
        print(pre)
        print(ans)
    suf=1
    for i in range(len(nums)-1,-1,-1):
        ans[i]*=suf
        suf=suf*nums[i]
    print(ans)
    return 



nums= [1,2,3,4]
productExceptSelf(nums)