class Solution:
    def reverseWords(self, s: str) -> str:
        word=s.split()
        rs=[]
        for i in word:
            a=i[::-1]
            rs.append(a)
        return " ".join(rs)


        