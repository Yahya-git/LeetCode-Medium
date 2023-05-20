from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        initialArea = 0
        pointer1 = 0
        pointer2 = len(height) - 1
        while pointer1 <= len(height) - 1 and pointer2 >= 0:
            area = abs(pointer2 - pointer1) * min(height[pointer1], height[pointer2])
            if initialArea > area:
                area = initialArea
            else:
                initialArea = area
            if height[pointer1] <= height[pointer2]:
                pointer1 += 1
            else:
                pointer2 -= 1
        return area


sol = Solution()
print("sol", sol.maxArea(height=[2, 3, 4, 5, 18, 17, 6]))
print("sol", sol.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
print("sol", sol.maxArea(height=[1, 1]))
