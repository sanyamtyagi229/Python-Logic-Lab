class Solution:
    def maxFreqSum(self, s: str) -> int:
        dicv={}
        dict={}
        for x in s:
            if x =='a'or x=='e'or x=='i'or x=='u' or x=='o':
                if x in dicv:
                    dicv[x]+=1
                else:
                    dicv[x]=1
            else:
                if x in dict:
                    dict[x]+=1
                else: 
                    dict[x]=1
        m=0
        for x, c in dict.items():
            m=max(m,c)
        n=0
        for x,c in dicv.items():
            n=max(n,c)
        return m+n

        