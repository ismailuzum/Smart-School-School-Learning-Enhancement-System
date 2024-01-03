class MessageBoard:
    def __init__(self, message_id, content, sender_id, recipient_id):
        self.message_id = message_id
        self.content = content
        self.sender_id = sender_id
        self.recipient_id = recipient_id

    def sendMessage(self, sender_id, recipient_id, content):
        self.sender_id = sender_id
        self.recipient_id = recipient_id
        self.content = content
        print("Message sent from", sender_id, "to", recipient_id)

    def viewMessages(self):
        print("Message content:", self.content)
        return self.content
