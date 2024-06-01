class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hm = {}
        for i in range(numCourses):
            hm[i] = []
        for i in range(len(prerequisites)):
            prerequisite = prerequisites[i]
            for j in range(len(prerequisite)):
                hm[prerequisite[-1]].append(prerequisite[0])
        visited = set()
        
        def dfs(course):
            if course in visited:
                return False
            if hm[course] == []:
                """
                if course is empty, then we know all pre reqs have been taken
                """
                return True
            visited.add(course)
            for prereq in hm[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True