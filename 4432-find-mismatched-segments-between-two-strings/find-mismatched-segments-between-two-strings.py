class Solution(object):
    def findMismatchedSegments(self, s1, s2):
        res=[]
        i=0
        n=len(s1)
        while i<n :
            j=i
            while j<n and s1[j]!=s2[j]:
                j+=1
            if i!=j:
                res.append([s1[i:j],s2[i:j]])
            i=j+1
        return res
            

            
            