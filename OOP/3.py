PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]

class Note:
    def __init__(self, pitch, is_long=False):
        self.pitch = pitch
        self.is_long = is_long

    def __str__(self):
        return self.pitch + ("-" if self.is_long else "")

class LoudNote(Note):
    def __str__(self):
        return self.pitch.upper() + ("-" if self.is_long else "")

class DefaultNote(Note):
    def __init__(self, pitch="до", is_long=False):
        super().__init__(pitch, is_long)

class NoteWithOctave(Note):
    def __init__(self, pitch, octave, is_long=False):
        super().__init__(pitch, is_long)
        self.octave = octave

    def __str__(self):
        return f"{self.pitch}{'-' if self.is_long else ''} ({self.octave})"

# Примеры использования:
print(Note("соль"))  # соль
print(LoudNote(PITCHES[4]))  # СОЛЬ
print(LoudNote("си", is_long=True))  # СИ-И
print(DefaultNote("ми"))  # ми
print(DefaultNote())  # до
print(DefaultNote(is_long=True))  # до-о
print(NoteWithOctave("ре", "первая октава"))  # ре (первая октава)
print(NoteWithOctave("ля", "малая октава", is_long=True))  # ля-а (малая октава)