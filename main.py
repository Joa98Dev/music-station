# Libraries
from tkinter import *
import tkinter as tk
from tkinter import filedialog, ttk
import pygame.mixer as mixer
from music_player import play_music, stop_music, paused_music, resume_music
from utils import load_music, reset_list

# Initialize the mixer library
mixer.init()

# GUI
root = Tk()
root.geometry('700x220')
root.title('Music Station')
root.resizable(0,0)
root.attributes("-alpha", 0.8)

# LabelFrames
music_frame = LabelFrame(root, text="Current Song", fg='#faaab4', bg='#131313', width=400, height=80, bd=0)
music_frame.place(x=0, y=0)

button_frame = LabelFrame(root, text='Control Buttons', fg='#faaab4', bg='#131313', width=400, height=120, bd=0)
button_frame.place(y=80)

Listbox_frame = LabelFrame(root, text='Playlist', fg='#faaab4', bg='#131313', bd=0)
Listbox_frame.place(x=400, y=0, height=200, width=300)

# StringVars
current_song = StringVar(root, value='<Not Selected>')
song_status = StringVar(root, value='<Not Selected>')


# Scrollbar themed
style = ttk.Style()
style.configure("CustomScrollbar.Vertical.TScrollbar", 
                bg='#131313',
                troughcolor="#131313", 
                slidercolor="#faaab4",
                arrowcolor = "#131313")

# Add a scrollbar to the playlist section
scroll_bar = ttk.Scrollbar(Listbox_frame, orient=VERTICAL, style="CustomScrollbar.Vertical.TScrollbar")
scroll_bar.pack(side=RIGHT, fill=BOTH)

# Control buttons
# Play button
play_button = Button(button_frame, text='Play', fg='#faaab4', bg='#131313', bd=0, highlightthickness=0, font=('Antipasto Pro DemiBold', 13), width=7, command=lambda: play_music(current_song, playlist, song_status))
play_button.place(x=195, y=10)

# Pause button
pause_button = Button(button_frame, text='Pause', fg='#faaab4', bg='#131313', bd=0, highlightthickness=0, font=('Antipasto Pro DemiBold', 13), width=7, command=lambda: paused_music(song_status))
pause_button.place(x=15, y=10)

# Stop button
stop_button = Button(button_frame, text='Stop', fg='#faaab4', bg='#131313', bd=0, highlightthickness=0, font=('Antipasto Pro DemiBold', 13), width=7, command=lambda: stop_music(song_status))
stop_button.place(x=105, y=10)

# Resume button
resume_button = Button(button_frame, text='Resume', fg='#faaab4', bg='#131313', bd=0, highlightthickness=0, font=('Antipasto Pro DemiBold', 13), width=7, command=lambda: resume_music(song_status))
resume_button.place(x=285, y=10)

# Load button
load_button = Button(button_frame, text='Load', fg='#faaab4', bg='#131313', bd=0, highlightthickness=0, font=('Antipasto Pro DemiBold', 13), width=7, command=lambda: load_music(playlist))
load_button.place(x=15, y=55)

# Reset button
reset_button = Button(button_frame, text='Reset', fg='#faaab4', bg='#131313', bd=0, highlightthickness=0, font=('Antipasto Pro DemiBold', 13), width=7, command=lambda: reset_list(playlist, current_song))
reset_button.place(x=105, y=55)

# Placing all the widget in each label

# Playlist (Listbox)
playlist = Listbox(Listbox_frame, font=('Antipasto Pro DemiBold', 12), selectbackground='#faaab4', bg='#131313', highlightthickness=0, border=0, fg='#faaab4')


playlist.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=playlist.yview)

playlist.pack(fill=BOTH, padx=5, pady=5)

# MusicFrames
Label(music_frame, text='Currently playing:', fg='#faaab4', bg='#131313', font=('Antipasto Pro DemiBold', 10, 'bold' )).place(x=5, y=20)

song_label = Label(music_frame, textvariable=current_song, bg='#faaab4', font=('Antipasto Pro DemiBold', 12), width=25)
song_label.place(x=150, y=20)

# Label that tells the status of the song
Label(root, textvariable=song_status, bg='#faaab4', font=('Antipasto Pro DemiBold', 8), justify=LEFT).pack(side=BOTTOM, fill=X)


root.update() # Update the GUI
root.mainloop() # Keeps the app running