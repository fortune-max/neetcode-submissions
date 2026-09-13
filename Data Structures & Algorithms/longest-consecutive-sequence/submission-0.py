from collections import OrderedDict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        while nums:
            num = nums.pop()
            count = 1
            inc = 1 # go fwd
            while num + inc in nums:
                nums.remove(num + inc)
                count += 1
                inc += 1
            dec = 1 # go bck
            while num - dec in nums:
                nums.remove(num - dec)
                count += 1
                dec += 1
            ans = max(ans, count)
        return ans

