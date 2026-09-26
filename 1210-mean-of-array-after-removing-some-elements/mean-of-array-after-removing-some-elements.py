class Solution:
    def trimMean(self, arr: list[int]) -> float:
        arr.sort()
        k=len(arr)//20
        remaining_elements = arr[k : -k]
        a=sum(remaining_elements)
        return a/len(remaining_elements)
        