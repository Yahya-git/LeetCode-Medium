from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        self.generateCombinations(nums, [], answer, set())
        return answer

    def generateCombinations(self, nums, path, answer, used):
        if len(path) == len(nums):
            answer.append(path)
        else:
            for i in range(len(nums)):
                if i not in used:
                    used.add(i)
                    self.generateCombinations(nums, path + [nums[i]], answer, used)
                    used.remove(i)


sol = Solution()
print("sol", sol.permute(nums=[1, 2, 3]))
