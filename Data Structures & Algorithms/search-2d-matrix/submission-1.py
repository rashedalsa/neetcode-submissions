class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        myList = sum(matrix, [])
        l, r = 0, len(myList) - 1
        while l <= r:
            mid  = (l + r) // 2
            if myList[mid] == target:
                return True
            if myList[mid] < target:
                l = mid + 1
            if myList[mid] > target:
                r = mid - 1
        return False
        