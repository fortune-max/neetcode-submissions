class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        to_fill, n = [], len(temperatures)
        ans = [0] * n
        for idx, temp in enumerate(temperatures):
            while to_fill and to_fill[-1][0] < temp:
                old_val, old_idx = to_fill.pop()
                ans[old_idx] = idx - old_idx
            to_fill.append((temp, idx))
        return ans
