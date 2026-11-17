class Solution:
    def maxProduct(self, words: list[str]) -> int:
        def isuncommon(s1,s2):
            seen=set(s1)
            for char in s2:
                if char in seen:
                    return False
            return True
        maxp=0
        for i in range(len(words)):
            for j in range(i,len(words)):
                if isuncommon(words[i],words[j]):
                    maxp=max(len(words[i])*len(words[j]),maxp)
        return maxp
                    
                
        