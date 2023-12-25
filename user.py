from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, user_id, email, password, role):
        self.user_id = user_id
        self.email = email
        self.password = password
        self.role = role

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass
