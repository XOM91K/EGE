N = 7
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]


class Note:
    def __init__(self, note, long_pitch=False):
        self.note = note
        self.long_pitch = long_pitch

    def __str__(self):
        if self.long_pitch and self.note in PITCHES:
            return LONG_PITCHES[PITCHES.index(self.note)]
        else:
            return self.note

    def __repr__(self):
        if self.long_pitch and self.note in PITCHES:
            return LONG_PITCHES[PITCHES.index(self.note)]
        else:
            return self.note


class Melody:
    def __init__(self, notes=[]):
        self.notes = notes.copy()
        self.notes2 = notes.copy()

    def __str__(self):
        return ', '.join([str(i) for i in self.notes]).capitalize()

    def __len__(self):
        return len(self.notes)

    def __rshift__(self, other):
        mel = self.notes.copy()
        for i in range(len(mel)):
            if mel[i].long_pitch:
                if mel[-1].long_pitch:
                    if LONG_PITCHES.index(str(mel[-1])) + other >= len(LONG_PITCHES):
                        return self.copy()
                mel[i] = Note(LONG_PITCHES[LONG_PITCHES.index(str(mel[i])) + other], True)
            else:
                if not(mel[-1].long_pitch):
                    if PITCHES.index(str(mel[-1])) + other >= len(PITCHES):
                        return self.copy()
                mel[i] = Note(PITCHES[PITCHES.index(str(mel[i])) + other])
        return Melody(mel)

    def __lshift__(self, other):
        mel = self.notes.copy()
        for i in range(len(mel)):
            if mel[i].long_pitch:
                if mel[0].long_pitch:
                    if LONG_PITCHES.index(str(mel[0])) - other < 0:
                        return self.copy()
                mel[i] = Note(LONG_PITCHES[LONG_PITCHES.index(str(mel[i])) - other], True)
            else:
                if not(mel[0].long_pitch):
                    if PITCHES.index(str(mel[0])) - other < 0:
                        return self.copy()
                mel[i] = Note(PITCHES[PITCHES.index(str(mel[i])) - other])
        return Melody(mel)

    def copy(self):
        return Melody(self.notes.copy())
    def append(self, note):
        self.notes.append(note)

    def replace_last(self, note):
        if len(self.notes) > 0:
            self.notes[-1] = note

    def remove_last(self):
        self.notes.pop()

    def clear(self):
        self.notes.clear()


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
