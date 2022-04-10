#%%
from music21 import note, corpus, converter
from itertools import product
import numpy as np
import string

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
# piece.write(fmt="midi", fp="randomly_generated_midi_2.mid")
# %%
alphabet_list = list(string.ascii_lowercase)
alphabet_notes_dict = dict(zip(alphabet_list, note_letters))

# %%
string_of_interest = """
A tension exists in neurology between those who believe that the 
most valuable lessons about the brain can be learned from statistical 
analyses involving large numbers of patients and those who believe 
that doing the right kind of experiments on the right patients—even 
a single patient—can yield much more useful information. This is 
really a silly debate since its resolution is obvious: It's a good 
idea to begin with experiments on single cases and then to confirm 
the findings through studies of additional patients. By way of 
analogy, imagine that I cart a pig into your living room and tell 
you that it can talk. You might say, "Oh, really? Show me." I 
then wave my wand and the pig starts talking. You might respond, 
"My God! That's amazing!" You are not likely to say, "Ah, but that's 
just one pig. Show me a few more and then I might believe you." 
Yet this is precisely the attitude of many people in my field.
"""

# %%
new_piece = list()
for x in string_of_interest:
    if x not in list(alphabet_notes_dict.keys()):
        new_piece.append("r")
    else:
        new_piece.append(alphabet_notes_dict[x])

new_piece = [f"{x}1" for x in new_piece]
# %%
piece_string = f"4/4 {' '.join(new_piece)}"
piece = converter.parse(piece_string, format="tinyNotation")
piece.id = "neuro_piece"

#%%
# piece.show("text")
_ = piece.plot()
# %%
# piece.write(fmt="midi", fp="neuro_midi.mid")
# %%
