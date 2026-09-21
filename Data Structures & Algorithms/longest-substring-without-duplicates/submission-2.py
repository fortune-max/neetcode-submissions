class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = [0] * 128
        l, r, n, ans = 0, 0, len(s), 0
        while r < n:
            c = ord(s[r])
            while count[c]:
                count[ord(s[l])] -= 1
                l += 1
            count[c] += 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans
