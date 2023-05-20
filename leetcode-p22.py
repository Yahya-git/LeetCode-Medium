from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        self.recursiveGenerator(n, n, "", answer)
        return answer


    def recursiveGenerator(self, openPar, closePar, currentCombination, answer):
        if openPar == 0 and closePar == 0:
            answer.append(currentCombination)
            return
        if openPar > 0:
            self.recursiveGenerator(openPar-1, closePar, currentCombination+"(", answer)
        if closePar > openPar:
            self.recursiveGenerator(openPar, closePar-1, currentCombination+")", answer)


sol = Solution()
print("sol", sol.generateParenthesis(n=3))