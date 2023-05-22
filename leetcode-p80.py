from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer1 = 0
        pointer2 = 1
        count = 1

        while pointer2 < len(nums):
            if nums[pointer2] == nums[pointer1]:
                count += 1
                if count > 2:
                    nums.pop(pointer2)
                else:
                    pointer2 += 1
            else:
                count = 1
                pointer1 = pointer2
                pointer2 += 1

        print(nums)
        return len(nums)


sol = Solution()
print("sol", sol.removeDuplicates(nums=[0, 0, 1, 1, 1, 1, 2, 3, 3]))
print("sol", sol.removeDuplicates(nums=[1, 1, 1, 1]))
