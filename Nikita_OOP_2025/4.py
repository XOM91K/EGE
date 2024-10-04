N = 7
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]
class Note:
    def __init__(self, note, long_pitch=False):
        self.note = note
        self.long_pitch = long_pitch
    def __str__(self):
        if self.long_pitch:
            return LONG_PITCHES[PITCHES.index(self.note)]
        else:
            return self.note
    def __repr__(self):
        if self.long_pitch:
            return LONG_PITCHES[PITCHES.index(self.note)]
        else:
            return self.note

class Melody:
    def __init__(self, notes=[]):
        self.notes = notes.copy()
    def __str__(self):
        return ', '.join([str(i) for i in self.notes]).capitalize()

    def __len__(self):
        return len(self.notes)
    def __rshift__(self, other):

    def append(self, note):
        self.notes.append(note)
    def replace_last(self, note):
        if len(self.notes) > 0:
            self.notes[-1] = note
    def remove_last(self):
        self.notes.pop()

    def clear(self):
        self.notes.clear()


melody = Melody([Note('до'), Note('ми'), Note('соль', True)])
print(melody, len(melody))
print(Melody(), len(Melody()))
melody.clear()
print(melody, len(melody))
print(melody >> 2)