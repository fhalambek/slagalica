from tkinter import *

prazna = 0

def akcija(event):
    global prazna
    #print(prazna)
    bla = event.widget.ime
    #print(bla)
    gumbi[prazna].config(image = slike[bla])
    gumbi[bla].config(image = slike[prazna])
    prazna = bla
    #print(prazna)
    
def ispis(event):
    global prazna
    print(prazna)

window = Tk()
window.geometry("400x400")
window.resizable(False, False)

slike = []
gumbi = []

slike.append(PhotoImage())
gumbi.append(Button(window))
for i in range(1, 9):
    slike.append(PhotoImage(file="{}.png".format(i)))
    gumbi.append(Button(window))


for i in range(9):
    gumbi[i].config(image = slike[i], borderwidth = 0, highlightthickness = 0, width = 100, height = 100)
    gumbi[i].ime = i
    gumbi[i].bind("<Button>", akcija)

gumb = Button(width = 50, height = 50, image = slike[0], borderwidth = 0, highlightthickness = 0)
gumb.bind("<Button>", ispis)
cnt = 0
for i in range(3):
    for j in range(3):
        gumbi[cnt].grid(row = i, column = j)
        cnt += 1
gumb.grid(row=3, column=3)
window.mainloop()
