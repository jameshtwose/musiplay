#%%
from music21 import note, corpus, converter
from itertools import product
import numpy as np

#%%
f = note.Note("f5")
bflat = note.Note("B-2")
# %%
# f.show()
# %%
verdi = corpus.parse('verdi/laDonnaEMobile')
verdi.id = 'verdi'
# verdi.measures(1, 10).show()
# %%
voice = verdi.parts[0]
_ = voice.measures(1, 10).plot()
# %%
fakePiece = converter.parse("tinyNotation: 1/4 c#4 2/4 d-4 e#4 3/4 e#2 f4 4/4 c#4 d'--2")
fakePiece.id = 'fake'
_ = fakePiece.plot()

# %%
note_letters = ["AA", "AA#", "BB", "CC", "CC#", "DD", "DD#", "EE", "FF", "FF#", "GG", "GG#",
                "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#",
                "a", "a#", "b", "c", "c#", "d", "d#", "e", "f", "f#", "g", "g#",
                "a'", "a'#", "b'", "c'", "c'#", "d'", "d'#", "e'", "f'", "f'#", "g'", "g'#"]
# note_letters_capital = [x.title() for x in note_letters]
# note_octaves = ["0", "1", "2", "3", "4", "5"]
note_lengths = ["1", "2", "4", "8", "16", "32"]
full_notes_list = ["".join(x) for x in product(note_letters, note_lengths)]

# %%
np.random.seed(42)
random_choice_list=np.random.choice(full_notes_list, size=50)
# random_choice_list

# %%
piece_string = f"4/4 {' '.join(random_choice_list)}"
piece = converter.parse(piece_string, format="tinyNotation")
piece.id = "random_generation"

#%%
# piece.show("text")
_ = piece.plot()
# %%
piece.write(fmt="midi", fp="randomly_generated_midi_2.mid")
# %%
