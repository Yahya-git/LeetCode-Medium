class Solution:
    def intToRoman(self, num: int) -> str:
        values = {
            1: "I",
            2: "II",
            3: "III",
            5: "V",
            6: "VI",
            7: "VII",
            8: "VIII",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
            4: "IV",
            9: "IX",
            40: "XL",
            90: "XC",
            400: "CD",
            900: "CM",
        }

        answer = ""

        for value in sorted(values.keys(), reverse=True):
            while num >= value:
                answer += values[value]
                num -= value

        return answer


sol = Solution()
print("sol", sol.intToRoman(num=2994))
