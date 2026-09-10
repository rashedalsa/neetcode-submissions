class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Freq = {}
        for n in nums:
            Freq[n] = Freq.get(n, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in Freq.items():
            buckets[count].append(num)

        res = []
        for count in range(len(buckets) - 1, 0, -1):
            for num in buckets[count]:
                res.append(num)
                if len(res) == k:
                    return res
        return res