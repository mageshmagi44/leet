def topk(nums,k):
    map={}
    bucket=[[] for i in range(len(nums)+1)]
    for i in nums:
        map[i]=1+map.get(i,0)
    for i,n in map.items():
        bucket[n].append(i)
    print(map)
    print(bucket)
    ans=[]
    for i in range(len(bucket)-1,0,-1):
        for n in bucket[i]:
            ans.append(n)
            if len(ans)==k:
                print(ans)
                return



nums=[1,1,2,2,2,3,3,3,3]
k=2

topk(nums,k)