class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0
        limit = 2**31
        if x > 0:
            while x > 0:
                lastDigit = x % 10
                reverse = (reverse * 10) + lastDigit
                x = int(x / 10)
            if reverse > limit:
                return 0
            return reverse
        else:
            x = abs(x)
            while x > 0:
                lastDigit = x % 10
                reverse = (reverse * 10) + lastDigit
                x = int(x / 10)
            if reverse > limit:
                return 0
            return -1 * reverse


sol = Solution()
print("sol", sol.reverse(x=123))
print("sol", sol.reverse(x=1534236469))
