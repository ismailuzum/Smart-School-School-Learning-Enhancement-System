class Meeting_Schedule:
    def __init__(self, meeting_schedule_id, meeting_dates, meeting_times, meetings):
        self.meeting_schedule_id = meeting_schedule_id
        self.meeting_dates = meeting_dates
        self.meeting_times = meeting_times
        self.meetings = meetings

    def create_meeting_Schedule(self, meeting_dates, meeting_times, meetings):
        self.meeting_dates = meeting_dates
        self.meeting_times = meeting_times
        self.meetings = meetings
        print("Meeting_Schedule created")

    def update_meeting_Schedule(self, new_meeting_dates, new_meeting_times, new_meetings):
        self.new_meeting_dates = new_meeting_dates
        self.new_meeting_times = new_meeting_times
        self.new_meetings = new_meetings
        print("Meeting_Schedule updated")

    def view_Meeting_Schedule(self):
        print("Course_Schedule:", self.course_dates, self.course_times, self.courses)
        return self.course_dates, self.course_times, self.courses
