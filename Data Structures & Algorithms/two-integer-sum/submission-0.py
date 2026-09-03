class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        MyMap = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in MyMap:
                return [MyMap[difference], i]
            MyMap[n] = i
        
