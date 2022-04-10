#%%
from music21 import note, corpus, converter
from itertools import product
import numpy as np
import string
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from jmspack.utils import apply_scaling

#%%
if "jms_style_sheet" in plt.style.available:
    plt.style.use("jms_style_sheet")

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
alphabet_list = list(string.ascii_lowercase)
alphabet_notes_dict = dict(zip(alphabet_list, note_letters))

# %%
def lorenz(x, y, z, s=10, r=28, b=2.667):
    """
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the lorenz attractor's partial
           derivatives at the point x, y, z
    """
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot


dt = 0.01
num_steps = 1000

# Need one more for the initial values
xs = np.empty(num_steps + 1)
ys = np.empty(num_steps + 1)
zs = np.empty(num_steps + 1)

# Set initial values
xs[0], ys[0], zs[0] = (0., 1., 1.05)

# Step through "time", calculating the partial derivatives at the current point
# and using them to estimate the next point
for i in range(num_steps):
    x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)

#%%
df = pd.DataFrame({"x": xs, "y": ys, "z": zs})
df.head()

# %%
range_max = 200
round_df = (df
    .pipe(apply_scaling, kwargs={"feature_range":(0,range_max)})
    .round()
    .astype(int)
)

_ = sns.lineplot(data=round_df
                        .reset_index()
                        .melt(id_vars="index"),
                x="index",
                y="value",
                hue="variable"
                )
_ = sns.despine()

# %%
number_list = list(range(range_max + 1))
number_notes_dict = dict(zip(number_list, full_notes_list))

# %%
new_piece=[number_notes_dict[x] for x in round_df["z"].values]

# %%
piece_name = "lorenz_piece_z"
piece_string = f"4/4 {' '.join(new_piece)}"
piece = converter.parse(piece_string, format="tinyNotation")
piece.id = piece_name

#%%
# piece.show("text")
_ = piece.plot()
# %%
# piece.write(fmt="midi", fp=f"{piece_name}.mid")
# %%
