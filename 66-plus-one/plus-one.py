class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        for digit in digits:
            s+=str(digit)
        c=int(s)+1
        res=[]
        for i in str(c):
            res.append(int(i))
        return res

        