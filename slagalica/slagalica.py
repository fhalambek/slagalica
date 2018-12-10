from tkinter import *
from random import *
from itertools import permutations

prazna = 0

#POMICANJE PLOČICA

def akcija(event):
    global prazna
    global LQ
    global obv
    bla = event.widget.ime
    
    redp=LQ.index(prazna)//3
    stupacp=LQ.index(prazna)%3
    redb=LQ.index(bla)//3
    stupacb=LQ.index(bla)%3

    if (redb==redp and (stupacb==stupacp-1 or stupacb==stupacp+1)) or (stupacb==stupacp and (redb==redp-1 or redb==redp+1)):

        indexbla=LQ.index(bla)
        indexprazna=LQ.index(prazna)
        LQ[indexbla]=prazna
        LQ[indexprazna]=bla
                                                                       
        cnt=0
                                                                       
        for i in range(1,4):
            for j in range (1,4):
                gumbi[LQ[cnt]].grid(row = i, column = j)
                cnt += 1

    if LQ==[0,1,2,3,4,5,6,7,8]:
        krajigre()

        
#POSTAVLJANJE PROZORA
        
window = Tk()
window.geometry("800x400")
window.title("Slagalica")
window.resizable(False, False)
window.configure(bg="#a6f2cc")

#window.grid_rowconfigure(0, weight=50)
#window.grid_columnconfigure(0, weight=50)
#window.grid_rowconfigure(4, weight=50)
#window.grid_columnconfigure(4, weight=50)

igra = Frame(height=400, width=400, bd=1, bg="#FFB6C1", padx=50, pady=50)
igra.grid(row=0,column =0)

igra.grid_rowconfigure(0, weight=50)
igra.grid_columnconfigure(0, weight=50)
igra.grid_rowconfigure(4, weight=50)
igra.grid_columnconfigure(4, weight=50)

opcije = Frame(height=400, width=400, bd=1, bg="#a1f7cc" )
opcije.grid(row=0, column=1)

#GUMBI + SLIKE

slike = []
gumbi = []

slike.append(PhotoImage())
gumbi.append(Button(igra))
for i in range(1, 9):
    slike.append(PhotoImage(file="stepenice/{}.png".format(i)))
    gumbi.append(Button(igra))


for i in range(9):
    gumbi[i].config(image = slike[i], borderwidth = 0, highlightthickness = 0, width = 100, height = 100, bg="#DB7093",activebackground="black")
    gumbi[i].ime = i
    gumbi[i].bind("<Button>", akcija)

#gumb = Button(width = 50, height = 50, image = PhotoImage(), borderwidth = 0, highlightthickness = 0, bg="red")

#POSTAVLJANJE GUMBA ZA POČETAK
def postavljanje():
    global LQ
    L=list(permutations([1,2,3,4,5,6,7,8]))
    LQ=list(L[randint(0,40320)])
    gumbi[0].grid(row=1, column=1)

    cnt=0
    for i in range(1,4):
        for j in range (1,4):
            if(i == 1 and j == 1):
                continue
            gumbi[LQ[cnt]].grid(row = i, column = j)
            cnt += 1
    LQ.insert(0,0)
    return

postavljanje()

#LEADERBOARD
score = float(input())
def izmjenilistu():
    global score
    global ime
    ranglista = open("ranglista.txt",'r')
    retci = ranglista.readlines()
    print (retci)
    for i in range (3,len(retci)):
        retci[i].split('  ')
        #if score<=float(retci[i][2]):
            #retci.insert(i,[0,ime,score])
    print(retci)
    ranglista.close()
    ranglista = open("ranglista.txt",'w')
    for i in range (3,len(retci)):
        retci[i][0]=str(i-1)+'.'
        retci[i][2]=str(retci[i][2])
    retci=retci.join('  ')
    ranglista.writelines(retci)
    print(ranglista.read())   
    
    
#POBJEDA
def krajigre():
    obv = Toplevel()
    obv.geometry("200x200")
    obv.title("Kraj igre")
    msg = Message(obv, text = "Pobijedili ste!")
    msg.grid(row=0, column=0)
    msg2 = Message(obv, text = "Ime:")
    msg2.grid(row=1)
    imenujse = Entry(obv)
    imenujse.grid(row=1, column=1)
    klikni = Button(obv, text = "U redu", command = obv.destroy)
    klikni.grid(row=3)
    
    def igrajopet():
        obv.destroy()
        postavljanje()
        return
    def unesi():
        global ime
        ime = imenujse.get()
        izmijenilistu()
        return
        
    klikni2 = Button(obv, text = "Igraj ponovo", command = igrajopet)
    klikni2.grid(row=4)
    klikni3 = Button(obv,text = "ok", command = unesi)
    klikni3.grid(row=2)

    dat = open("ranglista.txt",'r')
    print(dat.read())
    dat.close()

    return

krajigre()
izmjenilistu()

window.mainloop()
