# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent,md
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.9.1
#   kernelspec:
#     display_name: Python [conda env:midi-data515] *
#     language: python
#     name: conda-env-midi-data515-py
# ---

# %% [markdown]
# The following code is derived from the tutorial at:
#
# https://www.twilio.com/blog/working-with-midi-data-in-python-using-mido

# %%
from mido import MidiFile

mid = MidiFile('VampireKillerCV1.mid', clip=True)

# %%
type( mid )

# %%
print(mid)

# %%
for track in mid.tracks:
    print(track)

# %%
for msg in mid.tracks[0]:
    print(msg)

# %%
import os

from mido import MidiFile


cv1 = MidiFile('VampireKillerCV1.mid', clip=True)

message_numbers = []
duplicates = []

for track in cv1.tracks:
    if len(track) in message_numbers:
        duplicates.append(track)
    else:
        message_numbers.append(len(track))

for track in duplicates:
    cv1.tracks.remove(track)

cv1.save('new_song.mid')

# %%
import os

from mido import MidiFile


cv1 = MidiFile('new_song.mid', clip=True)
cv3 = MidiFile('VampireKillerCV3.mid', clip=True)

del cv1.tracks[4]
del cv1.tracks[4]

cv1.tracks.append(cv3.tracks[4])
cv1.tracks.append(cv3.tracks[5])

cv1.save('mashup.mid')

