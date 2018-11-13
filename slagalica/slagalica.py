from tkinter import *

prazna = 0

def akcija(event):
    global prazna
    bla = event.widget.ime
    gumbi[prazna].config(image = slike[bla])
    gumbi[bla].config(image = slike[prazna])
    slike[prazna], slike[bla] = slike[bla], slike[prazna]
    prazna = bla
    
def ispis(event):
    global prazna
    print(prazna)

window = Tk()
window.geometry("400x400")
window.resizable(False, False)
window.configure(bg="#FFB6C1")

slike = []
gumbi = []

slike.append(PhotoImage())
gumbi.append(Button(window))
for i in range(1, 9):
    slike.append(PhotoImage(file="{}.png".format(i)))
    gumbi.append(Button(window))


for i in range(9):
    gumbi[i].config(image = slike[i], borderwidth = 0, highlightthickness = 0, width = 100, height = 100, bg="#DB7093")
    gumbi[i].ime = i
    gumbi[i].bind("<Button-1>", akcija)

gumb = Button(width = 50, height = 50, image = PhotoImage(), borderwidth = 0, highlightthickness = 0, bg="red")
gumb.bind("<Button-1>", ispis)
#gumb.grid(row=0, column=0)
#gumb.grid(row=4, column=4)
cnt = 0
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(4, weight=1)
window.grid_columnconfigure(4, weight=1)

for i in range(1, 4):
    for j in range(1, 4):
        gumbi[cnt].grid(row = i, column = j, sticky=NSEW)
        cnt += 1
        
window.mainloop()
