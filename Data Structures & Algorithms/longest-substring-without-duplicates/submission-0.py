class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        CurrMax = 0
        seen = {}
        l, r = 0, 0
        dupe = 0
        for r, n in enumerate(s):
            if s[r] in seen:
                dupe = seen[s[r]]
                for i in range(l, seen[s[r]] + 1):
                    del seen[s[i]]
                l = dupe + 1
            seen[s[r]] = r
            if len(s[l:r+1]) > CurrMax:
                CurrMax = len(s[l:r+1])
        return CurrMax