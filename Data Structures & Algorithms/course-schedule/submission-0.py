class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        requirements = {i :[] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            requirements[course].append(prerequisite)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if requirements[course] == []:
                return True

            visited.add(course)
            for prerequisite in requirements[course]:
                if not dfs(prerequisite):
                    return False
            visited.remove(course)
            requirements[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
