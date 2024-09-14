class Solution:
    def findOrder_initial_solution(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        time complexity = O(numCourses + len(prerequisites)) 
            (time complexity of BFS is O(V+E), v=number of vertices, E=number of edges)
        space complexity = O(numCourses + len(prerequisites))
            (time complexity of BFS is O(V+E), v=number of vertices, E=number of edges)
        """
        # create dictionary that makes a course pre-requisites
        course_prereq_dict = {} # the course and it's prerequisites
        prereq_course_dict = {} # a course when complete, and the potential courses you can take afterwards
        for course, course_pre_req in prerequisites:
            if course in course_prereq_dict:
                course_prereq_dict[course].append(course_pre_req)
            else:
                course_prereq_dict[course] = [course_pre_req]   
            if course_pre_req in prereq_course_dict:
                prereq_course_dict[course_pre_req].append(course)
            else:
                prereq_course_dict[course_pre_req] = [course]

        courses_taken = set({}) # this records all the courses that are taken
        # after this loop we would have taken courses with no pre-requisites
        for i in range(numCourses):
            if i not in course_prereq_dict:
                courses_taken.add(i)

        # use BFS to get all the courses
        courses_taken_arr = list(courses_taken)
        queue = list(courses_taken)
        while queue != []:
            course_completed = queue.pop()
            if course_completed not in courses_taken:
                courses_taken_arr.append(course_completed)
            courses_taken.add(course_completed)

            # check what courses that potentially open up
            if course_completed in prereq_course_dict:
                # get the list of the courses that have potentially opened up as a result of complete a pre-requisite
                courses_potentially_available = prereq_course_dict[course_completed]
                # for each potential course, if all it's pre-reqs are met, it can be completed and added to the queue
                for course in courses_potentially_available:
                    # check if the courses prereqs are open
                    flag_all_taken = True
                    for c in course_prereq_dict[course]:
                        if c not in courses_taken:
                            flag_all_taken = False
                    if flag_all_taken == True:
                        queue.append(course)

        if numCourses != len(courses_taken_arr):
            return []
        else:
            return courses_taken_arr

