from models.note import Note

class Database: 
    def __init__(self):
        self.notes = []

        note1 = Note("Title1", "Content1")
        note2 = Note("Title2", "Content2")
        note3 = Note("Title3", "Content3")
        note4 = Note("Title4", "Content4")

        self.notes.append(note1)
        self.notes.append(note2)
        self.notes.append(note3)
        self.notes.append(note4)

    def add_note(self, note):
        self.notes.append(note)

    def get_notes(self):
        return self.notes
    
    def update_note(self, note):
        for item in self.notes:
            if item.id == note.id : 
                item.title = note.title
                item.content = note.content

    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note.id == note_id : 
                return note
        return None