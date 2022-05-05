import pygame
import pygame.camera
import sys
from synthesizer import Player, Synthesizer, Waveform

from music import *

def init():
    ## INIT DISPLAY
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("pyTuneGen Dance!")

    ## INIT CAMERA
    pygame.camera.init()
    webcams = pygame.camera.list_cameras()
    webcam = pygame.camera.Camera(webcams[0])
    webcam.start()

    ## INIT SYNTHESIZER
    player = Player()
    player.open_stream()
    synth = Synthesizer(osc1_waveform=Waveform.triangle, osc1_volume=1.0, use_osc2=False)

    return screen, webcam, player, synth

def take_photo(webcam):
    img = webcam.get_image()
    return img

def stop(webcam):
    webcam.stop()

def play_note(player, synth, note):
    if not type(note[0]) == list:
        player.play_wave(synth.generate_constant_wave(note[0], note[1]))
    else:
        player.play_wave(synth.generate_chord(note[0], note[1]))

def main(mseed=None):
    screen, webcam, player, synth = init()
    if mseed:
        song = generate_song(mseed)
    else:
        song = generate_song()

    while True:
        for e in pygame.event.get() :
            if e.type == pygame.QUIT :
                stop(webcam)
                pygame.display.quit()
                sys.exit()

        i = 0
        while i < len(song):
            
            img1 = take_photo(webcam)
            screen.blit(img1, (0,0))
            pygame.display.flip()

            play_note(player, synth, song[i])
            
            i += 1

            if i == len(song):
                i = 0
    
main(input("Enter seed or leave blank for random: "))

