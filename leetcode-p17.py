from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        keyboard = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        if len(digits) == 1:
            answer = keyboard[f"{digits[0]}"]
        else:
            arrays = []
            for key in digits:
                if key in keyboard:
                    arrays.append(keyboard[key])
            answer = list(self.generateCombinations(arrays))
        return answer

    def generateCombinations(self, arrays, current_combination=[], index=0):
        if index == len(arrays):
            if current_combination:
                yield "".join(current_combination)
        else:
            for element in arrays[index]:
                current_combination.append(element)
                yield from self.generateCombinations(
                    arrays, current_combination, index + 1
                )
                current_combination.pop()


sol = Solution()
print("sol", sol.letterCombinations(digits=""))
