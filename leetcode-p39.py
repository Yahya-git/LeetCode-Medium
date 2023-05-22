from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        self.generateCombinations(candidates, target, [], answer, 0)
        return answer

    def generateCombinations(
        self, candidates, target, current_combination, answer, start
    ):
        if target == 0:
            answer.append(current_combination[:])
        elif target < 0:
            return
        else:
            for i in range(start, len(candidates)):
                element = candidates[i]
                current_combination.append(element)
                self.generateCombinations(
                    candidates, target - element, current_combination, answer, i
                )
                current_combination.pop()


sol = Solution()
print("sol", sol.combinationSum(candidates=[2, 3, 4, 7, 8], target=7))
