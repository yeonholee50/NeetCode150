class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)

        time = 0
        q = deque()

        while max_heap or q:
            time+=1
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt < 0:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                cnt = q.popleft()[0]
                heapq.heappush(max_heap, cnt)
        return time