class Solution:
    def splitNum(self, num: int) -> int:
        l = []
        while num > 0:
            d = num % 10
            l.append(str(d)) 
            num = num // 10
        
        l.sort()
        
        num1_str = ""
        num2_str = ""
        for i in range(len(l)):
            if i % 2 == 0:
                num1_str += l[i]
            else:
                num2_str += l[i]
                
        return int(num1_str) + int(num2_str)