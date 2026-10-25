class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        groups = {}
        answer = []

        for person in range(len(groupSizes)):
            x = groupSizes[person]

            if x not in groups:
                groups[x] = []

            groups[x].append(person)

            if len(groups[x]) == x:
                answer.append(groups[x])
                groups[x] = []

        return answer