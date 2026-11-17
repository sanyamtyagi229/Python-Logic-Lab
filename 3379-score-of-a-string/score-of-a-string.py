class Solution:
    def scoreOfString(self, s: str) -> int:
        su=0
        for i in range(len(s)-1):
            diff=abs(ord(s[i+1])-ord(s[i]))
            su=su+diff
        return su
    