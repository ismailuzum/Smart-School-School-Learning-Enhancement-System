class Announcement:
    def __init__(self, announcement_id, message, date_posted):
        self.announcement_id = announcement_id
        self.message = message
        self.date_posted = date_posted

    def postAnnouncement(self, message):
        self.message = message
        print("Announcement posted:", message)

    def updateAnnouncement(self, new_message):
        self.message = new_message
        print("Announcement updated:", new_message)

    def viewAnnouncement(self):
        print("Announcement:", self.message, self.date_posted)
        return self.message, self.date_posted
