class Solution:
    def maxArea(self, heights: List[int]) -> int:
        from collections import defaultdict as d
        n = len(heights)
        dic = d(lambda: [n-1, 0])
        for idx, height in enumerate(heights):
            dic[height] = [min(dic[height][0], idx), max(dic[height][1], idx)]
        ans, leftmost, rightmost = -float("inf"), n-1, 0
        for height in sorted(dic, reverse=True):
            leftmost, rightmost = min(leftmost, dic[height][0]), max(rightmost, dic[height][1])
            ans = max(ans, (rightmost - leftmost) * height)
        return ans
