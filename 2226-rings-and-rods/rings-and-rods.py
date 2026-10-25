class Solution:
    def countPoints(self, rings: str) -> int:
        rc={}
        for  i in range(0,len(rings),2):
            color=rings[i]
            rod=rings[i+1]
            if rod not in rc:
                rc[rod]=set()
            rc[rod].add(color)
        count=0
        for rod in rc:
            if len(rc[rod])==3:
                count+=1
        return count 
        