class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_ct = [0] * 2001 # [0] => -1000, [2000] => 1000
        OFFSET = 1000
        for num in nums:
            num_ct[num + OFFSET] += 1
        import heapq
        h = []
        for num, ct in enumerate(num_ct, start=-1000):
            heapq.heappush(h, (-ct, num))
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(h)[-1])
        return ans