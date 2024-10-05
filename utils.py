import os
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import askyesno



# Load music function
def load_music(listbox):
    # Allow the user to select multiple MP3 files from any directory
    file_paths = filedialog.askopenfilenames(
        title="Select Music Files",
        filetypes=[("MP3 Files", "*.mp3"), ("OGG Files", "*.ogg"), ("WAV Files", "*.wav"), ("All Files", "*.*")]
    )
    
    if not file_paths:
        return  # If no files were selected, exit the function

    # Clear the existing items in the listbox
    listbox.delete(0, END)

    # Store the full file paths in a list
    listbox.file_paths = file_paths

    # Loop through the selected file paths and add each file's name to the listbox
    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        listbox.insert(END, file_name)

# Reset the playlist
def reset_list(playlist, current_song):
    if askyesno(title='Reset List', message='Are you sure you want to reset the playlist?'):
        playlist.delete(0, END)
        current_song.set('<Not Selected>')
