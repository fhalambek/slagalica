from tkinter import *
from random import *
from itertools import permutations

prazna = 0

def akcija(event):
    global prazna
    global LQ
    bla = event.widget.ime
    
    gumbi[prazna].config(image = slike[bla])
    gumbi[bla].config(image = slike[prazna])
    slike[prazna], slike[bla] = slike[bla], slike[prazna]
    #gumbi[bla].ime=prazna
    prazna = bla
    #print(gumbi[bla].ime)
    

window = Tk()
window.geometry("400x400")
window.title("Slagalica")
window.resizable(False, False)
window.configure(bg="#FFB6C1")

slike = []
gumbi = []

slike.append(PhotoImage())
gumbi.append(Button(window))
for i in range(1, 9):
    slike.append(PhotoImage(file="stepenice/{}.png".format(i)))
    gumbi.append(Button(window))


for i in range(9):
    gumbi[i].config(image = slike[i], borderwidth = 0, highlightthickness = 0, width = 100, height = 100, bg="#DB7093")
    gumbi[i].ime = i
    gumbi[i].bind("<Button-1>", akcija)

gumb = Button(width = 50, height = 50, image = PhotoImage(), borderwidth = 0, highlightthickness = 0, bg="red")

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(4, weight=1)
window.grid_columnconfigure(4, weight=1)

cnt = 0
L=list(permutations([1,2,3,4,5,6,7,8]))
LQ=L[randint(0,40320)]

gumbi[0].grid(row=1, column=1)
for i in range(1,4):
    for j in range (1,4):
        if(i == 1 and j == 1): continue;
        gumbi[LQ[cnt]].grid(row = i, column = j)
        cnt += 1
        
window.mainloop()
