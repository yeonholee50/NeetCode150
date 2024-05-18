class TimeMap:

    def __init__(self):
        self.hm = {}
        """
        format of hashmap should be
        hm[string] = [(timestamp, value)...]
        """

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hm.keys():
            self.hm[key].append((timestamp, value))
        else:
            self.hm[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hm.keys():
            return ""
        arr = self.hm[key]
        if arr[0][0] >= timestamp:
            return arr[0][-1] if arr[0][0] == timestamp else ""
        i = 1
        while i < len(arr) and arr[i][0] < timestamp:
            i*=2
        if i >= len(arr):
            i = len(arr) - 1
        while i > 0 and arr[i][0] > timestamp:
            i-=1
        return arr[i][-1]