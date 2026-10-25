class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        x = bin(a)
        y = bin(b)
        s1 = 0
        s2 = 0
        for i in x:
            if i == '1':
                s1 += 1
        for j in y:
            if j == '1':
                s2 += 1
        if s1 >= s2:
            return s1 * s2
        else:
            return s2 // s1