import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sys
from time import sleep
import pickle
import choice
# import rpg
import sounds as snd
import monster as mn
import eventFlags as ef
import choice as ch
import ability as abi
COUNTER = 0
##########################################################
#MAIN MENU
##########################################################
def mainmenu():
    root = tk.Tk()
    snd.mainTheme()
    def reload():
        snd.musicStop()
        root.destroy()
        l_check=rpg.load()
        rpg.gameStart(l_check)
    def start():
        snd.musicStop()
        root.destroy()
        rpg.gameStart()
    if rpg.is_accessible('savefile.dat')==True:
        startB = tk.Radiobutton(root,text="NEW GAME",value=False,indicatoron=0,command=start)
        startB.grid(row=1,column=1,columnspan=2,sticky="w,e")
        loadB = tk.Radiobutton(root,text="LOAD",value=False,indicatoron=0,command=reload)
        loadB.grid(row=2,column=1,columnspan=2,sticky="w,e")
        quit = tk.Radiobutton(root,text="QUIT",value=False,indicatoron=0,command=sys.exit)
        quit.grid(row=3,column=1,columnspan=2,sticky="w,e")
    else:
        startB = tk.Radiobutton(root,text="NEW GAME",value=False,indicatoron=0,command=start)
        startB.grid(row=1,column=1,columnspan=2,sticky="w,e")
        quit = tk.Radiobutton(root,text="QUIT",value=False,indicatoron=0,command=sys.exit)
        quit.grid(row=3,column=1,columnspan=2,sticky="w,e")
    image = Image.open("images/title.png")
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(image=photo,relief="sunken")
    label.grid(row=0,column=1,sticky="w,e")
    root.mainloop()

##########################################################
# DEAD ZONE--START
##########################################################
def introScene():
    root = tk.Tk()
    sleep(1)
    def intro():
        x = var.get()
        if x==OPTIONS[0]:
            root.destroy()
            print('\nWelcome! I am Meikahs, Keeper of the Lost!')
            return True
        else:
            print('\n???: Then begone from here! uwu')
            sys.exit()
    OPTIONS = ["Yes...","No","No, not really!"]
    var = tk.StringVar(root)
    # var.set(OPTIONS[2])
    dropDown = tk.OptionMenu(root,var,*OPTIONS)
    dropDown.pack()
    select = tk.Button(root, text="Enter", command=intro)
    select.pack()
    root.mainloop()
    if var.get() not in OPTIONS:
        introScene()


def nameChange(playerName):
    root = tk.Tk()
    print('\nMeikahs: So will you change your name?')
    sleep(2)
    def nameC(playerName=playerName):
        x = var.get()
        root.destroy()
        if x=="Yes":
            rpg.Player.playerList.pop()
            playerName=rpg.create_player()
        else:
            print("\nMeikahs: I guess you're sticking with "+playerName+", then?")
    OPTIONS = ["Yes","No"]
    var = tk.StringVar(root)
    dropDown = tk.OptionMenu(root,var,*OPTIONS)
    dropDown.pack()
    select = tk.Button(root, text="Enter", command=nameC)
    select.pack()
    root.mainloop()
    if var.get() not in OPTIONS:
        nameChange(playerName)
    return playerName

def understand(Meikahs):
    root=tk.Tk()
    def clarity():
        x = var.get()
        root.destroy()
        if x==0:
            rpg.Player.playerList[1].karma+=1
            print(Meikahs+": How compliant! Surely you'll survive.")
            sleep(2)
            print(Meikahs+": Well now, it's time for you to get going. Ta ta!")
        elif x==1 or x==2:
            print(Meikahs+": You could have just chosen the first option...")
            sleep(2)
            print(Meikahs+": Well now, it's time for you to get going. Ta ta!")
        else:
            rpg.Player.playerList[1].karma-=1
            print(Meikahs+": Silly child, you are guided by my hand. I cannot simply leave you to your own devices, now can I?")
            sleep(2)
            print(Meikahs+": It's time for you to LEAVE!!!")
        sleep(2)
        # ForestBisca()
    OPTIONS = ["Yes","Yes","Yes","What kind of options are these?"]
    var = tk.IntVar()
    for o in range(len(OPTIONS)):
        a = tk.Radiobutton(root,text=OPTIONS[o],variable=var,value=o,indicatoron=0).pack(fill="x")
    select = tk.Button(root, text="Enter", command=clarity)
    select.pack()
    if var.get() not in OPTIONS:
        understand(Meikahs)
    root.mainloop()

####################################################
# TOWN DE SUCRE NOIR
####################################################
def TSNMenu(player, eFlags):
    root = tk.Tk()
    def menu():
        x = var.get()
        if x==1:
            print("\nThe town looks empty...")
            b.config(state="normal")
            eFlags[0].options=True
        elif x==2:
            print("A change occurs!")
            eFlags[0].loop+=1
            rpg.save(player,rpg.Player.playerList)
            root.destroy()
        elif x==3:
            rpg.give_stats(1)
            pass
        elif x==4:
            rpg.save(player,rpg.Player.playerList)
            pass
    OPTIONS = [(1,"Look Around"),(2,"Interact with Crest"),(3,"Check Stats"),(4,"Save")]
    var = tk.IntVar()
    var.set(1)
    for num,option in OPTIONS:
        if num!=2:
            a = tk.Radiobutton(root,text=option,variable=var,value=num,indicatoron=0).pack(fill="x")
        else:
            b = tk.Radiobutton(root,text=option,variable=var,value=num,indicatoron=0,state="disabled")
            b.pack(fill="x")
    select = tk.Button(root, text="Submit", command=menu)
    select.pack()
    root.mainloop()

####################################################
# GEARDEG RATH
####################################################
def GDRMenu():
    root = tk.Tk()
    def menu():
        x=var.get()
        if x==1:
            print("You are awestruck by the mechanical marvels!")
        elif x==2:
            rpg.give_stats(1)
            pass
        elif x==3:
            rpg.save(player,rpg.Player.playerList)
            pass
    OPTIONS = [(1,"Look Around"),(2,"Check Stats"),(3,"Save")]
    var = tk.IntVar()
    var.set(1)
    for num,option in OPTIONS:
        a = tk.Radiobutton(root,text=option,variable=var,value=num,indicatoron=0).pack(fill="x")
    select = tk.Button(root, text="Enter", command=menu)
    select.pack()
    root.mainloop()

####################################################
# GENERAL USE
####################################################
def CharacterText(items,background="white",graphic="images/qmark.png"):
    global COUNTER
    COUNTER=0
    root = tk.Tk()
    def forward():
        global COUNTER
        txt.config(state="normal")
        txt.delete(0.0,"end")
        COUNTER+=1
        if COUNTER<len(items):
            txt.insert(tk.INSERT,items[COUNTER])
        if COUNTER>0:
            back.grid(row=2,column=2,sticky="w,e")
            if COUNTER==len(items)-1:
                end = tk.Button(root,text="Exit",state="normal",command=root.destroy,width=10,bg="#ee9090")
                end.grid(row=2,column=0,sticky="w")
                sel.grid_forget()
        txt.config(state="disabled")

    def backward():
        global COUNTER
        txt.config(state="normal")
        txt.delete(0.0,"end")
        COUNTER-=1
        if COUNTER>=0:
            txt.insert(tk.INSERT,items[COUNTER])
            if COUNTER<len(items)-1:
                sel.grid(row=2,column=3,sticky="w,e")
            if COUNTER==0:
                back.grid_forget()
        txt.config(state="disabled")

    root.config(bg=background)
    txt = tk.Text(root,height=7,width=60,state="disabled")
    txt.grid(row=1,column=0,columnspan=4)
    txt.config(state="normal")
    txt.insert(tk.INSERT,items[COUNTER])
    txt.config(state="disabled")
    image = Image.open(graphic)
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(image=photo,relief="groove")
    label.grid(row=0,column=3,sticky="e")
    back = tk.Button(root,text="Back",command=backward,width=10,bg="#9090ee")
    back.grid(row=2,column=2,sticky="w,e")
    back.grid_forget()
    sel = tk.Button(root,text="Next",state="normal",command=forward,bg="#90ee90",width=10)
    sel.grid(row=2,column=3,sticky="w,e")
    root.mainloop()
    COUNTER=0

def FourChoice(choices):
    #Set up varibales, will take dictionary
    root = tk.Tk()
    if len(choices)!=4:
        return
    keys=[k for k in choices.keys()]
    vals=[v for v in choices.values()]
    def dis():
        v = var.get()
        txt.config(state="normal")
        txt.delete(0.0,"end")
        if v==0:
            txt.insert(tk.INSERT,vals[0])
        elif v==1:
            txt.insert(tk.INSERT,vals[1])
        elif v==2:
            txt.insert(tk.INSERT,vals[2])
        elif v==3:
            txt.insert(tk.INSERT,vals[3])
        txt.config(state="disabled")
        sel.config(state="normal")
    Direct = []
    var = tk.IntVar()
    var.set(0)
    a = tk.Radiobutton(root,text=keys[0],variable=var,value=0,indicatoron=0,command=dis).grid(row=0,column=0,sticky="w,e")
    b = tk.Radiobutton(root,text=keys[1],variable=var,value=1,indicatoron=0,command=dis).grid(row=0,column=1,sticky="w,e")
    c = tk.Radiobutton(root,text=keys[2],variable=var,value=2,indicatoron=0,command=dis).grid(row=0,column=2,sticky="w,e")
    d = tk.Radiobutton(root,text=keys[3],variable=var,value=3,indicatoron=0,command=dis).grid(row=0,column=3,sticky="w,e")
    txt = tk.Text(root,height=10,width=50,state="disabled")
    txt.grid(row=2,column=0,columnspan=4)
    sel = tk.Button(root,text="Select",state="disabled",command=root.destroy)
    sel.grid(columnspan=4,sticky="w,e")
    root.mainloop()
    return var.get()

def combat(p1,p2):
    global COUNTER
    COUNTER=0
    def battl(Admg,Bdmg):
        if enemyH['value']>=0 and playerH['value']>=0:
            if p1.spd>p2.spd:
                if p1.hp>0:
                    p2.hp-=Admg
                    enemyH['value']=p2.hp
                if p2.hp>0:
                    p1.hp-=Bdmg
                    playerH['value']=p1.hp
            elif p2.spd>p1.spd:
                if p2.hp>0:
                    p1.hp-=Bdmg
                    playerH['value']=p1.hp
                if p1.hp>0:
                    p2.hp-=Admg
                    enemyH['value']=p2.hp
            txt.insert(tk.INSERT,p2.m_type+" took "+str(Admg)+" damage!\n")
            if enemyH['value']<=0:
                txt.delete(0.0,"end")
                txt.insert(tk.INSERT,"You defeated "+p2.m_type+"!")
                txt.insert(tk.INSERT,"\nYou gained "+str(p2.mxp)+" exp. points.")
                p1.levelUp(p2.mxp)
            if playerH['value']<=0:
                txt.delete(0.0,"end")
                txt.insert(tk.INSERT,"You lost to "+p2.m_type+".")
                txt.insert(tk.INSERT,"\nYou gained "+str(0.25*p2.mxp)+" exp. points.")
                p1.levelUp(0.25*p2.mxp)
            txt.config(state="disabled")
            if enemyH['value']<=0 or playerH['value']<=0:
                tk.messagebox.showinfo("Status","Battle End")
                root.destroy()
    
    def phys():
        global COUNTER
        COUNTER+=1
        txt.config(state='normal')
        txt.delete(0.0,"end")
        txt.insert(tk.INSERT,"Turn "+str(COUNTER)+"\n")
        abi.passiveAbi(p2,COUNTER,txt)
        mn.in_sphere_mode(COUNTER,p2)
        Admg,Bdmg=rpg.tc_combat(p1,p2,root,txt,1)
        if Bdmg<0:
            return
        battl(Admg,Bdmg)

    def magi():
        global COUNTER
        COUNTER+=1
        txt.config(state='normal')
        txt.delete(0.0,"end")
        txt.insert(tk.INSERT,"Turn "+str(COUNTER)+"\n")
        abi.passiveAbi(p2,COUNTER,txt)
        mn.in_sphere_mode(COUNTER,p2)
        Admg,Bdmg=rpg.tc_combat(p1,p2,root,txt,2)
        if Bdmg<0:
            return
        battl(Admg,Bdmg)

    def inspect():
        stats = tk.Tk()
        stats.resizable(False,False)
        i=tk.INSERT
        sd = tk.Text(stats,width=20,height=10,font=20)
        sd.grid()
        sd.insert(i,"Name: "+p2.m_type)
        sd.insert(i,"\nRank: "+str(p2.rank))
        sd.insert(i,"\nHP: "+str(p2.hp)+"/"+str(p2.baseHP))
        sd.insert(i,"\nAttack: "+str(round(p2.atk)))
        sd.insert(i,"\nDefense: "+str(round(p2.dfn)))
        sd.insert(i,"\nMagic Attack: "+str(round(p2.matk)))
        sd.insert(i,"\nMagic Defense: "+str(round(p2.mdef)))
        sd.insert(i,"\nSpeed: "+str(round(p2.spd)))
        sd.config(state="disabled")
        stats.mainloop()
    root = tk.Tk()
    root.resizable(False,False)
    image1 = Image.open(p1.image)
    photo1 = ImageTk.PhotoImage(image1)
    playerImage = tk.Label(image=photo1,relief="groove")
    playerImage.grid(row=0,column=1,sticky="s,e")
    image2 = Image.open(p2.image)
    photo2 = ImageTk.PhotoImage(image2)
    enemyImage = tk.Label(image=photo2,relief="groove")
    enemyImage.grid(row=0,column=0,sticky="w")
    playerH = ttk.Progressbar(root,orient="horizontal",value=p1.hp,maximum=p1.baseHP,length=200,mode='determinate')
    playerH.grid(row=1,column=1,sticky="n,s,e")
    enemyH = ttk.Progressbar(root,orient="horizontal",value=p2.hp,maximum=p2.baseHP,length=200,mode='determinate')
    enemyH.grid(row=1,column=0,sticky="n,w")

    attack = tk.Button(root,text="Attack",command=phys)
    attack.grid(row=2,column=0,sticky="w,e")
    mgcAttack = tk.Button(root,text="Magic Attack",command=magi)
    mgcAttack.grid(row=2,column=1,sticky="w,e")
    defend = tk.Button(root,text="Inspect",command=inspect)
    defend.grid(row=3,column=0,sticky="w,e")
    flee = tk.Button(root,text="Flee",command=root.destroy)
    flee.grid(row=3,column=1,sticky="w,e")
    txt = tk.Text(root,height=7,width=60,state="normal")
    txt.grid(row=4,column=0,columnspan=2)
    txt.insert(tk.INSERT,"A "+p2.m_type+" attacked!")
    txt.config(state="disabled")
    root.mainloop()
    p1.hp=p1.baseHP
    p2.hp=p2.baseHP

def walking2():
    global x,y,a,b
    root = tk.Tk()
    mt = tk.Tk()
    x = 150
    y = 150
    a = 150
    b = 150
    db = [(x,y,a,b)]
    def draw():
        global x,y,a,b
        f = var.get()
        if f=="U":
            b-=25
        elif f=="D":
            b+=25
        elif f=="R":
            a+=25
        else:
            a-=25
        map.create_line(x,y,a,b)
        if a==300:
            right.config(state="disabled")
        else:
            right.config(state="normal")
        if a==25:
            left.config(state="disabled")
        else:
            left.config(state="normal")
        if b==300:
            down.config(state="disabled")
        else:
            down.config(state="normal")
        if b==25:
            up.config(state="disabled")
        else:
            up.config(state="normal")
        x,y=a,b
        if (x,y,a,b) not in db:
            db.append((x,y,a,b))
        else:
            pass
        print(db)
    map = tk.Canvas(mt,width=325,height=325)
    map.grid()
    var = tk.StringVar()
    up = tk.Radiobutton(root,text="UP",variable=var,value="U",indicatoron=0,command=draw)
    up.grid(row=0,column=1,ipadx=50)
    down = tk.Radiobutton(root,text="DOWN",variable=var,value="D",indicatoron=0,command=draw)
    down.grid(row=2,column=1,ipadx=40)
    right = tk.Radiobutton(root,text="RIGHT",variable=var,value="R",indicatoron=0,command=draw)
    right.grid(row=1,column=2,ipadx=30)
    left = tk.Radiobutton(root,text="LEFT",variable=var,value="L",indicatoron=0,command=draw)
    left.grid(row=1,column=0,ipadx=30)
    root.mainloop()
    mt.mainloop()

# combat(Player1,Player2)
# walking()
