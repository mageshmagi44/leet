s="swt"
t="ats"
def anagram(s,t):
    if len(s)!=len(t):
        return False
    smap={}
    tmap={}
    for i in range(len(s)):
        smap[s[i]]=1+smap.get(i,0)
        tmap[t[i]]=1+tmap.get(i,0)

    for i in t:
        if smap.get(i,0)!=tmap[i]:
            print (False)
            return
        print(True)
        return True
    


anagram(s,t)