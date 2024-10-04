import pygame.mixer as mixer
import os

# Play music feature
def play_music(song_name, song_list, status):
    try:
        song_index = song_list.curselection()

        if not song_index:
            status.set('No song selected')
            return

        # Get the selected song
        selected_song = song_list.get(song_index[0])
        song_name.set(selected_song)

        # Load and play the song
        mixer.music.load(selected_song)  # Ensure you have the correct path
        mixer.music.play()

        status.set('Song is playing...')

    except Exception as e:
        status.set(f'Error: {e}')

# Stop music
def stop_music(status):
    mixer.music.stop()
    status.set('Song stopped...')

# Pause music
def paused_music(status):
    mixer.music.pause()
    status.set('Song is paused...')

# Resume music
def resume_music(status):
    mixer.music.unpause()
    status.set('Song resumed...')