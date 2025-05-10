class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to prereq list
        pre_map = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            pre_map[course].append(prereq)

        visited = set()
        def has_cycle(course):
            if course in visited:
                return False #cycle detected            
            if not pre_map[course]:
                return True # already processed or no prereqs

            visited.add(course)
            for prereq in pre_map[course]:
                if not has_cycle(prereq): 
                    return False
            visited.remove(course)
            pre_map[course] = []  #mark as processed
            return True

        for course in range(numCourses):
            if not has_cycle(course):
                return False
        return True


# TC: O(V + E) where V = numCourses, E = len(prerequisites) | SC: O(V + E) for adjacency list + recursion stack
            



        