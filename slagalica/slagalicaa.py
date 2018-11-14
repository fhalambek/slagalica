from tkinter import *
from random import *
from itertools import permutations

prazna = 0

def akcija(event):
    global prazna
    global LQ
    bla = event.widget.ime
    
    redp=LQ.index(prazna)//3
    stupacp=LQ.index(prazna)%3
    redb=LQ.index(bla)//3
    stupacb=LQ.index(bla)%3

    if (redb==redp and (stupacb==stupacb-1 or stupacb==stupacb+1)) or (stupacb==stupacp and (redb==redp-1 or redb==redp+1)):

        indexbla=LQ.index(bla)
        indexprazna=LQ.index(prazna)
        LQ[indexbla]=prazna
        LQ[indexprazna]=bla
                                                                       
        cnt=0
                                                                       
        for i in range(1,4):
            for j in range (1,4):
                gumbi[LQ[cnt]].grid(row = i, column = j)
                cnt += 1
    
    

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
    gumbi[i].config(image = slike[i], borderwidth = 0, highlightthickness = 0, width = 100, height = 100, bg="#DB7093",activebackground="black")
    gumbi[i].ime = i
    gumbi[i].bind("<Button>", akcija)

gumb = Button(width = 50, height = 50, image = PhotoImage(), borderwidth = 0, highlightthickness = 0, bg="red")

window.grid_rowconfigure(0, weight=50)
window.grid_columnconfigure(0, weight=50)
window.grid_rowconfigure(4, weight=50)
window.grid_columnconfigure(4, weight=50)

cnt=0
L=list(permutations([1,2,3,4,5,6,7,8]))
LQ=list(L[randint(0,40320)])

gumbi[0].grid(row=1, column=1)
for i in range(1,4):
    for j in range (1,4):
        if(i == 1 and j == 1): continue;
        gumbi[LQ[cnt]].grid(row = i, column = j)
        cnt += 1

LQ.insert(0,0)
window.mainloop()
