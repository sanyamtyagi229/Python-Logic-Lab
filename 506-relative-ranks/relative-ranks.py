class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        n = len(score)
        sorted_scores = sorted(score, reverse=True)
        
        answer = []
        for s in score:
            rank = sorted_scores.index(s) + 1  # 1-based rank
            
            if rank == 1:
                answer.append("Gold Medal")
            elif rank == 2:
                answer.append("Silver Medal")
            elif rank == 3:
                answer.append("Bronze Medal")
            else:
                answer.append(str(rank))
                
        return answer