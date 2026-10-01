class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        Answer = []
        index1 = 0
        index2 = len(numbers) - 1

        while index1 < index2:
            if numbers[index1] + numbers[index2] < target:
                index1 += 1
                continue
            if numbers[index1] + numbers[index2] > target:
                index2 -= 1
                continue
            if numbers[index1] + numbers[index2] == target:
                Answer.append(index1 + 1)
                Answer.append(index2 + 1)
                break

        return Answer            
            
        