from tkinter import * 
import tkinter as tk
import time;
from tkinter import Tk, PhotoImage, messagebox, ttk
medium_font= ('Verdana',20); small_font= ('Verdana',10)
LG = tk.Tk();LG.configure(background="white");LG.title("Schoolsysteem")
localtime=time.asctime(time.localtime(time.time()))
width = LG.winfo_screenwidth()
height = LG.winfo_screenheight()

if height >= 721:
    LG.geometry("1280x720")
if width >= 1281:
    LG.geometry("1280x720")
else: LG.attributes('-fullscreen',True)
value1 = StringVar(); value2 = StringVar(); value3 = StringVar(); var3=StringVar()
kleur1string = StringVar()
wachtwoord1=StringVar()
wachtwoord2=StringVar();gebruiker10=StringVar();wachtwoordherstel=StringVar();data=StringVar()
loginofniet10=StringVar()
boolean=StringVar()

img1 = PhotoImage(file="close.png")
img2 = PhotoImage(file="vergroot.png")
img3 = PhotoImage(file="menu.png")
img4 = PhotoImage(file="bergen.png")
img5 = PhotoImage(file="siri.png")
img6 = PhotoImage(file="addvak.png")
img7 = PhotoImage(file="weekvooruit.png")
img8 = PhotoImage(file="start.png")
img9 = PhotoImage(file="stop.png")
img10 = PhotoImage(file="delvak.png")
img11 = PhotoImage(file="deletedelvak.png")
img12 = PhotoImage(file="deleteaddvak.png")
#LG.iconbitmap(r'C:\Users\bramt\Desktop\Schoolsysteem\icon.ico')

with open('safecolor.txt', 'r') as f: safecolor = f.read()
with open('loginofniet.txt', 'r') as f: loginofniet11 = f.read()
with open('height1.txt', 'r') as f: height1 = f.read()
with open('height2.txt', 'r') as f: height2 = f.read()
with open('height3.txt', 'r') as f: height3 = f.read()
with open('height4.txt', 'r') as f: height4 = f.read()
with open('height5.txt', 'r') as f: height5 = f.read()
with open('gebruiker1.txt', 'r') as file: data = file.readlines()
counter1 = open("counter1.txt", "r").readlines()[0]
changey1 = open("changey1.txt", "r").readlines()
changey2 = open("changey2.txt", "r").readlines()
if counter1 == '1': gebruikersnaamup = '2'
if counter1 == '2': gebruikersnaamup = '3'
if counter1 == '3': gebruikersnaamup = '4'
if counter1 == '4': gebruikersnaamup = '5'
if counter1 == '5': pass
def Gebruikersnaam1():
    if value3.get() == gebruiker1 and value1.get() == wachtwoord1 : homepage()
def Gebruikersnaam2():
    if value3.get() == gebruiker2 and value1.get() == wachtwoord2 : homepage()
def Gebruikersnaam3():
    if value3.get() == gebruiker3 and value1.get() == wachtwoord3 : homepage()
def Gebruikersnaam4():
    if value3.get() == gebruiker4 and value1.get() == wachtwoord4 : homepage()
def Gebruikersnaam5():
    if value3.get() == gebruiker5 and value1.get() == wachtwoord5 : homepage()
def Gebruikers2(): Gebruikersnaam1(); Gebruikersnaam2();
def Gebruikers3(): Gebruikersnaam1(); Gebruikersnaam2(); Gebruikersnaam3()
def Gebruikers4(): Gebruikersnaam1(); Gebruikersnaam2(); Gebruikersnaam3(); Gebruikersnaam4()
def Gebruikers5(): Gebruikersnaam1(); Gebruikersnaam2(); Gebruikersnaam3(); Gebruikersnaam4(); Gebruikersnaam5()

    
def sluiten(): HoverButton(LG, image=img1,bg="white",bd=0,command=LG.destroy).place(x=1240,y=5); HoverButton(LG, image=img2,bg="white",bd=0,command=homepage).place(x=1210,y=5)
class HoverButton(tk.Button):
        def __init__(self, master, **kw):
            tk.Button.__init__(self,master=master,**kw)
            self.defaultBackground = self["background"]
            self.bind("<Enter>", self.on_enter)
            self.bind("<Leave>", self.on_leave)
        def on_enter(self, e):
            self['background'] = self['activebackground']
        def on_leave(self, e):
            self['background'] = self.defaultBackground
def changebackground():
    self.defaultBackground = self["background"]
    self['background'] = "yellow"
class DropButton(tk.Button):
        def __init__(self, master, **kw):
            tk.Button.__init__(self,master=master,**kw)
            self.defaultBackground = self["background"]
            self.bind("<Enter>", self.on_enter)
            self.bind("<Leave>", self.on_leave)
        def on_enter(self, e):
            Frame(LG,width=500,height=600,bg=safecolor).place(x=0,y=37)
            lb = Listbox(f1, height=3)
            lb.place(x=0,y=40)
            lb.insert(END, "first entry")
            sb = Scrollbar(f1, orient=VERTICAL)
            sb.place(x=50,y=40)
            sb.configure(command=lb.yview)
            lb.configure(yscrollcommand=sb.set)
            lb.curselection()
        def on_leave(self, e):
            time.sleep(3)
            homepage()
#def addvak1():
#    GU="486";oTF=open('changey1.txt', 'w');oTF.write(GU);oTF.close()
#    GU="490";oTF=open('changey2.txt', 'w');oTF.write(GU);oTF.close()
#    lijnen()
#    return

def homepage():
    with open('safecolor.txt', 'r') as f: safecolor = f.read()
    frame4 = Canvas( LG, bg ="white", height=750, width=1300,bd=0); image = frame4.create_image(1300,-100,anchor=NE,image=img4); frame4.place(x=-5,y=0)
    starframe=Frame(LG,width=1500,height=20,bg='white',bd=0).place(x=0,y=0)
    DropButton(LG, text='Start',        padx=2, pady=0, bd=0, fg="black",font=('arial', 10), width= 12, height=2,bg=safecolor).grid(row=0,column=1)
    Button(LG, text='Gebruikers',   padx=2, pady=0, bd=0, fg="black",font=('arial', 10), width= 12, height=2,bg=safecolor).grid(row=0,column=2)
    Button(LG,                      padx=2, pady=0, bd=0, fg="black",font=('arial', 10), width= 50, height=2,bg=safecolor).grid(row=0,column=3)
    Button(LG, text='Knorth',       padx=2, pady=0, bd=0, fg="black",font=('arial', 10), width= 12, height=2,command=knorth,bg=safecolor).grid(row=0,column=4)
    Button(LG, text='meldingen',    padx=2, pady=0, bd=0, fg="black",font=('arial', 10), width= 12, height=2,bg=safecolor).grid(row=0,column=5)
    Button(LG, text='Kalender',     padx=2, pady=0, bd=0, fg="black",font=('arial', 10), width= 12, height=2,bg=safecolor).grid(row=0,column=6)
    Button(LG, text='instellingen', padx=2, pady=0, bd=0, fg="black",font=('arial', 10), width= 12, height=2,command=instellingen,bg=safecolor).grid(row=0,column=7) 
    Button(LG, text='Exit',         padx=2, pady=0, bd=0, fg="black",font=('arial', 10), width= 12, height=2,command=LG.destroy,bg=safecolor).grid(row=0,column=8)
    Button(LG,                      padx=2, pady=0, bd=0, fg="black",font=('arial', 10), width= 19, height=2,bg=safecolor).grid(row=0,column=9)
    Label (LG, text=localtime,      padx=0, pady=0, bd=0, fg="black",font=('arial', 10), width= 20, height=2,bg=safecolor).grid(row=0,column=9)
def instellingen():
    def thema():
        with open('safecolor.txt', 'r') as f: safecolor = f.read()
        with open('safecolor2.txt', 'r') as f: safecolor = f.read()
        def safecolor1(): gradeUpdate = "grey99"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor2(): gradeUpdate = "grey75"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor3(): gradeUpdate = "grey60"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor4(): gradeUpdate = "grey40"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor5(): gradeUpdate = "grey30"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor6(): gradeUpdate = "grey20"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor7(): gradeUpdate = "grey10"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor8(): gradeUpdate = "grey1"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor9(): gradeUpdate = "Bisque"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor10(): gradeUpdate = "Bisque2"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor11(): gradeUpdate = "Bisque3"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor12(): gradeUpdate = "Bisque4"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor13(): gradeUpdate = "RoyalBlue1"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor14(): gradeUpdate = "RoyalBlue2"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor15(): gradeUpdate = "RoyalBlue3"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor16(): gradeUpdate = "RoyalBlue4"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor17(): gradeUpdate = "LightSteelBlue1"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor18(): gradeUpdate = "LightSteelBlue2"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor19(): gradeUpdate = "LightSteelBlue3"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor20(): gradeUpdate = "LightSteelBlue4"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor21(): gradeUpdate = "cyan1"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor22(): gradeUpdate = "cyan2"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor23(): gradeUpdate = "cyan3"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor24(): gradeUpdate = "cyan4"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor25(): gradeUpdate = "lawn Green"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor26(): gradeUpdate = "green2"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor27(): gradeUpdate = "green3"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor28(): gradeUpdate = "green4"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor29(): gradeUpdate = "khaki1"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor30(): gradeUpdate = "khaki2"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor31(): gradeUpdate = "khaki3"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor32(): gradeUpdate = "khaki4"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor33(): gradeUpdate = "yellow"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor34(): gradeUpdate = "yellow2"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor35(): gradeUpdate = "yellow3"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor36(): gradeUpdate = "yellow4"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor37(): gradeUpdate = "red"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor38(): gradeUpdate = "red2"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor39(): gradeUpdate = "red3"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor40(): gradeUpdate = "red4"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor41(): gradeUpdate = "coral1"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor42(): gradeUpdate = "coral2"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor43(): gradeUpdate = "coral3"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor44(): gradeUpdate = "coral4"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor45(): gradeUpdate = "Orange Red"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor46(): gradeUpdate = "Orangered2"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor47(): gradeUpdate = "Orangered3"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor48(): gradeUpdate = "Orangered4"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor49(): gradeUpdate = "Maroon1"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor50(): gradeUpdate = "Maroon2"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor51(): gradeUpdate = "Maroon3"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor52(): gradeUpdate = "Maroon4"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor53(): gradeUpdate = "plum1"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor54(): gradeUpdate = "plum2"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor55(): gradeUpdate = "plum3"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor56(): gradeUpdate = "plum4"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor57(): gradeUpdate = "purple1"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor58(): gradeUpdate = "purple2"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor59(): gradeUpdate = "purple3"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor60(): gradeUpdate = "purple4"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor61(): gradeUpdate = "thistle1"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor62(): gradeUpdate = "thistle1"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor63(): gradeUpdate = "thistle1"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor64(): gradeUpdate = "thistle1"; oTF = open('safecolor.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor101(): gradeUpdate = "grey99"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor102(): gradeUpdate = "grey75"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor103(): gradeUpdate = "grey60"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor104(): gradeUpdate = "grey40"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor105(): gradeUpdate = "grey30"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor106(): gradeUpdate = "grey20"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor107(): gradeUpdate = "grey10"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor108(): gradeUpdate = "grey1"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor109(): gradeUpdate = "Bisque"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor110(): gradeUpdate = "Bisque2"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor111(): gradeUpdate = "Bisque3"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor112(): gradeUpdate = "Bisque4"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor113(): gradeUpdate = "RoyalBlue1"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor114(): gradeUpdate = "RoyalBlue2"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor115(): gradeUpdate = "RoyalBlue3"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor116(): gradeUpdate = "RoyalBlue4"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor117(): gradeUpdate = "LightSteelBlue1"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor118(): gradeUpdate = "LightSteelBlue2"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor119(): gradeUpdate = "LightSteelBlue3"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor120(): gradeUpdate = "LightSteelBlue4"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor121(): gradeUpdate = "cyan1"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor122(): gradeUpdate = "cyan2"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor123(): gradeUpdate = "cyan3"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor124(): gradeUpdate = "cyan4"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor125(): gradeUpdate = "lawn Green"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor126(): gradeUpdate = "green2"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor127(): gradeUpdate = "green3"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor128(): gradeUpdate = "green4"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor129(): gradeUpdate = "khaki1"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor130(): gradeUpdate = "khaki2"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor131(): gradeUpdate = "khaki3"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor132(): gradeUpdate = "khaki4"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor133(): gradeUpdate = "yellow"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor134(): gradeUpdate = "yellow2"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor135(): gradeUpdate = "yellow3"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor136(): gradeUpdate = "yellow4"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor137(): gradeUpdate = "red"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor138(): gradeUpdate = "red2"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor139(): gradeUpdate = "red3"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor140(): gradeUpdate = "red4"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor141(): gradeUpdate = "coral1"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor142(): gradeUpdate = "coral2"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor143(): gradeUpdate = "coral3"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor144(): gradeUpdate = "coral4"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor145(): gradeUpdate = "Orange Red"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor146(): gradeUpdate = "Orangered2"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor147(): gradeUpdate = "Orangered3"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor148(): gradeUpdate = "Orangered4"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor149(): gradeUpdate = "Maroon1"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor150(): gradeUpdate = "Maroon2"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor151(): gradeUpdate = "Maroon3"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor152(): gradeUpdate = "Maroon4"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor153(): gradeUpdate = "plum1"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor154(): gradeUpdate = "plum2"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor155(): gradeUpdate = "plum3"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor156(): gradeUpdate = "plum4"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor157(): gradeUpdate = "purple1"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor158(): gradeUpdate = "purple2"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor159(): gradeUpdate = "purple3"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor160(): gradeUpdate = "purple4"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor161(): gradeUpdate = "thistle1"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor162(): gradeUpdate = "thistle1"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor163(): gradeUpdate = "thistle1"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def safecolor164(): gradeUpdate = "thistle1"; oTF = open('safecolor2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        Canvas(LG,width=1000,height=750,bg="white",bd=0).place(x=300,y=0);sluiten(); Label(LG,font=('arial', 25),bg='white',fg="black",text="Thema's").place(x=350,y=30); Label(LG,text="Hoofd kleur",font=('arial', 18, 'bold'),bg="white").place(x=690,y=150); f1 = Frame(LG,width=870,bg="grey85",bd=0,height=200).place(x=335,y=185); HoverButton(LG,bg="grey99",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor1).place(x=350,y=200); HoverButton(LG,bg="grey75",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor2).place(x=400,y=200); HoverButton(LG,bg="grey60",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor3).place(x=450,y=200); HoverButton(LG,bg="grey40",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor4).place(x=500,y=200); HoverButton(LG,bg="grey30",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor5).place(x=550,y=200); HoverButton(LG,bg="grey20",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor6).place(x=600,y=200); HoverButton(LG,bg="grey10",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor7).place(x=650,y=200); HoverButton(LG,bg="grey1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor8).place(x=700,y=200); HoverButton(LG,bg="Bisque",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor9).place(x=350,y=245); HoverButton(LG,bg="Bisque2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor10).place(x=400,y=245); HoverButton(LG,bg="Bisque3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor11).place(x=450,y=245); HoverButton(LG,bg="Bisque4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor12).place(x=500,y=245); HoverButton(LG,bg="RoyalBlue1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor13).place(x=550,y=245); HoverButton(LG,bg="RoyalBlue2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor14).place(x=600,y=245); HoverButton(LG,bg="RoyalBlue3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor15).place(x=650,y=245); HoverButton(LG,bg="RoyalBlue4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor16).place(x=700,y=245); HoverButton(LG,bg="LightSteelBlue1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor17).place(x=350,y=290); HoverButton(LG,bg="LightSteelBlue2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor18).place(x=400,y=290); HoverButton(LG,bg="LightSteelBlue3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor19).place(x=450,y=290); HoverButton(LG,bg="LightSteelBlue4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor20).place(x=500,y=290); HoverButton(LG,bg="cyan1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor21).place(x=550,y=290); HoverButton(LG,bg="cyan2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor22).place(x=600,y=290); HoverButton(LG,bg="cyan3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor23).place(x=650,y=290); HoverButton(LG,bg="cyan4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor24).place(x=700,y=290); HoverButton(LG,bg="lawn Green",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor25).place(x=350,y=335); HoverButton(LG,bg="green2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor26).place(x=400,y=335); HoverButton(LG,bg="green3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor27).place(x=450,y=335); HoverButton(LG,bg="green4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor28).place(x=500,y=335); HoverButton(LG,bg="khaki1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor29).place(x=550,y=335); HoverButton(LG,bg="khaki2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor30).place(x=600,y=335); HoverButton(LG,bg="khaki3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor31).place(x=650,y=335); HoverButton(LG,bg="khaki4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor32).place(x=700,y=335); HoverButton(LG,bg="yellow",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor33).place(x=800,y=200); HoverButton(LG,bg="yellow2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor34).place(x=850,y=200); HoverButton(LG,bg="yellow3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor35).place(x=900,y=200); HoverButton(LG,bg="yellow4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor36).place(x=950,y=200); HoverButton(LG,bg="red",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor37).place(x=1000,y=200); HoverButton(LG,bg="red2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor38).place(x=1050,y=200); HoverButton(LG,bg="red3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor39).place(x=1100,y=200); HoverButton(LG,bg="red4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor40).place(x=1150,y=200); HoverButton(LG,bg="coral1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor41).place(x=800,y=245); HoverButton(LG,bg="coral2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor42).place(x=850,y=245); HoverButton(LG,bg="coral3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor43).place(x=900,y=245); HoverButton(LG,bg="coral4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor44).place(x=950,y=245); HoverButton(LG,bg="orange red",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor45).place(x=1000,y=245); HoverButton(LG,bg="Orangered2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor46).place(x=1050,y=245); HoverButton(LG,bg="Orangered3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor47).place(x=1100,y=245); HoverButton(LG,bg="Orangered4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor48).place(x=1150,y=245); HoverButton(LG,bg="Maroon1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor49).place(x=800,y=290); HoverButton(LG,bg="Maroon2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor50).place(x=850,y=290); HoverButton(LG,bg="Maroon3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor51).place(x=900,y=290); HoverButton(LG,bg="Maroon4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor52).place(x=950,y=290); HoverButton(LG,bg="plum1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor53).place(x=1000,y=290); HoverButton(LG,bg="plum2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor54).place(x=1050,y=290); HoverButton(LG,bg="plum3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor55).place(x=1100,y=290); HoverButton(LG,bg="plum4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor56).place(x=1150,y=290); HoverButton(LG,bg="purple1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor57).place(x=800,y=335); HoverButton(LG,bg="purple2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor58).place(x=850,y=335); HoverButton(LG,bg="purple3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor59).place(x=900,y=335); HoverButton(LG,bg="purple4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor60).place(x=950,y=335); HoverButton(LG,bg="thistle1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor61).place(x=1000,y=335); HoverButton(LG,bg="thistle2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor62).place(x=1050,y=335); HoverButton(LG,bg="thistle3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor63).place(x=1100,y=335); HoverButton(LG,bg="thistle4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor64).place(x=1150,y=335); Label(LG,text="Tweede kleur",font=('arial', 18, 'bold'),bg="white").place(x=690,y=450); f1 = Frame(LG,width=870,bg="grey85",bd=0,height=200).place(x=335,y=485); HoverButton(LG,bg="grey99",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor101).place(x=350,y=500); HoverButton(LG,bg="grey75",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor102).place(x=400,y=500); HoverButton(LG,bg="grey60",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor103).place(x=450,y=500); HoverButton(LG,bg="grey40",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor104).place(x=500,y=500); HoverButton(LG,bg="grey30",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor105).place(x=550,y=500); HoverButton(LG,bg="grey20",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor106).place(x=600,y=500); HoverButton(LG,bg="grey10",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor107).place(x=650,y=500); HoverButton(LG,bg="grey1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor108).place(x=700,y=500); HoverButton(LG,bg="Bisque",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor109).place(x=350,y=545); HoverButton(LG,bg="Bisque2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor110).place(x=400,y=545); HoverButton(LG,bg="Bisque3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor111).place(x=450,y=545); HoverButton(LG,bg="Bisque4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor112).place(x=500,y=545); HoverButton(LG,bg="RoyalBlue1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor113).place(x=550,y=545); HoverButton(LG,bg="RoyalBlue2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor114).place(x=600,y=545); HoverButton(LG,bg="RoyalBlue3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor115).place(x=650,y=545); HoverButton(LG,bg="RoyalBlue4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor116).place(x=700,y=545); HoverButton(LG,bg="LightSteelBlue1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor117).place(x=350,y=590); HoverButton(LG,bg="LightSteelBlue2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor118).place(x=400,y=590); HoverButton(LG,bg="LightSteelBlue3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor119).place(x=450,y=590); HoverButton(LG,bg="LightSteelBlue4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor120).place(x=500,y=590); HoverButton(LG,bg="cyan1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor121).place(x=550,y=590); HoverButton(LG,bg="cyan2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor122).place(x=600,y=590); HoverButton(LG,bg="cyan3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor123).place(x=650,y=590); HoverButton(LG,bg="cyan4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor124).place(x=700,y=590); HoverButton(LG,bg="lawn Green",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor125).place(x=350,y=635); HoverButton(LG,bg="green2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor126).place(x=400,y=635); HoverButton(LG,bg="green3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor127).place(x=450,y=635); HoverButton(LG,bg="green4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor128).place(x=500,y=635); HoverButton(LG,bg="khaki1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor129).place(x=550,y=635); HoverButton(LG,bg="khaki2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor130).place(x=600,y=635); HoverButton(LG,bg="khaki3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor131).place(x=650,y=635); HoverButton(LG,bg="khaki4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor132).place(x=700,y=635); HoverButton(LG,bg="yellow",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor133).place(x=800,y=500); HoverButton(LG,bg="yellow2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor134).place(x=850,y=500); HoverButton(LG,bg="yellow3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor135).place(x=900,y=500); HoverButton(LG,bg="yellow4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor136).place(x=950,y=500); HoverButton(LG,bg="red",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor137).place(x=1000,y=500); HoverButton(LG,bg="red2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor138).place(x=1050,y=500); HoverButton(LG,bg="red3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor139).place(x=1100,y=500); HoverButton(LG,bg="red4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor140).place(x=1150,y=500); HoverButton(LG,bg="coral1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor141).place(x=800,y=545); HoverButton(LG,bg="coral2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor142).place(x=850,y=545); HoverButton(LG,bg="coral3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor143).place(x=900,y=545); HoverButton(LG,bg="coral4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor144).place(x=950,y=545); HoverButton(LG,bg="orange red",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor145).place(x=1000,y=545); HoverButton(LG,bg="Orangered2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor146).place(x=1050,y=545); HoverButton(LG,bg="Orangered3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor147).place(x=1100,y=545); HoverButton(LG,bg="Orangered4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor148).place(x=1150,y=545); HoverButton(LG,bg="Maroon1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor149).place(x=800,y=590); HoverButton(LG,bg="Maroon2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor150).place(x=850,y=590); HoverButton(LG,bg="Maroon3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor151).place(x=900,y=590); HoverButton(LG,bg="Maroon4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor152).place(x=950,y=590); HoverButton(LG,bg="plum1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor153).place(x=1000,y=590); HoverButton(LG,bg="plum2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor154).place(x=1050,y=590); HoverButton(LG,bg="plum3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor155).place(x=1100,y=590); HoverButton(LG,bg="plum4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor156).place(x=1150,y=590); HoverButton(LG,bg="purple1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor157).place(x=800,y=635); HoverButton(LG,bg="purple2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor158).place(x=850,y=635); HoverButton(LG,bg="purple3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor159).place(x=900,y=635); HoverButton(LG,bg="purple4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor160).place(x=950,y=635); HoverButton(LG,bg="thistle1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor161).place(x=1000,y=635); HoverButton(LG,bg="thistle2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor162).place(x=1050,y=635); HoverButton(LG,bg="thistle3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor163).place(x=1100,y=635); HoverButton(LG,bg="thistle4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=safecolor164).place(x=1150,y=635)
    def wachtwoord():
        Canvas(LG,width=1000,height=750,bg="white",bd=0).place(x=300,y=0)
        e2=Entry(LG,textvariable=wachtwoord2).place(x=400,y=300)
        e3=Entry(LG,textvariable=gebruiker10).place(x=400,y=200)
        box=ttk.Combobox(LG,textvariable=loginofniet10,font=small_font,state='readonly'); box['values']=('Als ik het programma opstart','Nooit'); remembertest=box.current(0); box.place(x=400,y=140)
        Label(LG,text="Aanmeldingsopties",font=('arial', 20),bg="white").place(x=400,y=30)
        Label(LG,text="Aanmelding vereisen",font=('arial', 16),bg="white").place(x=400,y=80)
        Label(LG,text="Wanneer moet er een log in scherm getoont worden?",font=('arial', 12),bg="white").place(x=400,y=110)
        def nieuwwachtwoord(): fline=wachtwoord2.get();src=open("wachtwoord1.txt","w"); src.writelines(fline); src.close(); return
        def nieuwegebruiker(): gradeUpdate = gebruiker10.get(); oTF = open('gebruiker1.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def loginofnietsafe(): gradeUpdate = loginofniet10.get(); oTF = open('loginofniet.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def loginofniet(): loginofnietsafe(); homepage()
        def loginofniet2(): loginofnietsafe(); LG.destroy()
        HoverButton(LG, image=img1,bg="white",bd=0,command=loginofniet2).place(x=1240,y=5); HoverButton(LG, image=img2,bg="white",bd=0,command=loginofniet).place(x=1210,y=5)
        Button(LG,text="update",font=('arial', 20),bg="red",command=nieuwegebruiker).place(x=500,y=200)
        Button(LG,text="update",font=('arial', 20),bg="red",command=nieuwwachtwoord).place(x=500,y=300)
    def gebruikersnaam():
        def a1(): HoverButton(LG,text=gebruiker1,bd=0,bg='gray20',font=('arial', 15),fg="white",width=20).place(x=900,y=150);HoverButton(LG,bg='red',bd=0,font=('arial', 25),text='x',width=2).place(x=1120,y=150)
        def a2(): HoverButton(LG,text=gebruiker2,bd=0,bg='gray20',font=('arial', 15),fg="white",width=20).place(x=900,y=200);HoverButton(LG,bg='red',bd=0,font=('arial', 25),text='x',width=2).place(x=1120,y=200)
        def a3(): HoverButton(LG,text=gebruiker3,bd=0,bg='gray20',font=('arial', 15),fg="white",width=20).place(x=900,y=250);HoverButton(LG,bg='red',bd=0,font=('arial', 25),text='x',width=2).place(x=1120,y=250)
        def a4(): HoverButton(LG,text=gebruiker4,bd=0,bg='gray20',font=('arial', 15),fg="white",width=20).place(x=900,y=300);HoverButton(LG,bg='red',bd=0,font=('arial', 25),text='x',width=2).place(x=1120,y=300)            
        def a5(): HoverButton(LG,text=gebruiker5,bd=0,bg='gray20',font=('arial', 15),fg="white",width=20).place(x=900,y=350);HoverButton(LG,bg='red',bd=0,font=('arial', 25),text='x',width=2).place(x=1120,y=350)
        Canvas(LG,width=1000,height=750,bg="white",bd=0).place(x=300,y=0)
        Entry(LG,textvariable=gebruiker10).place(x=400,y=200)
        wachtwoord2 = StringVar()
        Entry(LG,textvariable=wachtwoord2).place(x=400,y=300)
        Label(LG,text="Nieuwe gebruiker toevoegen",font=('arial', 20),bg="white").place(x=400,y=30)
        Frame(LG,bg="dodgerblue",width=300,height=450,bd=0).place(x=900,y=150)
        counter1 = open("counter1.txt", "r").readlines()[0]
        if counter1 == '1':
            a1()
        if counter1 == '2':
            a1();a2()
        if counter1 == '3':
            a1();a2();a3()
        if counter1 == '4':
            a1();a2();a3();a4()
        if counter1 == '5':
            a1();a2();a3();a4();a5()
        def nieuwegebruiker1():
            counter1 = open("counter1.txt", "r").readlines()[0]
            if counter1 == '1':
                gebruikersnaamup = '2'; oTF = open('counter1.txt', 'w'); oTF.write(gebruikersnaamup); oTF.close()
            if counter1 == '2':
                gebruikersnaamup = '3'; oTF = open('counter1.txt', 'w'); oTF.write(gebruikersnaamup); oTF.close()
            if counter1 == '3':
                gebruikersnaamup = '4'; oTF = open('counter1.txt', 'w'); oTF.write(gebruikersnaamup); oTF.close()
            if counter1 == '4':
                gebruikersnaamup = '5'; oTF = open('counter1.txt', 'w'); oTF.write(gebruikersnaamup); oTF.close()
            if counter1 == '5':
                messagebox.showinfo("Systeem", "Je hebt al het maximaal aantal gebruikers")
            def writeit1():
                if counter1 == '1':
                    data[1] = gebruiker10.get()
                    with open('gebruiker1.txt', 'w') as file: file.writelines( data )
                if counter1 == '2':
                    data[2] = gebruiker10.get()
                    with open('gebruiker1.txt', 'w') as file: file.writelines( data )
                if counter1 == '3':
                    data[3] = gebruiker10.get()
                    with open('gebruiker1.txt', 'w') as file: file.writelines( data )
                if counter1 == '4':
                    data[4] = gebruiker10.get()
                    with open('gebruiker1.txt', 'w') as file: file.writelines( data )
                if counter1 == '5':
                    pass
            def writeit2():
                if counter1 == '1':
                    gt = wachtwoord2.get()
                    with open('wachtwoord2.txt', 'w') as file: file.writelines( gt )
                if counter1 == '2':
                    gt = wachtwoord2.get()
                    with open('wachtwoord3.txt', 'w') as file: file.writelines( gt )
                if counter1 == '3':
                    gt = wachtwoord2.get()
                    with open('wachtwoord4.txt', 'w') as file: file.writelines( gt )
                if counter1 == '4':
                    gt = wachtwoord2.get()
                    with open('wachtwoord5.txt', 'w') as file: file.writelines( gt )
                if counter1 == '5':
                    pass
            writeit1()
            writeit2()
        def loginofniet(): homepage()
        def loginofniet2(): LG.destroy()
        HoverButton(LG, image=img1,bg="white",bd=0,command=loginofniet2).place(x=1240,y=5); HoverButton(LG, image=img2,bg="white",bd=0,command=loginofniet).place(x=1210,y=5)
        Button(LG,text="update",font=('arial', 20),bg="red",command=nieuwegebruiker1).place(x=500,y=200)
        
    Canvas(LG,width=1280,height=750,bd=0,bg="white").place(x=0,y=0);sluiten()
    Frame(LG,width=300,height=1000,bg='gray20',bd=0).place(x=0,y=0)
    Label(LG,font=('arial', 15, 'bold'),bg='gray20',fg="white",text="Systeem").place(x=20,y=30)
    Button(LG,font=('arial', 15),bg='gray20',fg="white",text="Thema's",bd=0,command=thema).place(x=40,y=65)
    Button(LG,font=('arial', 15),bg='gray20',fg="white",text="Wachtwoord",bd=0,command=wachtwoord).place(x=40,y=100)
    Button(LG,font=('arial', 15),bg='gray20',fg="white",text="gebruikersnaam",bd=0,command=gebruikersnaam).place(x=40,y=145)
def forgotLG():
    def close():
        Label(LG,width=60,height=200,bd=0,bg="white").place(x=0,y=0)
        frame2 = Canvas( LG, bg ="white", height=130, width=284,bd=0);         image = frame2.create_image(284,0,anchor=NE,image=image2); frame2.place(x=20,y=30)
        frame3 = Canvas( LG, bg ="white", height=30, width=30,bd=0);           image = frame3.create_image(40,0,anchor=NE,image=image3); frame3.place(x=50,y=680)
        Button(LG,text='LG',bd=0,fg="white",font=('arial', 20), width= 20, height=1, command= Gebruikersnaam,bg=safecolor,relief="ridge").place(x=70,y=540)
        Button(LG,text='Forgot your LG?',width=20,bd=0,height=1,font=('arial', 13),bg="white",fg="blue",command=forgotLG).place(x=140,y=600)
        Button(LG,text='Exit the LG panel',width=17,bd=0,height=1,font=('arial', 8),bg="white",command=LG.destroy).place(x=85,y=683)

        Label(LG,text='Username:',bd=0,font=('arial', 10),bg="white").place(x=70,y=270)
        Label(LG,text='Password:',bd=0,font=('arial', 10),bg="white").place(x=70,y=370)
        L3=Label(LG,bd=0,bg="white",height=12,width=3).place(x=19,y=30)
        L4=Label(LG,bd=0,bg="white",height=12,width=3).place(x=303,y=30)
        L5=Label(LG,bd=0,bg="white",height=3,width=41).place(x=19,y=30)
        L6=Label(LG,bd=0,bg="white",height=3,width=41).place(x=19,y=160)
        L7=Label(LG,text='Good afternoon,',bd=0,font=('arial', 15, 'bold'),bg="white").place(x=70,y=180)
        L8=Label(LG,text='welcome back!',bd=0,font=('arial', 14),bg="white").place(x=230,y=181)
        L9=Label(LG,text='Feel free to LG anytime.',bd=0,font=('arial', 11),bg="white").place(x=70,y=210)
        L10=Label(LG,bg="white",height=20,width=1).place(x=41,y=680)
        L11=Label(LG,bg="white",height=20,width=1).place(x=78,y=680)
        L12=Label(LG,bg="white",height=1,width=10).place(x=41,y=665)
        Checkbutton(LG,text="remember me",bg="white",variable=var3,onvalue=1,offvalue=0).place(x=70,y=470)
        t1=Entry(LG,show='*',textvariable=value1,bd=2,font=medium_font,relief="groove").place(x=70,y=400)
        box=ttk.Combobox(LG,textvariable=value3,font=medium_font,state='readonly'); box['values']=(' ','Bram','Nathan'); remembertest=box.current(1); box.place(x=70,y=300)

    Canvas(LG,width=500,height=750,bd=0,bg="white").place(x=0,y=0)
    Label(LG,font=('arial',15, 'bold'),text="Op welk huis nummer woon ik").place(x=50,y=50)
    Button(LG,text="<--",command=close).place(x=0,y=0)
    def wachtwoordverkrijgen():
        if wachtwoordherstel.get() == "68":
            Label(LG,text=wachtwoord1,font=('arial',15,'bold'),width=10).place(x=50,y=200)
        else:
            Label(LG,text="Antwoord is fout",fg="red",font=('arial',15,'bold')).place(x=50,y=200)
    e1=Entry(LG,textvariable=wachtwoordherstel).place(x=50,y=100)
    Button(LG,text="Herstel",command=wachtwoordverkrijgen).place(x=50,y=150)
def knorth():
    Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0)
    with open('maandagvak1.txt', 'r') as f: f_contents1 = f.read()
    with open('maandagvak2.txt', 'r') as f: f_contents2 = f.read()
    with open('maandagvak3.txt', 'r') as f: f_contents3 = f.read()
    with open('maandagvak4.txt', 'r') as f: f_contents4 = f.read()
    with open('dinsdagvak1.txt', 'r') as f: f_contents5 = f.read()
    with open('dinsdagvak2.txt', 'r') as f: f_contents6 = f.read()
    with open('dinsdagvak3.txt', 'r') as f: f_contents7 = f.read()
    with open('dinsdagvak4.txt', 'r') as f: f_contents8 = f.read()
    with open('woensdagvak1.txt', 'r') as f: f_contents9 = f.read()
    with open('woensdagvak2.txt', 'r') as f: f_contents10 = f.read()
    with open('woensdagvak3.txt', 'r') as f: f_contents11 = f.read()
    with open('woensdagvak4.txt', 'r') as f: f_contents12 = f.read()
    with open('donderdagvak1.txt', 'r') as f: f_contents13 = f.read()
    with open('donderdagvak2.txt', 'r') as f: f_contents14 = f.read()
    with open('donderdagvak3.txt', 'r') as f: f_contents15 = f.read()
    with open('donderdagvak4.txt', 'r') as f: f_contents16 = f.read()
    with open('vrijdagvak1.txt', 'r') as f: f_contents17 = f.read()
    with open('vrijdagvak2.txt', 'r') as f: f_contents18 = f.read()
    with open('vrijdagvak3.txt', 'r') as f: f_contents19 = f.read()
    with open('vrijdagvak4.txt', 'r') as f: f_contents20 = f.read()
    #============================================================
    with open('maandaghuiswerk1.txt', 'r') as f: f_contents21 = f.read()
    with open('maandaghuiswerk2.txt', 'r') as f: f_contents22 = f.read()
    with open('maandaghuiswerk3.txt', 'r') as f: f_contents23 = f.read()
    with open('maandaghuiswerk4.txt', 'r') as f: f_contents24 = f.read()
    with open('dinsdaghuiswerk1.txt', 'r') as f: f_contents25 = f.read()
    with open('dinsdaghuiswerk2.txt', 'r') as f: f_contents26 = f.read()
    with open('dinsdaghuiswerk3.txt', 'r') as f: f_contents27 = f.read()
    with open('dinsdaghuiswerk4.txt', 'r') as f: f_contents28 = f.read()
    with open('woensdaghuiswerk1.txt', 'r') as f: f_contents29 = f.read()
    with open('woensdaghuiswerk2.txt', 'r') as f: f_contents30 = f.read()
    with open('woensdaghuiswerk3.txt', 'r') as f: f_contents31 = f.read()
    with open('woensdaghuiswerk4.txt', 'r') as f: f_contents32 = f.read()
    with open('donderdaghuiswerk1.txt', 'r') as f: f_contents33 = f.read()
    with open('donderdaghuiswerk2.txt', 'r') as f: f_contents34 = f.read()
    with open('donderdaghuiswerk3.txt', 'r') as f: f_contents35 = f.read()
    with open('donderdaghuiswerk4.txt', 'r') as f: f_contents36 = f.read()
    with open('vrijdaghuiswerk1.txt', 'r') as f: f_contents37 = f.read()
    with open('vrijdaghuiswerk2.txt', 'r') as f: f_contents38 = f.read()
    with open('vrijdaghuiswerk3.txt', 'r') as f: f_contents39 = f.read()
    with open('vrijdaghuiswerk4.txt', 'r') as f: f_contents40 = f.read()
    with open('maandagtoetsen.txt', 'r') as f: f_contents41 = f.read()
    with open('dinsdagtoetsen.txt', 'r') as f: f_contents42 = f.read()
    with open('woensdagtoetsen.txt', 'r') as f: f_contents43 = f.read()
    with open('donderdagtoetsen.txt', 'r') as f: f_contents44 = f.read()
    with open('vrijdagtoetsen.txt', 'r') as f: f_contents45 = f.read()
    with open('dezemaand1.txt', 'r') as f: f_contents46 = f.read()
    with open('week2maandagtoetsen.txt', 'r') as f: f_contents47 = f.read()
    with open('week2dinsdagtoetsen.txt', 'r') as f: f_contents48 = f.read()
    with open('week2woensdagtoetsen.txt', 'r') as f: f_contents49 = f.read()
    with open('week2donderdagtoetsen.txt', 'r') as f: f_contents50 = f.read()
    with open('week2vrijdagtoetsen.txt', 'r') as f: f_contents51 = f.read()
    with open('week2maandaghuiswerk1.txt', 'r') as f: f_contents52 = f.read()
    with open('week2maandaghuiswerk2.txt', 'r') as f: f_contents53 = f.read()
    with open('week2maandaghuiswerk3.txt', 'r') as f: f_contents54 = f.read()
    with open('week2maandaghuiswerk4.txt', 'r') as f: f_contents55 = f.read()
    with open('week2dinsdaghuiswerk1.txt', 'r') as f: f_contents56 = f.read()
    with open('week2dinsdaghuiswerk2.txt', 'r') as f: f_contents57 = f.read()
    with open('week2dinsdaghuiswerk3.txt', 'r') as f: f_contents58 = f.read()
    with open('week2dinsdaghuiswerk4.txt', 'r') as f: f_contents59 = f.read()
    with open('week2woensdaghuiswerk1.txt', 'r') as f: f_contents60 = f.read()
    with open('week2woensdaghuiswerk2.txt', 'r') as f: f_contents61 = f.read()
    with open('week2woensdaghuiswerk3.txt', 'r') as f: f_contents62 = f.read()
    with open('week2woensdaghuiswerk4.txt', 'r') as f: f_contents63 = f.read()
    with open('week2donderdaghuiswerk1.txt', 'r') as f: f_contents64 = f.read()
    with open('week2donderdaghuiswerk2.txt', 'r') as f: f_contents65 = f.read()
    with open('week2donderdaghuiswerk3.txt', 'r') as f: f_contents66 = f.read()
    with open('week2donderdaghuiswerk4.txt', 'r') as f: f_contents67 = f.read()
    with open('week2vrijdaghuiswerk1.txt', 'r') as f: f_contents68 = f.read()
    with open('week2vrijdaghuiswerk2.txt', 'r') as f: f_contents69 = f.read()
    with open('week2vrijdaghuiswerk3.txt', 'r') as f: f_contents70 = f.read()
    with open('week2vrijdaghuiswerk4.txt', 'r') as f: f_contents71 = f.read()
    with open('extravak1.txt', 'r') as f: f_contents72 = f.read()
    with open('safecolor.txt', 'r') as f: safecolor = f.read()
    with open('safecolor2.txt', 'r') as f: safecolor2 = f.read()
    changey1 = open("changey1.txt", "r").readlines()
    changey2 = open("changey2.txt", "r").readlines()
    def weekvooruitspoelen():
        GT = ""
        oTF = open('maandagtoetsen.txt', 'w'); oTF.write(f_contents47); oTF.close()
        oTF = open('week2maandagtoetsen.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('dinsdagtoetsen.txt', 'w'); oTF.write(f_contents48); oTF.close()
        oTF = open('week2dinsdagtoetsen.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('woensdagtoetsen.txt', 'w'); oTF.write(f_contents49); oTF.close()
        oTF = open('week2woensdagtoetsen.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('donderdagtoetsen.txt', 'w'); oTF.write(f_contents50); oTF.close()
        oTF = open('week2donderdagtoetsen.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('vrijdagtoetsen.txt', 'w'); oTF.write(f_contents51); oTF.close()
        oTF = open('week2vrijdagtoetsen.txt', 'w'); oTF.write(GT); oTF.close()
        if f_contents47 == "": oTF = open('maandagtoetsen.txt', 'w'); oTF.write(""); oTF.close()
        if f_contents48 == "": oTF = open('dinsdagtoetsen.txt', 'w'); oTF.write(""); oTF.close()
        if f_contents49 == "": oTF = open('woensdagtoetsen.txt', 'w'); oTF.write(""); oTF.close()
        if f_contents50 == "": oTF = open('donderdagtoetsen.txt', 'w'); oTF.write(""); oTF.close()
        if f_contents51 == "": oTF = open('vrijdagtoetsen.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('maandaghuiswerk1.txt', 'w'); oTF.write(f_contents52); oTF.close()
        if f_contents52 == "": oTF = open('maandaghuiswerk1.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2maandaghuiswerk1.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('maandaghuiswerk1.txt', 'w'); oTF.write(f_contents53); oTF.close()
        if f_contents53 == "": oTF = open('maandaghuiswerk2.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2maandaghuiswerk2.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('maandaghuiswerk1.txt', 'w'); oTF.write(f_contents54); oTF.close()
        if f_contents54 == "": oTF = open('maandaghuiswerk3.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2maandaghuiswerk3.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('maandaghuiswerk1.txt', 'w'); oTF.write(f_contents55); oTF.close()
        if f_contents55 == "": oTF = open('maandaghuiswerk4.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2maandaghuiswerk4.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('dinsdaghuiswerk1.txt', 'w'); oTF.write(f_contents56); oTF.close()
        if f_contents56 == "": oTF = open('dinsdaghuiswerk1.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2dinsdaghuiswerk1.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('dinsdaghuiswerk1.txt', 'w'); oTF.write(f_contents57); oTF.close()
        if f_contents57 == "": oTF = open('dinsdaghuiswerk2.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2dinsdaghuiswerk2.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('dinsdaghuiswerk1.txt', 'w'); oTF.write(f_contents58); oTF.close()
        if f_contents58 == "": oTF = open('dinsdaghuiswerk3.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2dinsdaghuiswerk3.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('dinsdaghuiswerk1.txt', 'w'); oTF.write(f_contents59); oTF.close()
        if f_contents59 == "": oTF = open('dinsdaghuiswerk4.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2dinsdaghuiswerk4.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('woensdaghuiswerk1.txt', 'w'); oTF.write(f_contents60); oTF.close()
        if f_contents60 == "": oTF = open('woensdaghuiswerk1.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2woensdaghuiswerk1.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('woensdaghuiswerk1.txt', 'w'); oTF.write(f_contents61); oTF.close()
        if f_contents61 == "": oTF = open('woensdaghuiswerk2.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2woensdaghuiswerk2.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('woensdaghuiswerk1.txt', 'w'); oTF.write(f_contents62); oTF.close()
        if f_contents62 == "": oTF = open('woensdaghuiswerk3.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2woensdaghuiswerk3.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('woensdaghuiswerk1.txt', 'w'); oTF.write(f_contents63); oTF.close()
        if f_contents63 == "": oTF = open('woensdaghuiswerk4.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2woensdaghuiswerk4.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('donderdaghuiswerk1.txt', 'w'); oTF.write(f_contents64); oTF.close()
        if f_contents64 == "": oTF = open('donderdaghuiswerk1.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2donderdaghuiswerk1.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('donderdaghuiswerk1.txt', 'w'); oTF.write(f_contents65); oTF.close()
        if f_contents65 == "": oTF = open('donderdaghuiswerk2.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2donderdaghuiswerk2.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('donderdaghuiswerk1.txt', 'w'); oTF.write(f_contents66); oTF.close()
        if f_contents66 == "": oTF = open('donderdaghuiswerk3.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2donderdaghuiswerk3.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('donderdaghuiswerk1.txt', 'w'); oTF.write(f_contents67); oTF.close()
        if f_contents67 == "": oTF = open('donderdaghuiswerk4.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2donderdaghuiswerk4.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('vrijdaghuiswerk1.txt', 'w'); oTF.write(f_contents68); oTF.close()
        if f_contents68 == "": oTF = open('vrijdaghuiswerk1.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2vrijdaghuiswerk1.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('vrijdaghuiswerk1.txt', 'w'); oTF.write(f_contents69); oTF.close()
        if f_contents69 == "": oTF = open('vrijdaghuiswerk2.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2vrijdaghuiswerk2.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('vrijdaghuiswerk1.txt', 'w'); oTF.write(f_contents70); oTF.close()
        if f_contents70 == "": oTF = open('vrijdaghuiswerk3.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2vrijdaghuiswerk3.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('vrijdaghuiswerk1.txt', 'w'); oTF.write(f_contents71); oTF.close()
        if f_contents71 == "": oTF = open('vrijdaghuiswerk4.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2vrijdaghuiswerk4.txt', 'w'); oTF.write(GT); oTF.close()
        homepage()
    def waarschuwing():
        window = Tk()
        window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
        window.withdraw()
        if messagebox.askyesno("Systeem", "Alles word een week voor je doorgeschoven") == True: weekvooruitspoelen()
        else: pass
        window.deiconify()
        window.destroy()
        window.quit()
    def week2():
        def witscherm(): Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0)
        def week2mavak1(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents52,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2mavak2(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents53,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2mavak3(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents54,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2mavak4(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents55,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2divak1(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents56,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2divak2(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents57,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2divak3(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents58,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2divak4(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents59,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2wovak1(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents60,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2wovak2(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents61,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2wovak3(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents62,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2wovak4(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents63,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2dovak1(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents64,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2dovak2(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents65,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2dovak3(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents66,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2dovak4(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents67,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2vrvak1(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents68,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2vrvak2(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents69,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2vrvak3(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents70,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2vrvak4(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents71,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        #----------dagen die lijden naar huiswerk---------#
        HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents1,font=('arial', 15),command=week2mavak1).place(x=100,y=140); HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents2,font=('arial', 15),command=week2mavak2).place(x=100,y=200); HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents3,font=('arial', 15),command=week2mavak3).place(x=100,y=260);b4=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents4,font=('arial', 15),command=week2mavak4).place(x=100,y=320); b5=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents5,font=('arial', 15),command=week2divak1).place(x=310,y=140); b6=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents6,font=('arial', 15),command=week2divak2).place(x=310,y=200); b7=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents7,font=('arial', 15),command=week2divak3).place(x=310,y=260); b8=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents8,font=('arial', 15),command=week2divak4).place(x=310,y=320); b9=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents9,font=('arial', 15),command=week2wovak1).place(x=520,y=140); b10=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents10,font=('arial', 15),command=week2wovak2).place(x=520,y=200); b11=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents11,font=('arial', 15),command=week2wovak3).place(x=520,y=260); b12=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents12,font=('arial', 15),command=week2wovak4).place(x=520,y=320); b13=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents13,font=('arial', 15),command=week2dovak1).place(x=730,y=140); b14=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents14,font=('arial', 15),command=week2dovak2).place(x=730,y=200); b15=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents15,font=('arial', 15),command=week2dovak3).place(x=730,y=260); b16=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents16,font=('arial', 15),command=week2dovak4).place(x=730,y=320); b17=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents17,font=('arial', 15),command=week2vrvak1).place(x=940,y=140); b18=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents18,font=('arial', 15),command=week2vrvak2).place(x=940,y=200); b19=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents19,font=('arial', 15),command=week2vrvak3).place(x=940,y=260); b20=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents20,font=('arial', 15),command=week2vrvak4).place(x=940,y=320); b21=HoverButton(LG,bg='spring green',bd=0,width=4,height=10,text="<",font=('arial', 20),activebackground='gray79',command=knorth).place(x=15,y=200)
        #-------labels met de toetsen erin--------------#
        Label(LG,bg='white',bd=0,width=17,height=8,text=f_contents47,font=('arial', 15)).place(x=100,y=530)
        Label(LG,bg='white',bd=0,width=17,height=8,text=f_contents48,font=('arial', 15)).place(x=310,y=530)
        l3=Label(LG,bg='white',bd=0,width=17,height=8,text=f_contents49,font=('arial', 15)).place(x=520,y=530)
        l4=Label(LG,bg='white',bd=0,width=17,height=8,text=f_contents50,font=('arial', 15)).place(x=730,y=530)
        l5=Label(LG,bg='white',bd=0,width=17,height=8,text=f_contents51,font=('arial', 15)).place(x=940,y=530)
        #Button(LG,image=addvakimg,bd=0,bg="white").place(x=0,y=0)
        #-------labels met de dagen erop----------------#
        l6=Label(LG,bg='white',bd=0,width=16,height=4,text="Maandag",font=('arial', 15, 'bold')).place(x=100,y=60); l7=Label(LG,bg='white',bd=0,width=16,height=4,text="Dinsdag",font=('arial', 15, 'bold')).place(x=310,y=60); l8=Label(LG,bg='white',bd=0,width=16,height=4,text="Woensdag",font=('arial', 15, 'bold')).place(x=520,y=60); l9=Label(LG,bg='white',bd=0,width=16,height=4,text="Donderdag",font=('arial', 15, 'bold')).place(x=730,y=60); l0=Label(LG,bg='white',bd=0,width=16,height=4,text="Vrijdag",font=('arial', 15, 'bold')).place(x=940,y=60)
        HoverLabel1(LG,bg='white',bd=0,width=30,height=4).place(x=100,y=380)
        HoverLabel2(LG,bg='white',bd=0,width=30,height=4).place(x=310,y=380)
        HoverLabel3(LG,bg='white',bd=0,width=30,height=4).place(x=520,y=380)
        HoverLabel4(LG,bg='white',bd=0,width=30,height=4).place(x=730,y=380)
        HoverLabel5(LG,bg='white',bd=0,width=30,height=4).place(x=940,y=380)
        
        #-------de datum bovenaan-----------------------#
        Label(LG,bg='white',bd=0,width=46,height=2,text="volgende week",font=('arial', 20, 'bold')).place(x=250,y=0)
        #-------de lijnen die als kader zijn------------#
        Canvas(LG,bg=safecolor,bd=0,height=1,width=1050).place(x=100,y=135)
        c2=Canvas(LG,bg=safecolor,bd=0,height=1,width=1050).place(x=100,y=139)
        c3=Canvas(LG,bg=safecolor,bd=0,height=1,width=1050).place(x=100,y=416)
        c4=Canvas(LG,bg=safecolor,bd=0,height=1,width=1050).place(x=100,y=420)
        c5=Canvas(LG,bg=safecolor2,bd=0,height=1,width=1050).place(x=100,y=526)
        c6=Canvas(LG,bg=safecolor2,bd=0,height=1,width=1050).place(x=100,y=530)
        c7=Canvas(LG,bg=safecolor2,bd=0,height=1,width=1050).place(x=100,y=686)
        c8=Canvas(LG,bg=safecolor2,bd=0,height=1,width=1050).place(x=100,y=690)
        
        c9=Canvas(LG,bg=safecolor,bd=0,height=285,width=1).place(x=98,y=135)
        c10=Canvas(LG,bg=safecolor,bd=0,height=285,width=1).place(x=102,y=135)
        c11=Canvas(LG,bg=safecolor,bd=0,height=285,width=1).place(x=308,y=135)
        c12=Canvas(LG,bg=safecolor,bd=0,height=285,width=1).place(x=312,y=135)
        c13=Canvas(LG,bg=safecolor,bd=0,height=285,width=1).place(x=518,y=135)
        c14=Canvas(LG,bg=safecolor,bd=0,height=285,width=1).place(x=522,y=135)
        c15=Canvas(LG,bg=safecolor,bd=0,height=285,width=1).place(x=728,y=135)
        c16=Canvas(LG,bg=safecolor,bd=0,height=285,width=1).place(x=732,y=135)
        c17=Canvas(LG,bg=safecolor,bd=0,height=285,width=1).place(x=938,y=135)
        c18=Canvas(LG,bg=safecolor,bd=0,height=285,width=1).place(x=942,y=135)
        c19=Canvas(LG,bg=safecolor,bd=0,height=285,width=1).place(x=1148,y=135)
        c20=Canvas(LG,bg=safecolor,bd=0,height=285,width=1).place(x=1152,y=135)
        
        c21=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=98,y=526)
        c22=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=102,y=526)
        c23=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=308,y=526)
        c24=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=312,y=526)
        c25=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=518,y=526)
        c26=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=522,y=526)
        c27=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=728,y=526)
        c28=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=732,y=526)
        c29=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=938,y=526)
        c30=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=942,y=526)
        c31=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=1148,y=526)
        c32=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=1152,y=526)
        c33=Label(LG,bg="white",bd=0,height=60,width=20).place(x=1160,y=180)    
    def aanpassen():
        Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0)
        def dezeweekmaandagvak1():
            f= open("maandagvak1.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekmaandagvak2():
            f= open("maandagvak2.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekmaandagvak3():
            f= open("maandagvak3.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekmaandagvak4():
            f= open("maandagvak4.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekdinsdagvak1():
            f= open("dinsdagvak1.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekdinsdagvak2():
            f= open("dinsdagvak2.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekdinsdagvak3():
            f= open("dinsdagvak3.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekdinsdagvak4():
            f= open("dinsdagvak4.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekwoensdagvak1():
            f= open("woensdagvak1.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekwoensdagvak2():
            f= open("woensdagvak2.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekwoensdagvak3():
            f= open("woensdagvak3.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekwoensdagvak4():
            f= open("woensdagvak4.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekdonderdagvak1():
            f= open("donderdagvak1.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekdonderdagvak2():
            f= open("donderdagvak2.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekdonderdagvak3():
            f= open("donderdagvak3.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekdonderdagvak4():
            f= open("donderdagvak4.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekvrijdagvak1():
            f= open("vrijdagvak1.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekvrijdagvak2():
            f= open("vrijdagvak2.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekvrijdagvak3():
            f= open("vrijdagvak3.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekvrijdagvak4():
            f= open("vrijdagvak4.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekmaandaghuiswerk1():
            f= open("maandaghuiswerk1.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekmaandaghuiswerk1():
            f= open("maandaghuiswerk1.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekmaandaghuiswerk2():
            f= open("maandaghuiswerk2.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekmaandaghuiswerk3():
            f= open("maandaghuiswerk3.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekmaandaghuiswerk4():
            f= open("maandaghuiswerk4.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekdinsdaghuiswerk1():
            f= open("dinsdaghuiswerk1.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekdinsdaghuiswerk2():
            f= open("dinsdaghuiswerk2.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekdinsdaghuiswerk3():
            f= open("dinsdaghuiswerk3.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekdinsdaghuiswerk4():
            f= open("dinsdaghuiswerk4.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekwoensdaghuiswerk1():
            f= open("woensdaghuiswerk1.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekwoensdaghuiswerk2():
            f= open("woensdaghuiswerk2.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekwoensdaghuiswerk3():
            f= open("woensdaghuiswerk3.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekwoensdaghuiswerk4():
            f= open("woensdaghuiswerk4.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekdonderdaghuiswerk1():
            f= open("donderdaghuiswerk1.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekdonderdaghuiswerk2():
            f= open("donderdaghuiswerk2.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekdonderdaghuiswerk3():
            f= open("donderdaghuiswerk3.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekdonderdaghuiswerk4():
            f= open("donderdaghuiswerk4.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekvrijdaghuiswerk1():
            f= open("vrijdaghuiswerk1.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekvrijdaghuiswerk2():
            f= open("vrijdaghuiswerk2.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekvrijdaghuiswerk3():
            f= open("vrijdaghuiswerk3.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dezeweekvrijdaghuiswerk4():
            f= open("vrijdaghuiswerk4.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def maandagtoetsen():
            f= open("maandagtoetsen.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def dinsdagtoetsen():
            f= open("dinsdagtoetsen.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def woensdagtoetsen():
            f= open("woensdagtoetsen.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def donderdagtoetsen():
            f= open("donderdagtoetsen.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return
        def vrijdagtoetsen():
            f= open("vrijdagtoetsen.txt"); aboutStud.delete(1.0,END); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(END, studGradeString); f.close(); return  
        def opslaan1(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('maandagvak1.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def opslaan2(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('maandagvak2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def opslaan3(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('maandagvak3.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def opslaan4(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('maandagvak4.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def opslaan5(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('dinsdagvak1.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def opslaan6(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('dinsdagvak2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def opslaan7(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('dinsdagvak3.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def opslaan8(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('dinsdagvak4.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def opslaan9(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('woensdagvak1.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def opslaan10(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('woensdagvak2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def opslaan11(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('woensdagvak3.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def opslaan12(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('woensdagvak4.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def opslaan13(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('donderdagvak1.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def opslaan14(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('donderdagvak2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def opslaan15(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('donderdagvak3.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def opslaan16(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('donderdagvak4.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def opslaan17(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('vrijdagvak1.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def opslaan18(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('vrijdagvak2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def opslaan19(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('vrijdagvak3.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def opslaan20(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('vrijdagvak4.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def terug1(): knorth(); menubar.destroy()
        def terug2(): homepage()
        def huiswerkopslaan1(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('maandaghuiswerk1.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def huiswerkopslaan2(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('maandaghuiswerk2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def huiswerkopslaan3(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('maandaghuiswerk3.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def huiswerkopslaan4(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('maandaghuiswerk4.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def huiswerkopslaan5(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('dinsdaghuiswerk1.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def huiswerkopslaan6(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('dinsdaghuiswerk2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def huiswerkopslaan7(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('dinsdaghuiswerk3.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def huiswerkopslaan8(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('dinsdaghuiswerk4.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def huiswerkopslaan9(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('woensdaghuiswerk1.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def huiswerkopslaan10(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('woensdaghuiswerk2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def huiswerkopslaan11(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('woensdaghuiswerk3.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def huiswerkopslaan12(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('woensdaghuiswerk4.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def huiswerkopslaan13(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('donderdaghuiswerk1.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def huiswerkopslaan14(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('donderdaghuiswerk2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def huiswerkopslaan15(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('donderdaghuiswerk3.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def huiswerkopslaan16(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('donderdaghuiswerk4.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def huiswerkopslaan17(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('vrijdaghuiswerk1.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def huiswerkopslaan18(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('vrijdaghuiswerk2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def huiswerkopslaan19(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('vrijdaghuiswerk3.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def huiswerkopslaan20(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('vrijdaghuiswerk4.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def toetsenopslaan1(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('maandagtoetsen.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def toetsenopslaan2(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('dinsdagtoetsen.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def toetsenopslaan3(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('woensdagtoetsen.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def toetsenopslaan4(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('donderdagtoetsen.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def toetsenopslaan5(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('vrijdagtoetsen.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def week2toetsenopslaan1(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('week2maandagtoetsen.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def week2toetsenopslaan2(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('week2dinsdagtoetsen.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def week2toetsenopslaan3(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('week2woensdagtoetsen.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def week2toetsenopslaan4(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('week2donderdagtoetsen.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def week2toetsenopslaan5(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('week2vrijdagtoetsen.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def week2huiswerkopslaan1(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('week2maandaghuiswerk1.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def week2huiswerkopslaan2(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('week2maandaghuiswerk2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def week2huiswerkopslaan3(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('week2maandaghuiswerk3.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def week2huiswerkopslaan4(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('week2maandaghuiswerk4.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def week2huiswerkopslaan5(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('week2dinsdaghuiswerk1.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def week2huiswerkopslaan6(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('week2dinsdaghuiswerk2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def week2huiswerkopslaan7(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('week2dinsdaghuiswerk3.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def week2huiswerkopslaan8(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('week2dinsdaghuiswerk4.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def week2huiswerkopslaan9(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('week2woensdaghuiswerk1.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def week2huiswerkopslaan10(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('week2woensdaghuiswerk2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def week2huiswerkopslaan11(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('week2woensdaghuiswerk3.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def week2huiswerkopslaan12(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('week2woensdaghuiswerk4.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def week2huiswerkopslaan13(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('week2donderdaghuiswerk1.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def week2huiswerkopslaan14(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('week2donderdaghuiswerk2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def week2huiswerkopslaan15(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('week2donderdaghuiswerk3.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def week2huiswerkopslaan16(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('week2donderdaghuiswerk4.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def week2huiswerkopslaan17(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('week2vrijdaghuiswerk1.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def week2huiswerkopslaan18(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('week2vrijdaghuiswerk2.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def week2huiswerkopslaan19(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('week2vrijdaghuiswerk3.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        def week2huiswerkopslaan20(): gradeUpdate = aboutStud.get(1.0,END); oTF = open('week2vrijdaghuiswerk4.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
        menubar = Menu(LG)
        filemenu = Menu(menubar,tearoff=0)
        g_contents1 = f_contents1 + "_huiswerk"
        g_contents2 = f_contents2 + "_huiswerk"
        g_contents3 = f_contents3 + "_huiswerk"
        g_contents4 = f_contents4 + "_huiswerk"
        g_contents5 = f_contents5 + "_huiswerk"
        g_contents6 = f_contents6 + "_huiswerk"
        g_contents7 = f_contents7 + "_huiswerk"
        g_contents8 = f_contents8 + "_huiswerk"
        g_contents9 = f_contents9 + "_huiswerk"
        g_contents10 = f_contents10 + "_huiswerk"
        g_contents11 = f_contents11 + "_huiswerk"
        g_contents12 = f_contents12 + "_huiswerk"
        g_contents13 = f_contents13 + "_huiswerk"
        g_contents14 = f_contents14 + "_huiswerk"
        g_contents15 = f_contents15 + "_huiswerk"
        g_contents16 = f_contents16 + "_huiswerk"
        g_contents17 = f_contents17 + "_huiswerk"
        g_contents18 = f_contents18 + "_huiswerk"
        g_contents19 = f_contents19 + "_huiswerk"
        g_contents20 = f_contents20 + "_huiswerk"
        #=======================================
        def weekdagen1():
            filemenu.add_command(label=f_contents1,command=dezeweekmaandagvak1)
            filemenu.add_command(label=f_contents2,command=dezeweekmaandagvak2)
            filemenu.add_command(label=f_contents3,command=dezeweekmaandagvak3)
            filemenu.add_command(label=f_contents4,command=dezeweekmaandagvak4)
            filemenu.add_command(label=f_contents5,command=dezeweekdinsdagvak1)
            filemenu.add_command(label=f_contents6,command=dezeweekdinsdagvak2)
            filemenu.add_command(label=f_contents7,command=dezeweekdinsdagvak3)
            filemenu.add_command(label=f_contents8,command=dezeweekdinsdagvak4)
            filemenu.add_command(label=f_contents9,command=dezeweekwoensdagvak1)
            filemenu.add_command(label=f_contents10,command=dezeweekwoensdagvak2)
            filemenu.add_command(label=f_contents11,command=dezeweekwoensdagvak3)
            filemenu.add_command(label=f_contents12,command=dezeweekwoensdagvak4)
            filemenu.add_command(label=f_contents13,command=dezeweekdonderdagvak1)
            filemenu.add_command(label=f_contents14,command=dezeweekdonderdagvak2)
            filemenu.add_command(label=f_contents15,command=dezeweekdonderdagvak3)
            filemenu.add_command(label=f_contents16,command=dezeweekdonderdagvak4)
            filemenu.add_command(label=f_contents17,command=dezeweekvrijdagvak1)
            filemenu.add_command(label=f_contents18,command=dezeweekvrijdagvak2)
            filemenu.add_command(label=f_contents19,command=dezeweekvrijdagvak3)
            filemenu.add_command(label=f_contents20,command=dezeweekvrijdagvak4)
        def huiswerkweekdagen1():
            filemenu.add_command(label=g_contents1,command=dezeweekmaandaghuiswerk1)
            filemenu.add_command(label=g_contents2,command=dezeweekmaandaghuiswerk2)
            filemenu.add_command(label=g_contents3,command=dezeweekmaandaghuiswerk3)
            filemenu.add_command(label=g_contents4,command=dezeweekmaandaghuiswerk4)
            filemenu.add_command(label=g_contents5,command=dezeweekdinsdaghuiswerk1)
            filemenu.add_command(label=g_contents6,command=dezeweekdinsdaghuiswerk2)
            filemenu.add_command(label=g_contents7,command=dezeweekdinsdaghuiswerk3)
            filemenu.add_command(label=g_contents8,command=dezeweekdinsdaghuiswerk4)
            filemenu.add_command(label=g_contents9,command=dezeweekwoensdaghuiswerk1)
            filemenu.add_command(label=g_contents10,command=dezeweekwoensdaghuiswerk2)
            filemenu.add_command(label=g_contents11,command=dezeweekwoensdaghuiswerk3)
            filemenu.add_command(label=g_contents12,command=dezeweekwoensdaghuiswerk4)
            filemenu.add_command(label=g_contents13,command=dezeweekdonderdaghuiswerk1)
            filemenu.add_command(label=g_contents14,command=dezeweekdonderdaghuiswerk2)
            filemenu.add_command(label=g_contents15,command=dezeweekdonderdaghuiswerk3)
            filemenu.add_command(label=g_contents16,command=dezeweekdonderdaghuiswerk4)
            filemenu.add_command(label=g_contents17,command=dezeweekvrijdaghuiswerk1)
            filemenu.add_command(label=g_contents18,command=dezeweekvrijdaghuiswerk2)
            filemenu.add_command(label=g_contents19,command=dezeweekvrijdaghuiswerk3)
            filemenu.add_command(label=g_contents20,command=dezeweekvrijdaghuiswerk4)
        def toetsen():
            filemenu.add_command(label="maandag",command=maandagtoetsen)
            filemenu.add_command(label="dinsdag",command=dinsdagtoetsen)
            filemenu.add_command(label="woensdag",command=woensdagtoetsen)
            filemenu.add_command(label="donderdag",command=donderdagtoetsen)
            filemenu.add_command(label="vrijdag",command=vrijdagtoetsen)
        menubar.add_cascade(label="weken",menu=filemenu)
        huiswerkmenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="deze week",command=weekdagen1)
        filemenu.add_command(label="huiswerk",command=huiswerkweekdagen1)
        filemenu.add_command(label="toetsen",command=toetsen)
        filemenu.add_command(label="terug",command=terug1)
        filemenu.add_separator()
        menubar.add_cascade(label="huiswerk", command=huiswerkmenu); LG.config(menu=menubar); aboutStud = Text(LG); aboutStud.insert(END, "selecteer dag bovenaan"); aboutStud.place(x=400,y=200)
        def vorige1(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="maandag vak 1", width = 30, command=opslaan1).place(x=0,y=0); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=volgende1).place(x=80,y=50); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="", width = 10).place(x=0,y=50)
        def volgende1(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="maandag vak 2", width = 30, command=opslaan2).place(x=0,y=0); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=volgende2).place(x=80,y=50); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=vorige1).place(x=0,y=50)
        def volgende2(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="maandag vak 3", width = 30, command=opslaan3).place(x=0,y=0); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=volgende3).place(x=80,y=50); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=volgende1).place(x=0,y=50)
        def volgende3(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="maandag vak 4", width = 30, command=opslaan4).place(x=0,y=0); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=volgende4).place(x=80,y=50); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=volgende2).place(x=0,y=50)
        def volgende4(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="dinsdag vak 1", width = 30, command=opslaan5).place(x=0,y=0); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=volgende5).place(x=80,y=50); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=volgende3).place(x=0,y=50)
        def volgende5(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="dinsdag vak 2", width = 30, command=opslaan6).place(x=0,y=0); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=volgende6).place(x=80,y=50); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=volgende4).place(x=0,y=50)
        def volgende6(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="dinsdag vak 3", width = 30, command=opslaan7).place(x=0,y=0); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=volgende7).place(x=80,y=50); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=volgende5).place(x=0,y=50)
        def volgende7(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="dinsdag vak 4", width = 30, command=opslaan8).place(x=0,y=0); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=volgende8).place(x=80,y=50); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=volgende6).place(x=0,y=50)
        def volgende8(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="woensdag vak 1", width = 30, command=opslaan9).place(x=0,y=0); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=volgende9).place(x=80,y=50); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=volgende7).place(x=0,y=50)
        def volgende9(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="woensdag vak 2", width = 30, command=opslaan10).place(x=0,y=0); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=volgende10).place(x=80,y=50); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=volgende8).place(x=0,y=50)
        def volgende10(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="woensdag vak 3", width = 30, command=opslaan11).place(x=0,y=0); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=volgende11).place(x=80,y=50); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=volgende9).place(x=0,y=50)
        def volgende11(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="woensdag vak 4", width = 30, command=opslaan12).place(x=0,y=0); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=volgende12).place(x=80,y=50); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=volgende10).place(x=0,y=50)
        def volgende12(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="donderdag vak 1", width = 30, command=opslaan13).place(x=0,y=0); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=volgende13).place(x=80,y=50); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=volgende11).place(x=0,y=50)
        def volgende13(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="donderdag vak 2", width = 30, command=opslaan14).place(x=0,y=0); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=volgende14).place(x=80,y=50); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=volgende12).place(x=0,y=50)
        def volgende14(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="donderdag vak 3", width = 30, command=opslaan15).place(x=0,y=0); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=volgende15).place(x=80,y=50); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=volgende13).place(x=0,y=50)
        def volgende15(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="donderdag vak 4", width = 30, command=opslaan16).place(x=0,y=0); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=volgende16).place(x=80,y=50); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=volgende14).place(x=0,y=50)
        def volgende16(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="vrijdag vak 1", width = 30, command=opslaan17).place(x=0,y=0); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=volgende17).place(x=80,y=50); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=volgende15).place(x=0,y=50)
        def volgende17(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="vrijdag vak 2", width = 30, command=opslaan18).place(x=0,y=0); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=volgende18).place(x=80,y=50);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=volgende16).place(x=0,y=50)
        def volgende18(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="vrijdag vak 3", width = 30, command=opslaan19).place(x=0,y=0); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=volgende19).place(x=80,y=50); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=volgende17).place(x=0,y=50)
        def volgende19(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="vrijdag vak 4", width = 30, command=opslaan20).place(x=0,y=0); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="", width = 10).place(x=80,y=50); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=volgende18).place(x=0,y=50)

#==========================
        def huiswerkvorige1(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">>>", width = 10, command=week2huiswerkvolgende1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=g_contents1, width = 30, command=huiswerkopslaan1).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=huiswerkvolgende1).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="", width = 10).place(x=0,y=150)
        def huiswerkvolgende1(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">>>", width = 10, command=week2huiswerkvolgende1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=g_contents2, width = 30, command=huiswerkopslaan2).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=huiswerkvolgende2).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=huiswerkvorige1).place(x=0,y=150)
        def huiswerkvolgende2(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">>>", width = 10, command=week2huiswerkvolgende1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=g_contents3, width = 30, command=huiswerkopslaan3).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=huiswerkvolgende3).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=huiswerkvolgende1).place(x=0,y=150)
        def huiswerkvolgende3(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">>>", width = 10, command=week2huiswerkvolgende1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=g_contents4, width = 30, command=huiswerkopslaan4).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=huiswerkvolgende4).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=huiswerkvolgende2).place(x=0,y=150)
        def huiswerkvolgende4(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">>>", width = 10, command=week2huiswerkvolgende1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=g_contents5, width = 30, command=huiswerkopslaan5).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=huiswerkvolgende5).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=huiswerkvolgende3).place(x=0,y=150)
        def huiswerkvolgende5(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">>>", width = 10, command=week2huiswerkvolgende1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=g_contents6, width = 30, command=huiswerkopslaan6).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=huiswerkvolgende6).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=huiswerkvolgende4).place(x=0,y=150)
        def huiswerkvolgende6(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">>>", width = 10, command=week2huiswerkvolgende1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=g_contents7, width = 30, command=huiswerkopslaan7).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=huiswerkvolgende7).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=huiswerkvolgende5).place(x=0,y=150)
        def huiswerkvolgende7(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">>>", width = 10, command=week2huiswerkvolgende1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=g_contents8, width = 30, command=huiswerkopslaan8).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=huiswerkvolgende8).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=huiswerkvolgende6).place(x=0,y=150)
        def huiswerkvolgende8(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">>>", width = 10, command=week2huiswerkvolgende1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=g_contents9, width = 30, command=huiswerkopslaan9).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=huiswerkvolgende9).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=huiswerkvolgende7).place(x=0,y=150)
        def huiswerkvolgende9(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">>>", width = 10, command=week2huiswerkvolgende1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=g_contents10, width = 30, command=huiswerkopslaan10).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=huiswerkvolgende10).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=huiswerkvolgende8).place(x=0,y=150)
        def huiswerkvolgende10(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">>>", width = 10, command=week2huiswerkvolgende1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=g_contents11, width = 30, command=huiswerkopslaan11).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=huiswerkvolgende11).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=huiswerkvolgende9).place(x=0,y=150)
        def huiswerkvolgende11(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">>>", width = 10, command=week2huiswerkvolgende1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=g_contents12, width = 30, command=huiswerkopslaan12).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=huiswerkvolgende12).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=huiswerkvolgende10).place(x=0,y=150)
        def huiswerkvolgende12(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">>>", width = 10, command=week2huiswerkvolgende1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=g_contents13, width = 30, command=huiswerkopslaan13).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=huiswerkvolgende13).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=huiswerkvolgende11).place(x=0,y=150)
        def huiswerkvolgende13(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">>>", width = 10, command=week2huiswerkvolgende1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=g_contents14, width = 30, command=huiswerkopslaan14).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=huiswerkvolgende14).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=huiswerkvolgende12).place(x=0,y=150)
        def huiswerkvolgende14(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">>>", width = 10, command=week2huiswerkvolgende1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=g_contents15, width = 30, command=huiswerkopslaan15).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=huiswerkvolgende15).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=huiswerkvolgende13).place(x=0,y=150)
        def huiswerkvolgende15(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">>>", width = 10, command=week2huiswerkvolgende1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=g_contents16, width = 30, command=huiswerkopslaan16).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=huiswerkvolgende16).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=huiswerkvolgende14).place(x=0,y=150)
        def huiswerkvolgende16(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">>>", width = 10, command=week2huiswerkvolgende1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=g_contents17, width = 30, command=huiswerkopslaan17).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=huiswerkvolgende17).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=huiswerkvolgende15).place(x=0,y=150)
        def huiswerkvolgende17(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">>>", width = 10, command=week2huiswerkvolgende1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=g_contents18, width = 30, command=huiswerkopslaan18).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=huiswerkvolgende18).place(x=80,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=huiswerkvolgende16).place(x=0,y=150)
        def huiswerkvolgende18(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">>>", width = 10, command=week2huiswerkvolgende1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=g_contents19, width = 30, command=huiswerkopslaan19).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=huiswerkvolgende19).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=huiswerkvolgende17).place(x=0,y=150)
        def huiswerkvolgende19(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">>>", width = 10, command=week2huiswerkvolgende1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=g_contents20, width = 30, command=huiswerkopslaan20).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="", width = 10).place(x=80,y=50); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=huiswerkvolgende18).place(x=0,y=50)
#==========================
        def week2huiswerkvorige1(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<<<", width = 10, command=huiswerkvorige1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="w2_"+ g_contents1, width = 30, command=week2huiswerkopslaan1).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=week2huiswerkvolgende1).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="", width = 10).place(x=0,y=150)
        def week2huiswerkvolgende1(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<<<", width = 10, command=huiswerkvorige1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="w2_"+ g_contents2, width = 30, command=week2huiswerkopslaan2).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=week2huiswerkvolgende2).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=week2huiswerkvorige1).place(x=0,y=150)
        def week2huiswerkvolgende2(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<<<", width = 10, command=huiswerkvorige1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="w2_"+ g_contents3, width = 30, command=week2huiswerkopslaan3).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=week2huiswerkvolgende3).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=week2huiswerkvolgende1).place(x=0,y=150)
        def week2huiswerkvolgende3(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<<<", width = 10, command=huiswerkvorige1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="w2_"+ g_contents4, width = 30, command=week2huiswerkopslaan4).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=week2huiswerkvolgende4).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=week2huiswerkvolgende2).place(x=0,y=150)
        def week2huiswerkvolgende4(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<<<", width = 10, command=huiswerkvorige1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="w2_"+ g_contents5, width = 30, command=week2huiswerkopslaan5).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=week2huiswerkvolgende5).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=week2huiswerkvolgende3).place(x=0,y=150)
        def week2huiswerkvolgende5(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<<<", width = 10, command=huiswerkvorige1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="w2_"+ g_contents6, width = 30, command=week2huiswerkopslaan6).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=week2huiswerkvolgende6).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=week2huiswerkvolgende4).place(x=0,y=150)
        def week2huiswerkvolgende6(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<<<", width = 10, command=huiswerkvorige1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="w2_"+ g_contents7, width = 30, command=week2huiswerkopslaan7).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=week2huiswerkvolgende7).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=week2huiswerkvolgende5).place(x=0,y=150)
        def week2huiswerkvolgende7(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<<<", width = 10, command=huiswerkvorige1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="w2_"+ g_contents8, width = 30, command=week2huiswerkopslaan8).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=week2huiswerkvolgende8).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=week2huiswerkvolgende6).place(x=0,y=150)
        def week2huiswerkvolgende8(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<<<", width = 10, command=huiswerkvorige1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="w2_"+ g_contents9, width = 30, command=week2huiswerkopslaan9).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=week2huiswerkvolgende9).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=week2huiswerkvolgende7).place(x=0,y=150)
        def week2huiswerkvolgende9(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<<<", width = 10, command=huiswerkvorige1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="w2_"+ g_contents10, width = 30, command=week2huiswerkopslaan10).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=week2huiswerkvolgende10).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=week2huiswerkvolgende8).place(x=0,y=150)
        def week2huiswerkvolgende10(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<<<", width = 10, command=huiswerkvorige1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="w2_"+ g_contents11, width = 30, command=week2huiswerkopslaan11).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=week2huiswerkvolgende11).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=week2huiswerkvolgende9).place(x=0,y=150)
        def week2huiswerkvolgende11(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<<<", width = 10, command=huiswerkvorige1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="w2_"+ g_contents12, width = 30, command=week2huiswerkopslaan12).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=week2huiswerkvolgende12).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=week2huiswerkvolgende10).place(x=0,y=150)
        def week2huiswerkvolgende12(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<<<", width = 10, command=huiswerkvorige1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="w2_"+ g_contents13, width = 30, command=week2huiswerkopslaan13).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=week2huiswerkvolgende13).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=week2huiswerkvolgende11).place(x=0,y=150)
        def week2huiswerkvolgende13(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<<<", width = 10, command=huiswerkvorige1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="w2_"+ g_contents14, width = 30, command=week2huiswerkopslaan14).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=week2huiswerkvolgende14).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=week2huiswerkvolgende12).place(x=0,y=150)
        def week2huiswerkvolgende14(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<<<", width = 10, command=huiswerkvorige1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="w2_"+ g_contents15, width = 30, command=week2huiswerkopslaan15).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=week2huiswerkvolgende15).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=week2huiswerkvolgende13).place(x=0,y=150)
        def week2huiswerkvolgende15(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<<<", width = 10, command=huiswerkvorige1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="w2_"+ g_contents16, width = 30, command=week2huiswerkopslaan16).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=week2huiswerkvolgende16).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=week2huiswerkvolgende14).place(x=0,y=150)
        def week2huiswerkvolgende16(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<<<", width = 10, command=huiswerkvorige1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="w2_"+ g_contents17, width = 30, command=week2huiswerkopslaan17).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=week2huiswerkvolgende17).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=week2huiswerkvolgende15).place(x=0,y=150)
        def week2huiswerkvolgende17(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<<<", width = 10, command=huiswerkvorige1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="w2_"+ g_contents18, width = 30, command=week2huiswerkopslaan18).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=week2huiswerkvolgende18).place(x=80,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=week2huiswerkvolgende16).place(x=0,y=150)
        def week2huiswerkvolgende18(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<<<", width = 10, command=huiswerkvorige1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="w2_"+ g_contents19, width = 30, command=week2huiswerkopslaan19).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=week2huiswerkvolgende19).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=week2huiswerkvolgende17).place(x=0,y=150)
        def week2huiswerkvolgende19(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<<<", width = 10, command=huiswerkvorige1).place(x=200,y=150);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="w2_"+ g_contents20, width = 30, command=week2huiswerkopslaan20).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="", width = 10).place(x=80,y=50); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=week2huiswerkvolgende18).place(x=0,y=50)
#==========================
        def week2toetsen():
            def week2toetsenvorige1(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<<<", width = 10, command=toetsenvorige1).place(x=200,y=250);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="w2 maandag toetsen", width = 30, command=week2toetsenopslaan1).place(x=0,y=200); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=week2toetsenvolgende1).place(x=80,y=250); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="", width = 10).place(x=0,y=250)
            def week2toetsenvolgende1(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<<<", width = 10, command=toetsenvorige1).place(x=200,y=250);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="w2 dinsdag toetsen", width = 30, command=week2toetsenopslaan2).place(x=0,y=200); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=week2toetsenvolgende2).place(x=80,y=250); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=week2toetsenvorige1).place(x=0,y=250)
            def week2toetsenvolgende2(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<<<", width = 10, command=toetsenvorige1).place(x=200,y=250);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="w2 woensdag toetsen", width = 30, command=week2toetsenopslaan3).place(x=0,y=200); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=week2toetsenvolgende3).place(x=80,y=250); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=week2toetsenvolgende1).place(x=0,y=250)
            def week2toetsenvolgende3(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<<<", width = 10, command=toetsenvorige1).place(x=200,y=250);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="w2 donderdag toetsen", width = 30, command=week2toetsenopslaan4).place(x=0,y=200); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=week2toetsenvolgende4).place(x=80,y=250); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=week2toetsenvolgende2).place(x=0,y=250)
            def week2toetsenvolgende4(): HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<<<", width = 10, command=toetsenvorige1).place(x=200,y=250);HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="w2 vrijdag toetsen", width = 30, command=week2toetsenopslaan5).place(x=0,y=200); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="", width = 10).place(x=80,y=250); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=week2toetsenvolgende3).place(x=0,y=250)
            HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="w2 maandag toetsen", width = 30, command=week2toetsenopslaan1).place(x=0,y=200); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<<<", width = 10, command=toetsenvorige1).place(x=200,y=250); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=week2toetsenvolgende1).place(x=80,y=250); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="", width = 10).place(x=0,y=250)
        def toetsenvorige1(): b4 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">>>", width = 10, command=week2toetsen).place(x=200,y=250); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="maandag toetsen", width = 30, command=toetsenopslaan1).place(x=0,y=200); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=toetsenvolgende1).place(x=80,y=250); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="", width = 10).place(x=0,y=250)
        def toetsenvolgende1(): b4 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">>>", width = 10, command=week2toetsen).place(x=200,y=250); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="dinsdag toetsen", width = 30, command=toetsenopslaan2).place(x=0,y=200); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=toetsenvolgende2).place(x=80,y=250); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=toetsenvorige1).place(x=0,y=250)
        def toetsenvolgende2(): b4 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">>>", width = 10, command=week2toetsen).place(x=200,y=250); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="woensdag toetsen", width = 30, command=toetsenopslaan3).place(x=0,y=200); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=toetsenvolgende3).place(x=80,y=250); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=toetsenvolgende1).place(x=0,y=250)
        def toetsenvolgende3(): b4 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">>>", width = 10, command=week2toetsen).place(x=200,y=250); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="donderdag toetsen", width = 30, command=toetsenopslaan4).place(x=0,y=200); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=toetsenvolgende4).place(x=80,y=250); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=toetsenvolgende2).place(x=0,y=250)
        def toetsenvolgende4(): b4 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">>>", width = 10, command=week2toetsen).place(x=200,y=250); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="vrijdag toetsen", width = 30, command=toetsenopslaan5).place(x=0,y=200); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="", width = 10).place(x=80,y=250); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="<", width = 10, command=toetsenvolgende3).place(x=0,y=250); b4 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">>>", width = 10, command=week2toetsen).place(x=200,y=250)
        HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="maandag vak 1", width = 30, command=opslaan1).place(x=0,y=0); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=volgende1).place(x=80,y=50)
        HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=g_contents1, width = 30, command=huiswerkopslaan1).place(x=0,y=100); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=huiswerkvolgende1).place(x=80,y=150); HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">>>", width = 10, command=week2huiswerkvolgende1).place(x=200,y=150)
        HoverButton(LG,bg="white",bd=0,font=('arial', 15), text="maandag toetsen", width = 30, command=toetsenopslaan1).place(x=0,y=200);b4 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">>>", width = 10, command=week2toetsen).place(x=200,y=250); b2 = HoverButton(LG,bg="white",bd=0,font=('arial', 15), text=">", width = 10, command=toetsenvolgende1).place(x=80,y=250)
    def mavak1(): Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents21,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
    def mavak2(): Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents22,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
    def mavak3(): Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents23,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
    def mavak4(): Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents24,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
    def divak1(): Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents25,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
    def divak2(): Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents26,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
    def divak3(): Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents27,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
    def divak4(): Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents28,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
    def wovak1(): Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents29,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
    def wovak2(): Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents30,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
    def wovak3(): Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents31,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
    def wovak4(): Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents32,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
    def dovak1(): Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents33,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
    def dovak2(): Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents34,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
    def dovak3(): Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents35,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
    def dovak4(): Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents36,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
    def vrvak1(): Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents37,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
    def vrvak2(): Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents38,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
    def vrvak3(): Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents39,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
    def vrvak4(): Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents40,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
    def addvak1():
        GU="486";oTF=open('changey1.txt', 'w');oTF.write(GU);oTF.close()
        GU="490";oTF=open('changey2.txt', 'w');oTF.write(GU);oTF.close()
        GU="355";oTF=open('Extraheight1.txt', 'w');oTF.write(GU);oTF.close()
        GU="355";oTF=open('Extraheight2.txt', 'w');oTF.write(GU);oTF.close()
        data[0] = "1"
        with open('addbutton.txt', 'w') as file: file.writelines( data )
        Frame(LG,bg="white",bd=0,height=10,width=1050).place(x=100,y=416)
        Frame(LG,bg="white",bd=0,height=285,width=6).place(x=98,y=135)
        Frame(LG,bg="white",bd=0,height=285,width=6).place(x=308,y=135)
        HoverButton1(LG,bg='white',bd=0,width=16,height=4,text=f_contents72,font=('arial', 15)).place(x=100,y=330)
        HoverLabel6(LG,bg='white',bd=0,width=30,height=4).place(x=100,y=550)
        lijnen()
    def addvak2():
        GU="486";oTF=open('changey3.txt', 'w');oTF.write(GU);oTF.close()
        GU="490";oTF=open('changey4.txt', 'w');oTF.write(GU);oTF.close()
        GU="355";oTF=open('Extraheight2.txt', 'w');oTF.write(GU);oTF.close()
        GU="355";oTF=open('Extraheight3.txt', 'w');oTF.write(GU);oTF.close()
        Frame(LG,bg="white",bd=0,height=10,width=1050).place(x=100,y=416)
        Frame(LG,bg="white",bd=0,height=285,width=6).place(x=308,y=135)
        Frame(LG,bg="white",bd=0,height=285,width=6).place(x=518,y=135)
        HoverLabel2(LG,bg='white',bd=0,width=30,height=4).place(x=100,y=380)
        lijnen()
    def addvak3():
        GU="486";oTF=open('changey5.txt', 'w');oTF.write(GU);oTF.close()
        GU="490";oTF=open('changey6.txt', 'w');oTF.write(GU);oTF.close()
        GU="355";oTF=open('Extraheight3.txt', 'w');oTF.write(GU);oTF.close()
        GU="355";oTF=open('Extraheight4.txt', 'w');oTF.write(GU);oTF.close()
        Frame(LG,bg="white",bd=0,height=10,width=1050).place(x=100,y=416)
        Frame(LG,bg="white",bd=0,height=285,width=6).place(x=518,y=135)
        Frame(LG,bg="white",bd=0,height=285,width=6).place(x=728,y=135)
        HoverLabel3(LG,bg='white',bd=0,width=30,height=4).place(x=100,y=380)
        lijnen()
    def addvak4():
        GU="486";oTF=open('changey7.txt', 'w');oTF.write(GU);oTF.close()
        GU="490";oTF=open('changey8.txt', 'w');oTF.write(GU);oTF.close()
        GU="355";oTF=open('Extraheight4.txt', 'w');oTF.write(GU);oTF.close()
        GU="355";oTF=open('Extraheight5.txt', 'w');oTF.write(GU);oTF.close()
        Frame(LG,bg="white",bd=0,height=10,width=1050).place(x=100,y=416)
        Frame(LG,bg="white",bd=0,height=285,width=6).place(x=728,y=135)
        Frame(LG,bg="white",bd=0,height=285,width=6).place(x=938,y=135)
        HoverLabel4(LG,bg='white',bd=0,width=30,height=4).place(x=100,y=380)
        lijnen()
    def addvak5():
        GU="486";oTF=open('changey9.txt', 'w');oTF.write(GU);oTF.close()
        GU="490";oTF=open('changey10.txt', 'w');oTF.write(GU);oTF.close()
        GU="355";oTF=open('Extraheight5.txt', 'w');oTF.write(GU);oTF.close()
        GU="355";oTF=open('Extraheight6.txt', 'w');oTF.write(GU);oTF.close()
        Frame(LG,bg="white",bd=0,height=10,width=1050).place(x=100,y=416)
        Frame(LG,bg="white",bd=0,height=285,width=6).place(x=938,y=135)
        Frame(LG,bg="white",bd=0,height=285,width=6).place(x=1148,y=135)
        HoverLabel5(LG,bg='white',bd=0,width=30,height=4).place(x=100,y=380)
        lijnen()
    class HoverLabel1(tk.Label):
            def __init__(self, master, **kw):
                tk.Label.__init__(self,master=master,**kw)
                self.bind("<Enter>", self.on_enter)
                self.bind("<Leave>", self.on_leave)
            def on_enter(self, e):
                Button(LG,image=img6,bd=0,bg="white",command=addvak1).place(x=110,y=380)
            def on_leave(self, e):
                time.sleep(0.3)
                HoverLabel1(LG,bg='white',bd=0,width=28,height=2).place(x=110,y=380)
    class HoverLabel2(tk.Button):
            def __init__(self, master, **kw):
                tk.Label.__init__(self,master=master,**kw)
                self.bind("<Enter>", self.on_enter)
                self.bind("<Leave>", self.on_leave)
            def on_enter(self, e):
                Button(LG,image=img6,bd=0,bg="white",command=addvak2).place(x=320,y=380)
            def on_leave(self, e):
                time.sleep(0.3)
                HoverLabel2(LG,bg='white',bd=0,width=28,height=2).place(x=320,y=380)
    class HoverLabel3(tk.Button):
            def __init__(self, master, **kw):
                tk.Label.__init__(self,master=master,**kw)
                self.bind("<Enter>", self.on_enter)
                self.bind("<Leave>", self.on_leave)
            def on_enter(self, e):
                Button(LG,image=img6,bd=0,bg="white",command=addvak3).place(x=530,y=380)
            def on_leave(self, e):
                time.sleep(0.3)
                HoverLabel3(LG,bg='white',bd=0,width=28,height=2).place(x=530,y=380)
    class HoverLabel4(tk.Button):
            def __init__(self, master, **kw):
                tk.Label.__init__(self,master=master,**kw)
                self.bind("<Enter>", self.on_enter)
                self.bind("<Leave>", self.on_leave)
            def on_enter(self, e):
                Button(LG,image=img6,bd=0,bg="white",command=addvak4).place(x=740,y=380)
            def on_leave(self, e):
                time.sleep(0.3)
                HoverLabel4(LG,bg='white',bd=0,width=28,height=2).place(x=740,y=380)
    class HoverLabel5(tk.Button):
            def __init__(self, master, **kw):
                tk.Label.__init__(self,master=master,**kw)
                self.bind("<Enter>", self.on_enter)
                self.bind("<Leave>", self.on_leave)
            def on_enter(self, e):
                Button(LG,image=img6,bd=0,bg="white",command=addvak5).place(x=950,y=380)
            def on_leave(self, e):
                time.sleep(0.3)
                HoverLabel5(LG,bg='white',bd=0,width=28,height=2).place(x=950,y=380)
    class HoverLabel6(tk.Button):
            def __init__(self, master, **kw):
                tk.Label.__init__(self,master=master,**kw)
                self.bind("<Enter>", self.on_enter)
                self.bind("<Leave>", self.on_leave)
            def on_enter(self, e):
                Button(LG,image=img6,bd=0,bg="white",command=addvak5).place(x=950,y=550)
            def on_leave(self, e):
                time.sleep(0.3)
                HoverLabel5(LG,bg='white',bd=0,width=28,height=2).place(x=950,y=550)
    def delbutton():
        Button(LG,image=img10,bd=0,bg="white").place(x=280,y=310)
    def deletedelbutton():
        Button(LG,image=img11,bd=0,bg="white").place(x=280,y=310)  
    class HoverButton1(tk.Button):
        def __init__(self, master, **kw):
            tk.Button.__init__(self,master=master,**kw)
            self.defaultBackground = self["background"]
            self.bind("<Enter>", self.on_enter)
            self.bind("<Leave>", self.on_leave)
        def on_enter(self, e):
            self['background'] = self['activebackground']
            delbutton()
        def on_leave(self, e):
            self['background'] = self.defaultBackground
            deletedelbutton()
    addbutton1 = open("addbutton.txt", "r").readlines()#[0]
    #-------dagen die naar huiswerk lijden----------#
    def vakkenmetdagen():
        HoverButton1(LG,bg='white',bd=0,width=16,height=4,text=f_contents1,font=('arial', 15),command=mavak1).place(x=100,y=140); HoverButton1(LG,bg='white',bd=0,width=16,height=4,text=f_contents2,font=('arial', 15),command=mavak2).place(x=100,y=200); HoverButton1(LG,bg='white',bd=0,width=16,height=4,text=f_contents3,font=('arial', 15),command=mavak3).place(x=100,y=260); b4=HoverButton1(LG,bg='white',bd=0,width=16,height=4,text=f_contents4,font=('arial', 15),command=mavak4).place(x=100,y=320); b5=HoverButton1(LG,bg='white',bd=0,width=16,height=4,text=f_contents5,font=('arial', 15),command=divak1).place(x=310,y=140); b6=HoverButton1(LG,bg='white',bd=0,width=16,height=4,text=f_contents6,font=('arial', 15),command=divak2).place(x=310,y=200); b7=HoverButton1(LG,bg='white',bd=0,width=16,height=4,text=f_contents7,font=('arial', 15),command=divak3).place(x=310,y=260); b8=HoverButton1(LG,bg='white',bd=0,width=16,height=4,text=f_contents8,font=('arial', 15),command=divak4).place(x=310,y=320); b9=HoverButton1(LG,bg='white',bd=0,width=16,height=4,text=f_contents9,font=('arial', 15),command=wovak1).place(x=520,y=140); b10=HoverButton1(LG,bg='white',bd=0,width=16,height=4,text=f_contents10,font=('arial', 15),command=wovak2).place(x=520,y=200); b11=HoverButton1(LG,bg='white',bd=0,width=16,height=4,text=f_contents11,font=('arial', 15),command=wovak3).place(x=520,y=260); b12=HoverButton1(LG,bg='white',bd=0,width=16,height=4,text=f_contents12,font=('arial', 15),command=wovak4).place(x=520,y=320); b13=HoverButton1(LG,bg='white',bd=0,width=16,height=4,text=f_contents13,font=('arial', 15),command=dovak1).place(x=730,y=140); b14=HoverButton1(LG,bg='white',bd=0,width=16,height=4,text=f_contents14,font=('arial', 15),command=dovak2).place(x=730,y=200); b15=HoverButton1(LG,bg='white',bd=0,width=16,height=4,text=f_contents15,font=('arial', 15),command=dovak3).place(x=730,y=260); b16=HoverButton1(LG,bg='white',bd=0,width=16,height=4,text=f_contents16,font=('arial', 15),command=dovak4).place(x=730,y=320); b17=HoverButton1(LG,bg='white',bd=0,width=16,height=4,text=f_contents17,font=('arial', 15),command=vrvak1).place(x=940,y=140); b18=HoverButton1(LG,bg='white',bd=0,width=16,height=4,text=f_contents18,font=('arial', 15),command=vrvak2).place(x=940,y=200); b19=HoverButton1(LG,bg='white',bd=0,width=16,height=4,text=f_contents19,font=('arial', 15),command=vrvak3).place(x=940,y=260); b20=HoverButton1(LG,bg='white',bd=0,width=16,height=4,text=f_contents20,font=('arial', 15),command=vrvak4).place(x=940,y=320) 
        if addbutton1 == "1": HoverButton1(LG,bg='white',bd=0,width=16,height=4,text=f_contents72,font=('arial', 15)).place(x=100,y=330)
            
    vakkenmetdagen()
    #-------labels met de toetsen erin--------------#
    Label(LG,bg='white',bd=0,width=17,height=8,text=f_contents41,font=('arial', 15)).place(x=100,y=530)
    Label(LG,bg='white',bd=0,width=17,height=8,text=f_contents42,font=('arial', 15)).place(x=310,y=530)
    l3=Label(LG,bg='white',bd=0,width=17,height=8,text=f_contents43,font=('arial', 15)).place(x=520,y=530)
    l4=Label(LG,bg='white',bd=0,width=17,height=8,text=f_contents44,font=('arial', 15)).place(x=730,y=530)
    l5=Label(LG,bg='white',bd=0,width=17,height=8,text=f_contents45,font=('arial', 15)).place(x=940,y=530)
    Label(LG,bg='white',bd=0,width=160,height=4).place(x=100,y=380)
    # Hoverlabels met een extra button toevoeg functie
    if addbutton1 == "0": HoverLabel1(LG,bg='white',bd=0,width=30,height=4).place(x=100,y=380)
    HoverLabel2(LG,bg='white',bd=0,width=30,height=4).place(x=310,y=380)
    HoverLabel3(LG,bg='white',bd=0,width=30,height=4).place(x=520,y=380)
    HoverLabel4(LG,bg='white',bd=0,width=30,height=4).place(x=730,y=380)
    HoverLabel5(LG,bg='white',bd=0,width=30,height=4).place(x=940,y=380)
        
    #-------labels met de dagen erop----------------#
    l6=Label(LG,bg='white',bd=0,width=16,height=4,text="Maandag",font=('arial', 15, 'bold')).place(x=100,y=60); l7=Label(LG,bg='white',bd=0,width=16,height=4,text="Dinsdag",font=('arial', 15, 'bold')).place(x=310,y=60); l8=Label(LG,bg='white',bd=0,width=16,height=4,text="Woensdag",font=('arial', 15, 'bold')).place(x=520,y=60); l9=Label(LG,bg='white',bd=0,width=16,height=4,text="Donderdag",font=('arial', 15, 'bold')).place(x=730,y=60); l0=Label(LG,bg='white',bd=0,width=16,height=4,text="Vrijdag",font=('arial', 15, 'bold')).place(x=940,y=60)
    #-------de datum bovenaan-----------------------#
    Label(LG,bg='white',bd=0,width=46,height=2,text="deze week",font=('arial', 20, 'bold')).place(x=250,y=0)
    #-------de lijnen die als kader zijn------------#
    def lijnen():
        changey1 = open("changey1.txt", "r").readlines()
        changey2 = open("changey2.txt", "r").readlines()
        changey3 = open("changey3.txt", "r").readlines()
        changey4 = open("changey4.txt", "r").readlines()
        changey5 = open("changey5.txt", "r").readlines()
        changey6 = open("changey6.txt", "r").readlines()
        changey7 = open("changey7.txt", "r").readlines()
        changey8 = open("changey8.txt", "r").readlines()
        changey9 = open("changey9.txt", "r").readlines()
        changey10 = open("changey10.txt", "r").readlines()

        height1 = open("Extraheight1.txt", "r").readlines()
        height2 = open("Extraheight2.txt", "r").readlines()
        height3 = open("Extraheight3.txt", "r").readlines()
        height4 = open("Extraheight4.txt", "r").readlines()
        height5 = open("Extraheight5.txt", "r").readlines()
        height6 = open("Extraheight6.txt", "r").readlines()
        # liggenlijnen voor vakken
        Canvas(LG,bg=safecolor,bd=0,height=1,width=1050).place(x=100,y=135)
        Canvas(LG,bg=safecolor,bd=0,height=1,width=1050).place(x=100,y=139)

        Canvas(LG,bg=safecolor,bd=0,height=1,width=210).place(x=100,y=changey1)
        Canvas(LG,bg=safecolor,bd=0,height=1,width=210).place(x=100,y=changey2)
        Canvas(LG,bg=safecolor,bd=0,height=1,width=210).place(x=310,y=changey3)
        Canvas(LG,bg=safecolor,bd=0,height=1,width=210).place(x=310,y=changey4)
        Canvas(LG,bg=safecolor,bd=0,height=1,width=210).place(x=520,y=changey5)
        Canvas(LG,bg=safecolor,bd=0,height=1,width=210).place(x=520,y=changey6)
        Canvas(LG,bg=safecolor,bd=0,height=1,width=210).place(x=730,y=changey7)
        Canvas(LG,bg=safecolor,bd=0,height=1,width=210).place(x=730,y=changey8)
        Canvas(LG,bg=safecolor,bd=0,height=1,width=210).place(x=940,y=changey9)
        Canvas(LG,bg=safecolor,bd=0,height=1,width=210).place(x=940,y=changey10)

        # liggende lijnen voor toetsen
        c5=Canvas(LG,bg=safecolor2,bd=0,height=1,width=1050).place(x=100,y=526)
        c6=Canvas(LG,bg=safecolor2,bd=0,height=1,width=1050).place(x=100,y=530)
        c7=Canvas(LG,bg=safecolor2,bd=0,height=1,width=1050).place(x=100,y=686)
        c8=Canvas(LG,bg=safecolor2,bd=0,height=1,width=1050).place(x=100,y=690)


        # rechtopstaande lijnen voor vakken
        Canvas(LG,bg=safecolor,bd=0,height=height1,width=1).place(x=98,y=135)
        Canvas(LG,bg=safecolor,bd=0,height=height1,width=1).place(x=102,y=135)
        Canvas(LG,bg=safecolor,bd=0,height=height2,width=1).place(x=308,y=135)
        Canvas(LG,bg=safecolor,bd=0,height=height2,width=1).place(x=312,y=135)
        Canvas(LG,bg=safecolor,bd=0,height=height3,width=1).place(x=518,y=135)
        Canvas(LG,bg=safecolor,bd=0,height=height3,width=1).place(x=522,y=135)
        Canvas(LG,bg=safecolor,bd=0,height=height4,width=1).place(x=728,y=135)
        Canvas(LG,bg=safecolor,bd=0,height=height4,width=1).place(x=732,y=135)
        Canvas(LG,bg=safecolor,bd=0,height=height5,width=1).place(x=938,y=135)
        Canvas(LG,bg=safecolor,bd=0,height=height5,width=1).place(x=942,y=135)
        Canvas(LG,bg=safecolor,bd=0,height=height6,width=1).place(x=1148,y=135)
        Canvas(LG,bg=safecolor,bd=0,height=height6,width=1).place(x=1152,y=135)


        # rechtopstaande lijnen voor toetsen
        c21=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=98,y=526)
        c22=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=102,y=526)
        c23=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=308,y=526)
        c24=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=312,y=526)
        c25=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=518,y=526)
        c26=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=522,y=526)
        c27=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=728,y=526)
        c28=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=732,y=526)
        c29=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=938,y=526)
        c30=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=942,y=526)
        c31=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=1148,y=526)
        c32=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=1152,y=526)

        
    lijnen()
    b21=HoverButton(LG,bg=safecolor,bd=0,width=4,height=10,text=">",font=('arial', 20),activebackground='gray79',command=week2).place(x=1190,y=200)
    def komendeweken():
        with open('dezemaand1.txt', 'r') as f: dezemaand1 = f.read()
        wekende=Tk(); wekende.attributes('-fullscreen',True); wekende.configure(background='white')
        def dezeweekmaand1():
            f= open("dezemaand1.txt"); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(1.0, studGradeString); f.close(); return
        def openFiles1(selection):
            if selection == "februari/april": dezeweekmaand1()
        def maandopslaan1():
             gradeUpdate = aboutStud.get(1.0,END)
             oTF = open('dezemaand1.txt', 'w'); oTF.write(gradeUpdate); oTF.close(); return
            
        aboutStud = Text(wekende); aboutStud.place(x=40,y=100)
        menu_bar = Menu(wekende)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Quit!", command=dezeweekmaand1)
        file_menu.add_command(label="Exit!", command=wekende.destroy)
        file_menu.add_command(label="End!", command=wekende.destroy)
        menu_bar.add_cascade(label="File", menu=file_menu)

        Label(wekende,font=('arial',15),text=dezemaand1,bg="white",bd=0).place(x=800,y=50)
        
        Button(wekende,bg="white",bd=0,text="opslaan",command=maandopslaan1).place(x=0,y=500)
        wekende.config(menu=menu_bar)
        wekende.mainloop()
    def overzicht():
        t1=Tk(); t1.attributes('-fullscreen',True); t1.configure(background='white')
        def overzichtweek2():
            Frame(t1,bg="white",bd=0,height=560,width=245).place(x=300,y=35); Frame(t1,bg="white",bd=0,height=560,width=245).place(x=970,y=35)
            Label(t1,font=('arial',15),text=f_contents52,bg="white",bd=0).place(x=300,y=35);Label(t1,font=('arial',15),text=f_contents53,bg="white",bd=0).place(x=300,y=85)
            Label(t1,font=('arial',15),text=f_contents54,bg="white",bd=0).place(x=300,y=135); Label(t1,font=('arial',15),text=f_contents55,bg="white",bd=0).place(x=300,y=185); Label(t1,font=('arial',15),text=f_contents56,bg="white",bd=0).place(x=300,y=235); Label(t1,font=('arial',15),text=f_contents57,bg="white",bd=0).place(x=300,y=285); Label(t1,font=('arial',15),text=f_contents58,bg="white",bd=0).place(x=300,y=335); Label(t1,font=('arial',15),text=f_contents59,bg="white",bd=0).place(x=300,y=385); Label(t1,font=('arial',15),text=f_contents60,bg="white",bd=0).place(x=300,y=435); Label(t1,font=('arial',15),text=f_contents61,bg="white",bd=0).place(x=300,y=485); Label(t1,font=('arial',15),text=f_contents62,bg="white",bd=0).place(x=300,y=535); Label(t1,font=('arial',15),text=f_contents63,bg="white",bd=0).place(x=300,y=585); Label(t1,font=('arial',15),text=f_contents64,bg="white",bd=0).place(x=970,y=35); Label(t1,font=('arial',15),text=f_contents65,bg="white",bd=0).place(x=970,y=85); Label(t1,font=('arial',15),text=f_contents66,bg="white",bd=0).place(x=970,y=135); Label(t1,font=('arial',15),text=f_contents67,bg="white",bd=0).place(x=970,y=185); Label(t1,font=('arial',15),text=f_contents68,bg="white",bd=0).place(x=970,y=235); Label(t1,font=('arial',15),text=f_contents69,bg="white",bd=0).place(x=970,y=285); Label(t1,font=('arial',15),text=f_contents70,bg="white",bd=0).place(x=970,y=335); Label(t1,font=('arial',15),text=f_contents71,bg="white",bd=0).place(x=970,y=385)
        menu_bar = Menu(t1)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Week 1", command=overzicht)
        file_menu.add_command(label="Week 2", command=overzichtweek2)
        file_menu.add_command(label="End!", command=t1.destroy)
        menu_bar.add_cascade(label="File", menu=file_menu)
        t1.config(menu=menu_bar)
        #----------de labels met dagen erin--------#
        Label(t1,font=('arial',20),text="Maandag",bg="white",bd=0).place(x=80,y=35); Label(t1,font=('arial',20),text="Dinsdag",bg="white",bd=0).place(x=80,y=235); Label(t1,font=('arial',20),text="Woensdag",bg="white",bd=0).place(x=80,y=435); Label(t1,font=('arial',20),text="Donderdag",bg="white",bd=0).place(x=750,y=35); Label(t1,font=('arial',20),text="Vrijdag",bg="white",bd=0).place(x=750,y=235)
        #----------de labels met het huiswekr erin--------#
        Label(t1,font=('arial',15),text=f_contents21,bg="white",bd=0).place(x=300,y=35); Label(t1,font=('arial',15),text=f_contents22,bg="white",bd=0).place(x=300,y=85); Label(t1,font=('arial',15),text=f_contents23,bg="white",bd=0).place(x=300,y=135); Label(t1,font=('arial',15),text=f_contents24,bg="white",bd=0).place(x=300,y=185); Label(t1,font=('arial',15),text=f_contents25,bg="white",bd=0).place(x=300,y=235); Label(t1,font=('arial',15),text=f_contents26,bg="white",bd=0).place(x=300,y=285); Label(t1,font=('arial',15),text=f_contents27,bg="white",bd=0).place(x=300,y=335); Label(t1,font=('arial',15),text=f_contents28,bg="white",bd=0).place(x=300,y=385); Label(t1,font=('arial',15),text=f_contents29,bg="white",bd=0).place(x=300,y=435); Label(t1,font=('arial',15),text=f_contents30,bg="white",bd=0).place(x=300,y=485); Label(t1,font=('arial',15),text=f_contents31,bg="white",bd=0).place(x=300,y=535); Label(t1,font=('arial',15),text=f_contents32,bg="white",bd=0).place(x=300,y=585); Label(t1,font=('arial',15),text=f_contents33,bg="white",bd=0).place(x=970,y=35); Label(t1,font=('arial',15),text=f_contents34,bg="white",bd=0).place(x=970,y=85); Label(t1,font=('arial',15),text=f_contents35,bg="white",bd=0).place(x=970,y=135); Label(t1,font=('arial',15),text=f_contents36,bg="white",bd=0).place(x=970,y=185); Label(t1,font=('arial',15),text=f_contents37,bg="white",bd=0).place(x=970,y=235); Label(t1,font=('arial',15),text=f_contents38,bg="white",bd=0).place(x=970,y=285); Label(t1,font=('arial',15),text=f_contents39,bg="white",bd=0).place(x=970,y=335); Label(t1,font=('arial',15),text=f_contents40,bg="white",bd=0).place(x=970,y=385)
        #----------de groene lijnen eromheen--------#
        Canvas(t1,bg=safecolor,bd=0,height=1,width=500).place(x=50,y=26); Canvas(t1,bg=safecolor,bd=0,height=1,width=500).place(x=50,y=30); Canvas(t1,bg=safecolor,bd=0,height=1,width=500).place(x=50,y=626); Canvas(t1,bg=safecolor,bd=0,height=1,width=500).place(x=50,y=630); Canvas(t1,bg=safecolor,bd=0,height=604,width=2).place(x=46,y=26); Canvas(t1,bg=safecolor,bd=0,height=604,width=2).place(x=50,y=26); Canvas(t1,bg=safecolor,bd=0,height=604,width=2).place(x=546,y=26); Canvas(t1,bg=safecolor,bd=0,height=604,width=2).place(x=550,y=26); Canvas(t1,bg=safecolor,bd=0,height=1,width=500).place(x=720,y=26); Canvas(t1,bg=safecolor,bd=0,height=1,width=500).place(x=720,y=30); Canvas(t1,bg=safecolor,bd=0,height=1,width=500).place(x=720,y=626); Canvas(t1,bg=safecolor,bd=0,height=1,width=500).place(x=720,y=630); Canvas(t1,bg=safecolor,bd=0,height=604,width=2).place(x=716,y=26); Canvas(t1,bg=safecolor,bd=0,height=604,width=2).place(x=720,y=26); Canvas(t1,bg=safecolor,bd=0,height=604,width=2).place(x=1216,y=26); Canvas(t1,bg=safecolor,bd=0,height=604,width=2).place(x=1220,y=26)
        t1.mainloop()
    def sidemenu():
        Canvas(LG,width=200,height=750,bg="black",bd=0).place(x=-4,y=0)
        Button(LG, image=img3 ,bd=0,bg="white",command=knorth).place(x=203,y=3)
        HoverButton(LG,width=16,height=2,fg="white",font=('arial',15,'bold'),text="komende weken",bd=0,activebackground='gray15',bg="black",command=komendeweken).place(x=0,y=0)
        HoverButton(LG,width=16,height=2,fg="white",font=('arial',15,'bold'),text="overzicht",bd=0,activebackground='gray15',bg="black",command=overzicht).place(x=0,y=50)
        
        sluiten()
        
    Button(LG, image=img3 ,bd=0,bg="white",command=sidemenu).place(x=3,y=3);sluiten()
    Button(LG, image=img7 ,bd=0,bg="white",command=waarschuwing).place(x=10,y=670)
def algemeen():
    pass
def baas():
    pass
def personeel():
    pass
if loginofniet11 == "Nooit":
    homepage()
else:
    frame1 = Canvas( LG, bg ="white", height=4830, width=1810,bd=0)
    image1 = PhotoImage(file="beginschermfoto3.png")
    image = frame1.create_image( 1000, 0, anchor = NE,image=image1)
    var = IntVar()
    frame1.place(x=500,y=-3)
    
    frame2 = Canvas( LG, bg ="white", height=130, width=284,bd=0)
    image2 = PhotoImage(file="logo1.png")
    image = frame2.create_image(284,0,anchor=NE,image=image2)
    frame2.place(x=20,y=30)

    frame3 = Canvas( LG, bg ="white", height=30, width=30,bd=0)
    image3 = PhotoImage(file="terug1.png")
    image = frame3.create_image(40,0,anchor=NE,image=image3)
    frame3.place(x=50,y=679)

    Button(LG,text='Forgot your password?',width=20,bd=0,height=1,font=('arial', 13),bg="white",fg="blue",command=forgotLG).place(x=140,y=600)
    Button(LG,text='Exit',width=7,bd=0,height=1,font=('arial', 8),bg="white",command=LG.destroy).place(x=85,y=683)

    Label(LG,text='Username:',bd=0,font=('arial', 10),bg="white").place(x=70,y=270)
    Label(LG,text='Password:',bd=0,font=('arial', 10),bg="white").place(x=70,y=370)
    L3=Label(LG,bd=0,bg="white",height=12,width=3).place(x=19,y=30)
    L4=Label(LG,bd=0,bg="white",height=12,width=3).place(x=303,y=30)
    L5=Label(LG,bd=0,bg="white",height=3,width=41).place(x=19,y=30)
    L6=Label(LG,bd=0,bg="white",height=3,width=41).place(x=19,y=160)
    L7=Label(LG,text='Good afternoon,',bd=0,font=('arial', 15, 'bold'),bg="white").place(x=70,y=180)
    L8=Label(LG,text='welcome back!',bd=0,font=('arial', 14),bg="white").place(x=230,y=181)
    L9=Label(LG,text='Feel free to login anytime.',bd=0,font=('arial', 11),bg="white").place(x=70,y=210)
    L10=Label(LG,bg="white",height=20,width=1).place(x=41,y=680)
    L11=Label(LG,bg="white",height=20,width=1).place(x=78,y=680)
    L12=Label(LG,bg="white",height=1,width=10).place(x=41,y=665)
    Checkbutton(LG,text="remember me",bg="white",variable=var3,onvalue=1,offvalue=0).place(x=70,y=470)
    t1=Entry(LG,show='*',textvariable=value1,bd=2,font=medium_font,relief="groove").place(x=70,y=400)
    if counter1 == '1':
        gebruiker1 = open("gebruiker1.txt", "r").readlines()[0]
        with open('wachtwoord1.txt', 'r') as f: wachtwoord1 = f.read()
        Button(LG,text='login',bd=0,fg="white",font=('arial', 20), width= 20, height=1, command= Gebruikersnaam1,bg=safecolor,relief="ridge").place(x=70,y=540)
        box=ttk.Combobox(LG,textvariable=value3,font=medium_font,state='readonly'); box['values']=(gebruiker1); remembertest=box.current(0)
        box.place(x=70,y=300)
    if counter1 == '2':
        gebruiker1 = open("gebruiker1.txt", "r").readlines()[0]
        gebruiker2 = open("gebruiker1.txt", "r").readlines()[1]
        with open('wachtwoord1.txt', 'r') as f: wachtwoord1 = f.read()
        with open('wachtwoord2.txt', 'r') as f: wachtwoord2 = f.read()
        Button(LG,text='login',bd=0,fg="white",font=('arial', 20), width= 20, height=1, command= Gebruikers2,bg=safecolor,relief="ridge").place(x=70,y=540)
        box=ttk.Combobox(LG,textvariable=value3,font=medium_font,state='readonly'); box['values']=(gebruiker1,gebruiker2); remembertest=box.current(0)
        box.place(x=70,y=300)
    if counter1 == '3':
        gebruiker1 = open("gebruiker1.txt", "r").readlines()[0]
        gebruiker2 = open("gebruiker1.txt", "r").readlines()[1]
        gebruiker3 = open("gebruiker1.txt", "r").readlines()[2]
        with open('wachtwoord1.txt', 'r') as f: wachtwoord1 = f.read()
        with open('wachtwoord2.txt', 'r') as f: wachtwoord2 = f.read()
        with open('wachtwoord3.txt', 'r') as f: wachtwoord3 = f.read()
        Button(LG,text='login',bd=0,fg="white",font=('arial', 20), width= 20, height=1, command= Gebruikers3,bg=safecolor,relief="ridge").place(x=70,y=540)
        box=ttk.Combobox(LG,textvariable=value3,font=medium_font,state='readonly'); box['values']=(gebruiker1,gebruiker2,gebruiker3); remembertest=box.current(0)
        box.place(x=70,y=300)
    if counter1 == '4':
        gebruiker1 = open("gebruiker1.txt", "r").readlines()[0]
        gebruiker2 = open("gebruiker1.txt", "r").readlines()[1]
        gebruiker3 = open("gebruiker1.txt", "r").readlines()[2]
        gebruiker4 = open("gebruiker1.txt", "r").readlines()[3]
        with open('wachtwoord1.txt', 'r') as f: wachtwoord1 = f.read()
        with open('wachtwoord2.txt', 'r') as f: wachtwoord2 = f.read()
        with open('wachtwoord3.txt', 'r') as f: wachtwoord3 = f.read()
        with open('wachtwoord4.txt', 'r') as f: wachtwoord4 = f.read()
        Button(LG,text='login',bd=0,fg="white",font=('arial', 20), width= 20, height=1, command= Gebruikers4,bg=safecolor,relief="ridge").place(x=70,y=540)
        box=ttk.Combobox(LG,textvariable=value3,font=medium_font,state='readonly'); box['values']=(gebruiker1,gebruiker2,gebruiker3,gebruiker4); remembertest=box.current(0)
        box.place(x=70,y=300)
    if counter1 == '5':
        gebruiker1 = open("gebruiker1.txt", "r").readlines()[0]
        gebruiker2 = open("gebruiker1.txt", "r").readlines()[1]
        gebruiker3 = open("gebruiker1.txt", "r").readlines()[2]
        gebruiker4 = open("gebruiker1.txt", "r").readlines()[3]
        gebruiker5 = open("gebruiker1.txt", "r").readlines()[4]
        with open('wachtwoord1.txt', 'r') as f: wachtwoord1 = f.read()
        with open('wachtwoord2.txt', 'r') as f: wachtwoord2 = f.read()
        with open('wachtwoord3.txt', 'r') as f: wachtwoord3 = f.read()
        with open('wachtwoord4.txt', 'r') as f: wachtwoord4 = f.read()
        with open('wachtwoord5.txt', 'r') as f: wachtwoord5 = f.read()
        Button(LG,text='login',bd=0,fg="white",font=('arial', 20), width= 20, height=1, command= Gebruikers5,bg=safecolor,relief="ridge").place(x=70,y=540)
        box=ttk.Combobox(LG,textvariable=value3,font=medium_font,state='readonly'); box['values']=(gebruiker1,gebruiker2,gebruiker3,gebruiker4,gebruiker5); box.current(0)
        box.place(x=70,y=300)
    def sluiten1(): LG.destroy()
LG.mainloop()
