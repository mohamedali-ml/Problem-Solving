class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        result = {}
        for num in arr:
            result[num] = 0
        for num in arr:
            result[num] += 1
        s = sorted(list(result.values()))
        if len(s) == 1:
            return True
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                return False
        return True