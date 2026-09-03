class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for preq in prerequisites:
            graph[preq[0]].extend(preq[1:])
        
        state = [0] * numCourses
        
        def has_cycle(course):
            if state[course] == 2:
                return False
            if state[course] == 1:
                return True
            
            state[course] = 1
            
            for preq in graph[course]:
                if has_cycle(preq):
                    return True
            
            state[course] = 2
            # print(f"visited: {visited}")

            return False
        
        for course in range(numCourses):
            # print("checking course ", course)
            if state[course] == 0 and has_cycle(course):
                return False

        return True