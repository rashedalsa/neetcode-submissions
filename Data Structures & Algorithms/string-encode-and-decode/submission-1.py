class Solution:

    def encode(self, strs: List[str]) -> str:
        mString = ""
        for string in strs:
            newString = str(len(string)) + "|" + string
            mString += newString
        return mString

    def decode(self, s: str) -> List[str]:
        NewList = []
        i = 0
        while i < len(s):
            Del = s.find("|", i)
            length = int(s[i:Del])
            neWord = s[Del + 1:(Del + 1) + length]
            NewList.append(neWord)
            i = (Del + 1) + length
        return NewList


