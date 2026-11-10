class Solution:
    def minCost(self, color: str, neededTime: list[int]) -> int:
        time=0
        i=0
        n=len(color)
        while i<n:
            cc=color[i]
            gs=0
            gm=0
            while i < n and color[i]==cc:
                gs+=neededTime[i]
                gm=max(gm,neededTime[i])
                i=i+1
            time+=gs-gm
        return time
        