from sol import (
    Note, DefaultNote, LoudNote,
    LoudNote, NoteWithOctave,
    PITCHES
)
print(Note('соль'))
print(LoudNote(PITCHES[4]))
print(LoudNote("си", is_long=True))
print(DefaultNote('ми'))
print(DefaultNote())
print(DefaultNote(is_long=True))
print(NoteWithOctave('ре', 'первая октава'))