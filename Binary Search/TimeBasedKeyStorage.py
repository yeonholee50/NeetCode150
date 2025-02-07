class TimeMap:

    def __init__(self):
        self.hm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hm.keys():
            self.hm[key] = [(timestamp, value)]
        else:
            self.hm[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.hm.keys():
            return ""
        else:
            arr = self.hm[key]
            if arr[0][0] > timestamp:
                return ""
            i = 1
            while i < len(arr) and timestamp > arr[i][0]:
                i*=2
            if i >= len(arr):
                i = len(arr) - 1
            while i > 0 and timestamp < arr[i][0]:
                i-=1
            return arr[i][-1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)