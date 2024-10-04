import os
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import askyesno



def load_music(listbox):
    # Open a file dialog to select multiple mp3 files
    files = filedialog.askopenfilenames(title="Select MP3 Files", filetypes=[("MP3 Files", "*.mp3")])
    
    if not files:
        return  # If the user cancels, do nothing
    
    # Add selected files to the playlist listbox
    for file in files:
        filename = os.path.basename(file)  # Get the filename only
        listbox.insert(END, filename)

# Reset the playlist
def reset_list(playlist, current_song):
    if askyesno(title='Reset List', message='Are you sure you want to reset the playlist?'):
        playlist.delete(0, END)
        current_song.set('<Not Selected>')
