class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict as d
        l, r, n, dic, ans = 0, -1, len(s), d(int), 0
        max_char = ['-', -1] # char, freq
        while r + 1 < n:
            # check if can inch one more
            r += 1; dic[s[r]] += 1
            if dic[s[r]] > max_char[1]:
                max_char = [s[r], dic[s[r]]]
            # check if we need to squeeze one back
            window_sz = sum(dic.values())
            while window_sz - max_char[1] > k:
                dic[s[l]] -= 1; l += 1; window_sz -= 1
                if max_char[0] == s[l]:
                    c = max(dic, key = lambda x: dic[x])
                    max_char = [c, dic[c]]
            ans = max(ans, window_sz)
        return ans
