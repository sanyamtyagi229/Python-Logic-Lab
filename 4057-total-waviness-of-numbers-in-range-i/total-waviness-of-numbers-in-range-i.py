class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        w=0
        for i in range(num1,num2+1):
            dig=str(i)
            l=len(dig)
            if l<3:
                continue
            for j in range(1,l-1):
                pd=int(dig[j-1])
                cd=int(dig[j])
                nd=int(dig[j+1])
                if cd>pd and cd>nd:
                    w+=1
                elif cd<pd and cd<nd:
                    w+=1
        return w
        