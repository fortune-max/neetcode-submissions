class Solution:
    def trap(self, height: List[int]) -> int:
        heights = height; height = None
        from collections import defaultdict as d
        dic = d(list)
        for idx, height in enumerate(heights):
            dic[height].append(idx)
        n = len(heights); arr = [None] * n
        leftmost, rightmost = float("inf"), -float("inf")
        for height in sorted(dic, reverse=True):
            idxes = dic[height]
            for idx in idxes:
                arr[idx] = max(height, arr[idx] or height)
                r_step, l_step = 1, 1
                while idx + r_step < rightmost and arr[idx + r_step] == None:
                    arr[idx + r_step] = max(height, arr[idx + r_step] or height)
                    r_step += 1
                while idx - l_step > leftmost and arr[idx - l_step] == None:
                    arr[idx - l_step] = max(height, arr[idx - l_step] or height)
                    l_step += 1
                leftmost, rightmost = min(leftmost, idx - l_step + 1), max(rightmost, idx + r_step - 1)
        ans = 0
        for i in range(n):
            ans += arr[i] - heights[i]
        return ans
