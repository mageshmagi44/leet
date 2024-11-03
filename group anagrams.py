def groupana(ans):
    map={}
    for i in ans:
        s="".join(sorted(i))
        if s in map:
            map[s].append(i)
        else:
            map[s]=[i]djdj


    print(map)
    res=[]
    for i in map.values():
        res.append(i)

    print(res)
    return 

        













aaa=["eat","tea","tan","ate","nat","bat"]
groupana(aaa)