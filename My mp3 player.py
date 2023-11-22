# installed python packages  

from tkinter import *
import tkinter as tk 
from tkinter import filedialog
import pygame.mixer as mixer



class MP:
    def __init__(self, win):
        # created Tkinter window 
        win.geometry('200x200')
        win.title('Music Player')
        win.resizable(0, 0)
        
        # StringVar to change button text later
        
        self.play_restart = tk.StringVar()
        self.pause_resume = tk.StringVar()
        self.play_restart.set('Play')
        self.pause_resume.set('Pause')
        
        # The buttons and their positions 
        
        load_button = Button(win, text='Load', width=10, font=('Arial', 12), command=self.load)
        load_button.place(x = 125, y=30, anchor='center')
        
        play_button = Button(win, textvariable=self.play_restart, width=10, font=('Arial', 12), command=self.play)
        play_button.place(x = 125, y=70, anchor='center')
        
        pause_button = Button(win, textvariable=self.pause_resume, width=10, font=('Arial', 12), command=self.pause)
        pause_button.place(x = 125, y=110, anchor='center')
        
        stop_button = Button(win, text='Stop', width=10, font=('Arial', 12), command=self.stop)
        stop_button.place(x = 125, y=150, anchor='center')
        
        # created UI for the user to adjust volume 

        self.volume_slider = Scale(win, from_=0, to=100, orient=HORIZONTAL, command=self.set_volume)
        self.volume_slider.set(50)
        self.volume_slider.place(x=50, y=190, anchor='w')
        
        
        self.music_file = False
        self.playing_state = False 
        
       # created functions for the user to play, pause , load & stop the mp3 palyer  
     
    def load(self):
        self.music_file = filedialog.askopenfilename()
        print('Loaded:', self.music_file)
        self.play_restart.set('Play')
    
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
            self.playing_state = False
            self.play_restart.set('Restart')
            self.pause_resume.set('Pause')
             
    def pause(self):
        
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True 
            self.pause_resume.set("Resume")
            
        else: 
            mixer.music.pause()
            self.playing_state = False 
            self.pause_resume.set("Pause")
                
    def stop(self):
        mixer.music.stop()
        
    def set_volume(self,val):
        volume = int(val) / 100
        mixer.music.set_volume(volume)
    
root = Tk() 
MP(root) 
root.mainloop()