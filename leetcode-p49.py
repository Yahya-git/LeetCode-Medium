from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        map = {}
        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord not in map:
                map[sortedWord] = []
            map[sortedWord].append(word)
        print(map)
        answer = list(map.values())
        return answer


sol = Solution()
print("sol", sol.groupAnagrams(strs=["tea", "ate", "eat", "ten", "net"]))
