class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        same = set()
        nums2 = {item: index for index, item in enumerate(nums)}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                c = -(nums[i] + nums[j])
                if c in nums2 and ((nums2.get(c) != i) and (nums2.get(c) != j)):
                    k = nums2.get(c)
                    key = tuple(sorted([nums[i], nums[k], nums[j]]))
                    if key not in same:
                        same.add(key)
                        solutions.append([nums[i], nums[k], nums[j]])
                    else:
                        continue
        return solutions
                



                
                    




