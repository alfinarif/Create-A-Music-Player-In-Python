from tkinter import *
import pygame
import os

window = Tk()
window.geometry("400x150")
pygame.mixer.init()
n=0
def start_stop():
    global n
    n=n+1
    if n==1:
        song_name = songs_listbox.get()
        pygame.mixer.music.load(song_name)
        pygame.mixer.music.play(0)
    elif (n%2)==0:
        pygame.mixer.music.pause()
    elif (n%2)!=0:
        pygame.mixer.music.unpause()



l1 = Label(window,text="MUSIC PLAYER", font="times 20")
l1.grid(row=1,column=1)

b1 = Button(window,text="play", width=20,command=start_stop)
b1.grid(row=4,column=1)


songs_list = os.listdir()
songs_listbox = StringVar(window)
songs_listbox.set("select songs")
menu = OptionMenu(window,songs_listbox,*songs_list)
menu.grid(row=4,column=4)

window.mainloop()