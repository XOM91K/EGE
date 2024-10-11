# Constants
N = 7
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]

class Melody:
    def __init__(self, notes=None):
        if notes is None:
            self.notes = []
        else:
            self.notes = notes.copy()

    def __str__(self):
        if not self.notes:
            return ''
        note_strs = [str(note) for note in self.notes]
        note_strs[0] = note_strs[0].capitalize()
        return ', '.join(note_strs)

    def append(self, note):
        self.notes.append(note)

    def replace_last(self, note):
        self.notes[-1] = note

    def remove_last(self):
        self.notes.pop()

    def clear(self):
        self.notes.clear()

    def __len__(self):
        return len(self.notes)

    def __rshift__(self, k):
        return self._transpose(k)

    def __lshift__(self, k):
        return self._transpose(-k)

    def _transpose(self, shift):

        new_notes = []
        for note in self.notes:
            if note.name not in PITCHES:
                return self.copy()

            current_index = PITCHES.index(note.name)
            new_index = current_index + shift

            if not (0 <= new_index < N):
                return self.copy()

            new_pitch = PITCHES[new_index]
            new_note = type(note)(new_pitch, note.long_pitch)
            new_notes.append(new_note)

        return Melody(new_notes)

    def copy(self):
        return Melody(self.notes.copy())

class Note:
    def __init__(self, name, long_pitch=False):
        self.name = name
        self.long_pitch = long_pitch

    def __str__(self):
        if self.long_pitch:
            if self.name in PITCHES:
                index = PITCHES.index(self.name)
                return LONG_PITCHES[index]
            else:
                return self.name
        return self.name

    def __repr__(self):
        return f"Note('{self.name}', {self.long_pitch})"


mel1 = Melody([Note('ре', True), Note('ми'), Note('до', True), Note('фа'), Note('ля'), Note('соль', True)])
m1 = mel1 >> 1
m2 = mel1 >> 3
print(m1)
print(m2)
print()

mel2 = Melody([Note('ре', True), Note('ми'), Note('до', True), Note('фа'), Note('ля'), Note('соль', True)])
m3 = mel2 << 2
m4 = mel2 << 2
print(m3)
print(m4)
print()

n1 = Note('фа', True)
n2 = Note('соль', True)
mel3 = Melody()
mel3.append(n1)
mel3.append(n2)
m5 = mel3 >> 1 >> 1
m6 = mel3 << 1 << 1
m7 = mel3 >> 3
m8 = mel3 << 3
print(m5)
print(m6)
print(m7)
print(m8)
print()

mel4 = Melody()
m9 = mel4 >> 3
m10 = mel4 << 3
print(m9)
print(m10)
print()
n3 = Note('ми', True)
n4 = Note('ми')
n5 = Note('фа')
mel5 = Melody([n5, n4, n3])
m11 = mel5 >> 2
m12 = mel5 << 2
m13 = mel5 >> 12
m14 = mel5 << 6
print(m11)
print(m12)
print(m13)
print(m14)
