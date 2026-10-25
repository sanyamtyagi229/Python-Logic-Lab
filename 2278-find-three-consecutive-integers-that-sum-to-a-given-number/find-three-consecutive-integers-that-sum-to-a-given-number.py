class Solution:
    def sumOfThree(self, num: int) -> list[int]:
        if num%3!=0:
            return []
        else:
            return[(num//3)-1,num//3,(num//3)+1]
        