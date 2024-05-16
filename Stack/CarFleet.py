class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(reverse=True)
        stack = []
        print(cars)
        for p, s in cars:
            """
            we append the time
            """
            stack.append((target-p)/s)
            """
            if the time ahead is more, then we have to merge those fleet
            had to use reverse = true because the slower speed ahead will cause congestion which si what we need
            """
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)