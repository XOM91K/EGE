PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]

class Note:
    def __init__(self, name, is_long=False):
        self.name = name
        self.is_long = is_long

    def __str__(self):
        return self.name

class LoudNote(Note):
    def __str__(self):
        return self.name.upper()

class DefaultNote(Note):
    def __init__(self, name="до", is_long=False):
        super().__init__(name, is_long)

class NoteWithOctave(Note):
    def __init__(self, name, octave, is_long=False):
        super().__init__(name, is_long)
        self.octave = octave

    def __str__(self):
        return f"{self.name} ({self.octave})"