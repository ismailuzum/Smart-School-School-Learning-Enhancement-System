class Course_Schedule:
    def __init__(self, course_schedule_id, course_dates, course_times, courses):
        self.course_schedule_id = course_schedule_id
        self.course_dates = course_dates
        self.course_times = course_times
        self.courses = courses

    def create_course_Schedule(self, course_dates, course_times, courses):
        self.course_dates = course_dates
        self.course_times = course_times
        self.courses = courses
        print("Course_Schedule created")

    def update_course_Schedule(self, new_course_dates, new_course_times, new_courses):
        self.new_course_dates = new_course_dates
        self.new_course_times = new_course_times
        self.new_courses = new_courses
        print("Course_Schedule updated")

    def view_Course_Schedule(self):
        print("Course_Schedule:", self.course_dates, self.course_times, self.courses)
        return self.course_dates, self.course_times, self.courses
