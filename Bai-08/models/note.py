import uuid

class Note: 
    def __init__(self, title, content):
        self.id = str(uuid.uuid4()) 
        self.title = title
        self.content = content