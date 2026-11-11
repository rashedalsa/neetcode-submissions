class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, n in enumerate(temperatures):
            if not stack or n <= temperatures[stack[-1]]:
                stack.append(i)
                continue
            if n > temperatures[stack[-1]]:
                while stack and n > temperatures[stack[-1]]:
                    j = stack.pop()
                    result[j] = i - j
                stack.append(i)
        return result


                     

 
            
            
            

        