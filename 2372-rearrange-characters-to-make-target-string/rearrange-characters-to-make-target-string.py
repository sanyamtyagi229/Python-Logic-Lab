class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        char_count=[0]*26
        for i in s:
            char_count[ord(i)-ord('a')]+=1
        target_count=[0]*26
        for i in target:
            target_count[ord(i)-ord('a')]+=1
        unique_chars = set(target)
        m=float('inf')
        for i in unique_chars:
            ind=ord(i)-ord('a')
            ps=char_count[ind]//target_count[ind]
            m=min(m,ps)
        return m
        
            
        