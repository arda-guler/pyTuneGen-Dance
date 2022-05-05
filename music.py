from pytunegen.tunegen import TuneGen

def generate_song(seed = None):
    if not seed:
        tunegen = TuneGen()
    else:
        tunegen = TuneGen(seed)

    music = tunegen.generate()
    song = []
    for bar in music:
        for note in bar.notes:
            song.append([note.pitch, note.duration])

    return song
