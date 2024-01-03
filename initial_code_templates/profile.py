class Profile:
    def __init__(self, profile_id, details):
        self.profile_id = profile_id
        self.details = details

    def createProfile(self, details):
        self.details = details
        print("Profile created with details:", details)

    def updateProfile(self, new_details):
        self.details = new_details
        print("Profile updated with new details:", new_details)

    def viewProfile(self):
        print("Profile details:", self.details)
        return self.details
