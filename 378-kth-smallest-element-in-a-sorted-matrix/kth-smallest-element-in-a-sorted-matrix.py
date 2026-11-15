import heapq

class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        flat_list = [element for row in matrix for element in row]
        heapq.heapify(flat_list)
        ans = 0
        for _ in range(k):
            ans = heapq.heappop(flat_list)
            
        return ans