class Meeting_Attendance:
    def __init__(self, meeting_attendance_id, student_id, meeting_id, meeting_dates, meeting_status):
        self.meeting_attendance_id = meeting_attendance_id
        self.student_id = student_id
        self.meeting_id = meeting_id
        self.meeting_dates = meeting_dates
        self.meeting_status = meeting_status

    def create_meeting_Attendance(self, student_id, meeting_id, meeting_dates, meeting_status):
        self.student_id = student_id
        self.meeting_id = meeting_id
        self.meeting_dates = meeting_dates
        self.meeting_status = meeting_status
        print("Meeting_Attendance record created")

    def update_meeting_Attendance(self, new_meeting_dates, new_meeting_status):
        self.new_meeting_dates = new_meeting_dates
        self.new_meeting_status = new_meeting_status
        print("meeting_Attendance record updated")

    def view_meeting_Attendance(self):
        print("Meeting_Attendance:", self.meeting_dates, self.meeting_status)
        return self.meeting_dates, self.meeting_status