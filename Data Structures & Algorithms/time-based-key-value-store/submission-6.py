class TimeMap:

    def __init__(self):
        from collections import defaultdict as d
        self.dict = d(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.dict[key]
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            picked = arr[mid][0]
            if picked > timestamp:
                r = mid - 1
            elif picked < timestamp:
                l = mid + 1
            else:
                return arr[mid][1]
        if len(arr) and arr[r][0] <= timestamp:
            return arr[r][1]
        return ""
