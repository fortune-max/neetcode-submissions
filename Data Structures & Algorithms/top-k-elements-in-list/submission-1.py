class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict as d
        num_ct = d(int)
        for num in nums:
            num_ct[num] += 1
        import heapq
        h = []
        for num, ct in num_ct.items():
            heapq.heappush(h, (-ct, num))
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(h)[-1])
        return ans