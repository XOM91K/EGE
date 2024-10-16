# Constants
N = 7  
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]  
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]  
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]

class Melody:
    def __init__(self, notes=None):
        """Initialize the Melody with an optional list of Note objects."""
        if notes is None:
            self.notes = []
        else:
            self.notes = notes.copy()

    def __str__(self):
        """Return the melody as a string with notes separated by commas.
        The first note starts with a capital letter."""
        if not self.notes:
            return ''
        note_strs = [str(note) for note in self.notes]
        note_strs[0] = note_strs[0].capitalize()
        return ', '.join(note_strs)

    def append(self, note):
        """Append a Note object to the end of the melody."""
        self.notes.append(note)

    def replace_last(self, note):
        """Replace the last Note in the melody with the given Note."""
        self.notes[-1] = note

    def remove_last(self):
        """Remove the last Note from the melody."""
        self.notes.pop()

    def clear(self):
        """Clear all notes from the melody."""
        self.notes.clear()

    def __len__(self):
        """Return the number of notes in the melody."""
        return len(self.notes)

    def __rshift__(self, k):
        """Transpose the melody upwards by k semitones."""
        return self._transpose(k)

    def __lshift__(self, k):
        """Transpose the melody downwards by k semitones."""
        return self._transpose(-k)

    def _transpose(self, shift):
        """Helper method to transpose the melody by the given shift."""
        if not isinstance(shift, int):
            raise TypeError('Shift value must be an integer')

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
        """Return a copy of the current melody."""
        return Melody(self.notes.copy())

# Assuming the Note class is defined as follows:
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
melody = Melody([Note('ля'), Note('соль'), Note('ми'),  Note('до', True)])
print(melody)
print(Melody() >> 2)
melody_up = melody >> 1
melody_down = melody << 1
melody.replace_last(Note('соль'))
print('>> 1:', melody_up)
print('<< 1:', melody_down)
print(melody)