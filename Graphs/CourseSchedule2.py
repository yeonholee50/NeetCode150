class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hm = {}
        for i in range(numCourses):
            hm[i] = []
        for i in range(len(prerequisites)):
            prerequisite = prerequisites[i]
            for j in range(len(prerequisite)):
                hm[prerequisite[-1]].append(prerequisite[0])
        visit = set()
        cycle = set()
        output = []
        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            cycle.add(course)
            for pre in hm[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []
        output.reverse()
        return output