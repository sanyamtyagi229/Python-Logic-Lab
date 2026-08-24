class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mind=float('inf')
        for i in range(len(arr)-1):
            if (arr[i+1]-arr[i])<mind:
                mind=(arr[i+1]-arr[i])
        result=[]
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] == mind:
                result.append([arr[i], arr[i+1]])
        return result