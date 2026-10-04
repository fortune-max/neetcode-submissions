class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mx_pile, total_pile = 0, 0
        for pile in piles:
            mx_pile = max(pile, mx_pile)
            total_pile += pile
        r = mx_pile # k_max (one pile per hour)
        l = total_pile // h + (bool(total_pile % h)) # k_min (no breaks in hour)
        def time_enough(k):
            ans = 0
            for pile in piles:
                ans += pile // k + (bool(pile % k))
                if ans > h:
                    return False
            return True
        while l <= r:
            mid = (l + r) // 2
            mid_ok = time_enough(mid)
            if mid_ok:
                r = mid - 1
            elif not mid_ok:
                l = mid + 1
        return l
