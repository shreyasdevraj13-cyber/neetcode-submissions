class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        while q and sandwiches[0] in q:
            if q[0] == sandwiches[0]:
                q.popleft()
                sandwiches.pop(0)
            else:
                q.append(q.popleft())
        return len(q)
        
                

        