# Libraries
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter.messagebox import showinfo, showerror, askyesno
import pygame.mixer as mixer
import os

# Initializing the pyagame.mixer library
mixer.init()

# App GUI
root = Tk()
root.geometry('700x220')
root.title('Music Player App')
root.resizable(0,0)

# Setting the app icon
#inco_path = ''
#root.iconbitmap(icon_path)

# Play music function
def play_music(song_name: StringVar, song_list: Listbox, status: StringVar):
    song_name.set(song_list.get(ACTIVE))

    mixer.music.load(song_list.get(ACTIVE))
    mixer.music.play()

    status.set('Song is playing...')

# Stop music function
def stop_music(status: StringVar):
    mixer.music.stop()
    status.set('Song stopped...')

# Load music function
def load_music(listbox):
    os.chdir(filedialog.askdirectory(title="Open a song directory"))
    tracks = os.listdir()

    for track in tracks:
        listbox.insert(END, track)

def paused_music(status: StringVar):
    mixer.music.pause()
    status.set('Song is puased')

def resume_music(status: StringVar):
    mixer.music.unpause()
    status.set('Song resumed')

# LabelFrames
music_frame = LabelFrame(root, text="Current Song", bg='LightBlue', width=400, height=80)
music_frame.place(x=0, y=0)

button_frame = LabelFrame(root, text='Control Buttons', bg='Turquoise', width=400, height=120)
button_frame.place(y=80)

Listbox_frame = LabelFrame(root, text='Playlist', bg='RoyalBlue')
Listbox_frame.place(x=400, y=0, height=200, width=300)

# StringVars
current_song = StringVar(root, value='<Not Selected>')

song_status = StringVar(root, value='<Not Selected>')

# Placing all the widget in each label
# Playlist (Listbox)
playlist = Listbox(Listbox_frame, font=('Helvetica', 11), selectbackground='Gold')

scroll_bar = Scrollbar(Listbox_frame, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=BOTH)


playlist.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=playlist.yview)

playlist.pack(fill=BOTH, padx=5, pady=5)

# MusicFrames
Label(music_frame, text='Currently playing:', bg='LightBlue', font=('Times', 10, 'bold' )).place(x=5, y=20)

song_label = Label(music_frame, textvariable=current_song, bg='Goldenrod', font=('Times', 12), width=25)
song_label.place(x=150, y=20)

# Buttons showing on the control buttons label
# Pause button
pause_button = Button(button_frame, text='Pause', bg='Aqua', font=('Georgia', 13), width=7,
                    command=lambda: paused_music(song_status))

pause_button.place(x=15, y=10)

# Stop button
stop_button = Button(button_frame, text='Stop', bg='Aqua', font=('Georgia', 13), width=7,
                    command=lambda: stop_music(song_status))

stop_button.place(x=105, y=10)

# Play button
play_button = Button(button_frame, text='Play', bg='Aqua', font=('Georgia', 13), width=7,
                    command=lambda: play_music(current_song, playlist, song_status))

play_button.place(x=195, y=10)

# Resume button
resume_button = Button(button_frame, text='Resume', bg='Aqua', font=('Georgia', 13), width=7,
                    command=lambda: resume_music(song_status))

resume_button.place(x=285, y=10)

# Load button
load_button = Button(button_frame, text='Load', bg='Aqua', font=('Georgia', 13), width=7,
                    command=lambda: load_music(playlist))

load_button.place(x=15, y=55)



# Label that tells the status of the song
Label(root, textvariable=song_status, bg='SteelBlue', font=('Times', 8), justify=LEFT).pack(side=BOTTOM, fill=X)

def reset_list(playlist):
    if askyesno(title='Reset List', message='Are you sure you want to reset the playlist?'):
        playlist.delete(0, END)

# Reste button
reset_button = Button(button_frame, text='Reset', bg='Aqua', font=('Georgia, 13'), width=7,
                    command=lambda: reset_list(playlist))

reset_button.place(x=105, y=55)

root.update()
root.mainloop()