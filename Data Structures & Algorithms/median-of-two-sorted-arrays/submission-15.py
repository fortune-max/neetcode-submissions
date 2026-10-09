class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ct1, ct2 = len(nums1), len(nums2); nums_ct = ct1 + ct2
        if ct2 > ct1:
            nums1, nums2, ct1, ct2 = nums2, nums1, ct2, ct1
        nums2 = [-float("inf"), *nums2, float("inf")]; ct2 += 2; nums_ct += 2

        exp_hs_sz = nums_ct // 2 - (not (nums_ct % 2))
        l, r = max(exp_hs_sz - ct2, 0), min(exp_hs_sz, ct1 - 1)
        while True:
            i = (l + r) // 2; j = exp_hs_sz - i
            a2, b2 = nums1[i], nums2[j]
            a1 = nums1[i-1] if 0 <= i-1 < ct1 else None
            b1 = nums2[j-1] if 0 <= j-1 < ct2 else None
            if a1 is not None and b2 < a1:
                r = i - 1
            elif b1 is not None and a2 < b1:
                l = i + 1
            else:
                if nums_ct % 2:
                    return min([nums1[i], *nums2[j:j+1]])
                else:
                    arr = sorted([*nums1[i:i+2], *nums2[j:j+2]])[:2]
                    return sum(arr) / 2
            
        