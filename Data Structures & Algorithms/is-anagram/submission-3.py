class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        MapS = {}
        MapT = {}
        for i in s:
            if i in MapS:
                MapS[i] += 1
            else:
                MapS[i] = 1
        for i in t:
            if i in MapT:
                MapT[i] += 1
            else:
                MapT[i] = 1
        if MapS == MapT:
            return True
        else:
            return False
        