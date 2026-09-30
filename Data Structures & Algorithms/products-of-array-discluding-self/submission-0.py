class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        Products = []
        prefix = []
        postfix = [1]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
            else:
                prefix.append(prefix[i-1]*nums[i-1])
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                postfix[i] = postfix[i] * 1
            else:
                postfix[i] = postfix[i+1]*nums[i+1]
        for i in range(len(nums)):
            Products.append(postfix[i]*prefix[i])
        return Products



                


            
            