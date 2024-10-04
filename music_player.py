# Libraries
import pygame.mixer as mixer
import os

# Play music function
def play_music(song_name, song_list, status):
    try:
        # Get the index of the currently selected song in the Listbox
        song_index = song_list.curselection()

        # Verify if a song is selected
        if not song_index:
            status.set('No song selected')
            return

        # Get the absolute file path using the stored paths
        selected_song_path = song_list.file_paths[song_index[0]]

        # Print the selected song path for debugging
        print(f"Selected song path: {selected_song_path}")

        # Set the current song's name for the label
        song_name.set(os.path.basename(selected_song_path))

        # Load and play the selected song
        mixer.music.load(selected_song_path)
        mixer.music.play()

        # Update the status
        status.set('Song is playing...')

    except Exception as e:
        status.set(f'Error: {e}')
        print(f"Error: {e}")

# Stop music function
def stop_music(status):
    mixer.music.stop()
    status.set('Song stopped...')

# Pause music function
def paused_music(status):
    mixer.music.pause()
    status.set('Song is paused...')

# Resume music function
def resume_music(status):
    mixer.music.unpause()
    status.set('Song resumed...')