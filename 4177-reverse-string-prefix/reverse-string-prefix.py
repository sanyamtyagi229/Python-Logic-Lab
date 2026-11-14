class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        i=0
        j=k-1
        string=list(s)
        while(i<j):
            string[i],string[j]=string[j],string[i]
            i=i+1
            j=j-1
        return "".join(string)
        
            
        