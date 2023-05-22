from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            min = i
            for j in range(i + 1, len(nums)):
                if nums[min] > nums[j]:
                    min = j
            nums[i], nums[min] = nums[min], nums[i]
        print(nums)


sol = Solution()
print("sol", sol.sortColors(nums=[2, 0, 2, 1, 0, 1]))
