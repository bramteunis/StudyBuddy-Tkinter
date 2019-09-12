##from win32api import GetSystemMetrics
##
##width = GetSystemMetrics(0)
##height = GetSystemMetrics(1)
##width1 = str(width)
##height1 = str(height)
##r1 = open("lastwidth.txt", "r").readlines()[0]; lastwidth=r1.strip()
##r2 = open("lastwidth.txt", "r").readlines()[1]; lastheight=r2.strip()
##test = "yellow"
##if width1 != lastwidth or height1 != lastheight:
##    from PIL import Image
##    def resize(imgname):
##        img = Image.open(str(imgname)+'.png')
##        wpercent = (basewidth/float(img.size[0]))
##        hsize = int((float(img.size[1])*float(wpercent)))
##        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
##        img.save(str(imgname)+'.png')
##    basewidth = width; imgname="bergen";resize()
##    w20 = (width / 64); basewidth=round(w20);resize("quit")
##    w20 = (width / 64); basewidth=round(w20);resize("minimalize")
##    w20 = (width / 64); basewidth=round(w20);resize("weekvooruit")
##    w30 = (width / 42.6); basewidth=round(w30);resize("menu")
##    w900 = (width / 1.2673); basewidth=round(w900);resize("beginschermfoto3")
##    w285 = (width / 4.4912); basewidth=round(w285);resize("logo1")
##    w40 = (width / 32); basewidth=round(w40);resize("terug1")
##

    
from tkinter import *
import tkinter as tk
import time, re, webbrowser, zipfile, shutil, os, win32api
from tkinter import Tk, PhotoImage, messagebox, ttk, colorchooser
import urllib.request as urllib2
from pathlib import Path
needed="1"
access1 = float
access1 = (0)

username = os.getlogin()

LG = tk.Tk();LG.configure(background="white");LG.title("Schoolsysteem");LG.resizable(False, False)
localtime=time.asctime(time.localtime(time.time()))
width = LG.winfo_screenwidth()
height = LG.winfo_screenheight()

w1 = (width / 1280); width1=round(w1)
w2 = (width / 640); width2=round(w2)
w3 = (width / 426.67); width3=round(w3)
w5 = (width / 256); width5=round(w5)
w8 = (width / 160); width8=round(w8)
w9 = (width / 142.2); width9=round(w9)
w10 = (width / 128); width10=round(w10)
w11 = (width / 116.363); width11=round(w11)
w12 = (width / 106.6); width12=round(w12)
w14 = (width / 91.4285); width14=round(w14)
w15 = (width / 85.3); width15=round(w15)
w16 = (width / 80); width16=round(w16)
w19 = (width / 67.36); width19=round(w19)
w20 = (width / 64); width20=round(w20)
w25 = (width / 51.2); width25=round(w25)
w30 = (width / 42.6); width30=round(w30)
w40 = (width / 32); width40=round(w40)
w43 = (width / 29.53); width43=round(w43)
w48 = (width / 26.66); width48=round(w48)
w50 = (width / 25.6); width50=round(w50)
w55 = (width / 23.27); width55=round(w55)
w60 = (width / 21.33); width60=round(w60)
w70 = (width / 18.2857); width70=round(w70)
w85 = (width / 15.0588); width85=round(w85)
w90 = (width / 14.22); width90=round(w90)
w98 = (width / 13.0612); width98=round(w98)
w100 = (width / 12.8); width100=round(w100)
w102 = (width / 12.549); width102=round(w102)
w110 = (width / 11.63); width110=round(w110)
w120 = (width / 10.66); width120=round(w120)
w130 = (width / 9.846); width130=round(w130)
w135 = (width / 9.4814); width135=round(w135)
w139 = (width / 9.2086); width139=round(w139)
w140 = (width / 9.1428); width140=round(w140)
w145 = (width / 8.83); width145=round(w145)
w150 = (width / 8.53); width150=round(w150)
w155 = (width / 8.258); width155=round(w155)
w160 = (width / 8); width160=round(w160)
w164 = (width / 7.804878); width164=round(w164)
w170 = (width / 7.5294); width170=round(w170)
w175 = (width / 7.3142); width175=round(w175)
w180 = (width / 7.11); width180=round(w180)
w200 = (width / 6.4); width200=round(w200)
w205 = (width / 6.24); width205=round(w205)
w210 = (width / 6.0952); width210=round(w210)
w220 = (width / 5.8181); width220=round(w220)
w225 = (width / 5.68); width225=round(w225)
w230 = (width / 5.5652); width230=round(w230)
w240 = (width / 5.33); width240=round(w240)
w250 = (width / 5.12); width250=round(w250)
w255 = (width / 5.02); width255=round(w255)
w270 = (width / 4.7407); width270=round(w270)
w275 = (width / 4.654); width275=round(w275)
w280 = (width / 4.571); width280=round(w280)
w285 = (width / 4.4912); width285=round(w285)
w290 = (width / 4.42); width290=round(w290)
w300 = (width / 4.266); width300=round(w300)
w305 = (width / 4.197); width305=round(w305)
w308 = (width / 4.1558); width308=round(w308)
w310 = (width / 4.12903); width310=round(w310)
w312 = (width / 4.10256); width312=round(w312)
w320 = (width / 4); width320=round(w320)
w325 = (width / 3.938); width325=round(w325)
w340 = (width / 3.765); width340=round(w340)
w350 = (width / 3.66); width350=round(w350)
w355 = (width / 3.60563); width355=round(w355)
w360 = (width / 3.5555); width360=round(w360)
w370 = (width / 3.45946); width370=round(w370)
w375 = (width / 3.41); width375=round(w375)
w380 = (width / 3.37); width380=round(w380)
w385 = (width / 3.3247); width385=round(w385)
w390 = (width / 3.28); width390=round(w390)
w400 = (width / 3.2); width400=round(w400)
w405 = (width / 3.1605); width405=round(w405)
w416 = (width / 3.0769); width416=round(w416)
w420 = (width / 3.047); width420=round(w420)
w425 = (width / 3.011); width425=round(w425)
w440 = (width / 2.9091); width440=round(w440)
w450 = (width / 2.84); width450=round(w450)
w455 = (width / 2.8132); width455=round(w455)
w470 = (width / 2.7234); width470=round(w470)
w475 = (width / 2.694); width475=round(w475)
w490 = (width / 2.61225); width490=round(w490)
w500 = (width / 2.56); width500=round(w500)
w505 = (width / 2.5346); width505=round(w505)
w518 = (width / 2.471); width518=round(w518)
w520 = (width / 2.4615); width520=round(w520)
w522 = (width / 2.4521); width522=round(w522)
w525 = (width / 2.438); width525=round(w525)
w530 = (width / 2.415094); width530=round(w530)
w540 = (width / 2.3704); width540=round(w540)
w550 = (width / 2.33); width550=round(w550)
w555 = (width / 2.3063); width555=round(w555)
w560 = (width / 2.2857); width560=round(w560)
w565 = (width / 2.2655); width565=round(w565)
w570 = (width / 2.2456); width570=round(w570)
w575 = (width / 2.226); width575=round(w575)
w600 = (width / 2.13); width600=round(w600)
w605 = (width / 2.1157); width605=round(w605)
w625 = (width / 2.048); width625=round(w625)
w640 = (width / 2); width640=round(w640)
w650 = (width / 1.9692); width650=round(w650)
w655 = (width / 1.9541); width655=round(w655)
w660 = (width / 1.9394); width660=round(w660)
w685 = (width / 1.8686); width685=round(w685)
w690 = (width / 1.85507); width690=round(w690)
w700 = (width / 1.8285); width700=round(w700)
w728 = (width / 1.7582); width728=round(w728)
w730 = (width / 1.7534); width730=round(w730)
w732 = (width / 1.74863); width732=round(w732)
w740 = (width / 1.7297); width740=round(w740)
w745 = (width / 1.71812); width745=round(w745)
w750 = (width / 1.7067); width750=round(w750)
w770 = (width / 1.66233); width770=round(w770)
w780 = (width / 1.64103); width780=round(w780)
w830 = (width / 1.5422); width830=round(w830)
w840 = (width / 1.52381); width840=round(w840)
w870 = (width / 1.47126); width870=round(w870)
w900 = (width / 1.42222); width900=round(w900)
w910 = (width / 1.40659); width910=round(w910)
w920 = (width / 1.3913); width920=round(w920)
w930 = (width / 1.3763); width930=round(w930)
w938 = (width / 1.3646); width938=round(w938)
w940 = (width / 1.3617); width940=round(w940)
w942 = (width / 1.3588); width942=round(w942)
w950 = (width / 1.34737); width950=round(w950)
w980 = (width / 1.306123); width980=round(w980)
w990 = (width / 1.2929); width990=round(w990)
w1010 = (width / 1.2673); width1010=round(w1010)
w1050 = (width / 1.21905); width1050=round(w1050)
w1080 = (width / 1.18518); width1080=round(w1080)
w1100 = (width / 1.1636); width1100=round(w1100)
w1110 = (width / 1.1531); width1110=round(w1110)
w1120 = (width / 1.14286); width1120=round(w1120)
w1148 = (width / 1.11498); width1148=round(w1148)
w1152 = (width / 1.1111); width1152=round(w1152)
w1190 = (width / 1.0756); width1190=round(w1190)
w1210 = (width / 1.0578); width1210=round(w1210)
w1240 = (width / 1.0322); width1240=round(w1240)


medium_font= ('Verdana',width20); small_font= ('Verdana',10)
if height >= 721:
    #LG.geometry("1280x720")
    LG.attributes('-fullscreen',True)
if width >= 1281:
    #LG.geometry("1280x720")
    LG.attributes('-fullscreen',True)
else: LG.attributes('-fullscreen',True)
value1 = StringVar(); value2 = StringVar(); value3 = StringVar(); var3=StringVar()
kleur1string = StringVar()
wachtwoord1=StringVar()
wachtwoord2=StringVar();gebruiker10=StringVar();wachtwoordherstel=StringVar();data=StringVar()
loginofniet10=StringVar()
boolean=StringVar()
inlog=StringVar()
img1 = PhotoImage(file="quit.png")
img2 = PhotoImage(file="minimalize.png")
img3 = PhotoImage(file="menu.png")
img4 = PhotoImage(file="bergen.png")
img7 = PhotoImage(file="weekvooruit.png")
img8 = PhotoImage(file="start.png")
img9 = PhotoImage(file="stop.png")
img10 = PhotoImage(file="info1.png")
img11 = PhotoImage(file="beginschermfoto3 - kopie (3).png")
img12 = PhotoImage(file="logo1.png")
img13 = PhotoImage(file="terug1.png")
#LG.iconbitmap(default='icon.ico')
with open('safecolor.txt', 'r') as f: safecolor = f.read()#; safecolor = safecolor12[32:39]
with open('loginofniet.txt', 'r') as f: loginofniet11 = f.read()
with open('rechten.txt', 'r') as f: rechten = f.read()
with open('gebruiker1.txt', 'r') as file: data = file.readlines()
c1 = open("gebruiker1.txt", "r").readlines()[10]; counter1=c1.strip()
if counter1 == '1': gebruikersnaamup = '2'
if counter1 == '2': gebruikersnaamup = '3'
if counter1 == '3': gebruikersnaamup = '4'
if counter1 == '4': gebruikersnaamup = '5'
if counter1 == '5': pass
r2 = open("rechten2.txt", "r").readlines()[0]; rechten2=r2.strip()
r3 = open("rechten2.txt", "r").readlines()[1]; rechten3=r3.strip()
r4 = open("rechten2.txt", "r").readlines()[2]; rechten4=r4.strip()
r5 = open("rechten2.txt", "r").readlines()[3]; rechten5=r5.strip()
r6 = open("rechten2.txt", "r").readlines()[4]; rechten6=r6.strip()

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

def Gebruikersnaam1():
    if value3.get() == gebruiker1 and value1.get() == wachtwoord1 :
        homepage(); inlog.set("1")
        TF = open('rechten.txt', 'w'); TF.write(rechten2); TF.close()
        a4 = open("gebruiker1.txt", "r").readlines()[16]; aantal4=a4.strip()
        cf1=int(aantal4)+(1)
        replace_line("gebruiker1.txt",16,str(cf1)+"\n")
        #data[16] = aantal4 + '1'+'\n'
        #with open('gebruiker1.txt', 'w') as file: file.writelines( data )
        replace_line("gebruiker1.txt",21,"1\n")
        #data[21] = '1' + '\n'
        #with open('gebruiker1.txt', 'w') as file: file.writelines( data )
def Gebruikersnaam2():
    if value3.get() == gebruiker2 and value1.get() == wachtwoord2 :
        homepage(); inlog="2"
        GU = "2"; TF = open('rechten.txt', 'w'); TF.write(GU); TF.close()
        data[21] = '2' + '\n'
        with open('gebruiker1.txt', 'w') as file: file.writelines( data )
def Gebruikersnaam3():
    if value3.get() == gebruiker3 and value1.get() == wachtwoord3 :
        homepage(); inlog="3"
        GU = "3"; TF = open('rechten.txt', 'w'); TF.write(GU); TF.close()
        data[21] = '3' + '\n'
        with open('gebruiker1.txt', 'w') as file: file.writelines( data )
def Gebruikersnaam4():
    if value3.get() == gebruiker4 and value1.get() == wachtwoord4 :
        homepage(); inlog="4"
        GU = "4"; TF = open('rechten.txt', 'w'); TF.write(GU); TF.close()
        data[21] = '4' + '\n'
        with open('gebruiker1.txt', 'w') as file: file.writelines( data )
def Gebruikersnaam5():
    if value3.get() == gebruiker5 and value1.get() == wachtwoord5 :
        homepage(); inlog="5"
        GU = "5"; TF = open('rechten.txt', 'w'); TF.write(GU); TF.close()
        data[21] = '5' + '\n'
        with open('gebruiker1.txt', 'w') as file: file.writelines( data )
def Gebruikers2(): Gebruikersnaam1(); Gebruikersnaam2();
def Gebruikers3(): Gebruikersnaam1(); Gebruikersnaam2(); Gebruikersnaam3()
def Gebruikers4(): Gebruikersnaam1(); Gebruikersnaam2(); Gebruikersnaam3(); Gebruikersnaam4()
def Gebruikers5(): Gebruikersnaam1(); Gebruikersnaam2(); Gebruikersnaam3(); Gebruikersnaam4(); Gebruikersnaam5()


def sluiten(): HoverButton(LG, image=img1,bg="white",bd=0,command=LG.destroy).place(x=width1240,y=width5); HoverButton(LG, image=img2,bg="white",bd=0,command=homepage).place(x=width1210,y=width5)
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

def homepage():
    LG.attributes('-fullscreen',True)
    with open('safecolor.txt', 'r') as f: safecolor = f.read()#; safecolor = safecolor12[32:39]
    Label(LG,image=img4).place(x=-2,y=-1)
    if width >= 1200 and width <= 1800:
        b1 = Button(LG, text='Start',        padx=2, pady=0, bd=0, fg="black",font=('arial', width10), width= width12, height=2,bg=safecolor).grid(row=0,column=1)
        b2 = Button(LG, text='Gebruikers',   padx=2, pady=0, bd=0, fg="black",font=('arial', width10), width= width12, height=2,bg=safecolor,command=gebruikers).grid(row=0,column=2)
        b3 = Button(LG,                      padx=2, pady=0, bd=0, fg="black",font=('arial', width10), width= width48, height=2,bg=safecolor).grid(row=0,column=3)
        b4 = Button(LG, text='Rooster',       padx=2, pady=0, bd=0, fg="black",font=('arial', width10), width= width12, height=2,command=knorth,bg=safecolor).grid(row=0,column=4)
        b5 = Button(LG, text='Agenda',       padx=2, pady=0, bd=0, fg="black",font=('arial', width10), width= width12, height=2,bg=safecolor,command=agenda).grid(row=0,column=5)
        b6 = Button(LG, text='Kalender',     padx=2, pady=0, bd=0, fg="black",font=('arial', width10), width= width12, height=2,bg=safecolor).grid(row=0,column=6)
        b7 = Button(LG, text='instellingen', padx=2, pady=0, bd=0, fg="black",font=('arial', width10), width= width12, height=2,command=instellingen,bg=safecolor).grid(row=0,column=7)
        b8 = Button(LG, text='Exit',         padx=2, pady=0, bd=0, fg="black",font=('arial', width10), width= width12, height=2,command=LG.destroy,bg=safecolor).grid(row=0,column=8)
        b9 = Button(LG,                      padx=-2, pady=0, bd=0, fg="black",font=('arial', width10), width= width20, height=2,bg=safecolor).grid(row=0,column=9)
        b10 = Label(LG, text=localtime,      padx=0, pady=0, bd=0, fg="black",font=('arial', width10), width= width20, height=2,bg=safecolor).grid(row=0,column=9)
    if width >=1800 and width <= 2000:
        b1 = Button(LG, text='Start',        padx=2, pady=0, bd=0, fg="black",font=('arial', width10), width= width9, height=2,bg=safecolor).grid(row=0,column=1)
        b2 = Button(LG, text='Gebruikers',   padx=2, pady=0, bd=0, fg="black",font=('arial', width10), width= width9, height=2,bg=safecolor,command=gebruikers).grid(row=0,column=2)
        b3 = Button(LG,                      padx=2, pady=0, bd=0, fg="black",font=('arial', width10), width= width25, height=2,bg=safecolor).grid(row=0,column=3)
        b4 = Button(LG, text='Rooster',       padx=2, pady=0, bd=0, fg="black",font=('arial', width10), width= width9, height=2,command=knorth,bg=safecolor).grid(row=0,column=4)
        b5 = Button(LG, text='Agenda',       padx=2, pady=0, bd=0, fg="black",font=('arial', width10), width= width9, height=2,bg=safecolor,command=agenda).grid(row=0,column=5)
        b6 = Button(LG, text='Kalender',     padx=2, pady=0, bd=0, fg="black",font=('arial', width10), width= width9, height=2,bg=safecolor).grid(row=0,column=6)
        b7 = Button(LG, text='instellingen', padx=2, pady=0, bd=0, fg="black",font=('arial', width10), width= width9, height=2,command=instellingen,bg=safecolor).grid(row=0,column=7)
        b8 = Button(LG, text='Exit',         padx=2, pady=0, bd=0, fg="black",font=('arial', width10), width= width9, height=2,command=LG.destroy,bg=safecolor).grid(row=0,column=8)
        b9 = Button(LG,                      padx=-2, pady=0, bd=0, fg="black",font=('arial', width10), width= width19, height=2,bg=safecolor).grid(row=0,column=9)
        b10 = Label(LG, text=localtime,      padx=0, pady=0, bd=0, fg="black",font=('arial', width10), width= width19, height=2,bg=safecolor).grid(row=0,column=9)
        b3 = Button(LG,                      padx=-2, pady=0, bd=0, fg="black",font=('arial', width10), width= width30, height=2,bg=safecolor).grid(row=0,column=10)
class hoverFrame(tk.Frame):
    def __init__(self, master, **kw):
        tk.Frame.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
    def on_enter(self, e):
        self['background'] = self['activebackground']
    def on_leave(self, e):
        self['background'] = self.defaultBackground
class agenda():
    def __init__(self):
        LG.attributes('-fullscreen',True)
        c = Canvas(LG,width=width,height=height,bg="white", highlightthickness=0);c.place(x=0,y=0)
        HoverButton(LG, image=img1,bg="white",bd=0,command=LG.destroy).place(x=width1240,y=width5); HoverButton(LG, image=img2,bg="white",bd=0,command=homepage).place(x=width1210,y=width5)
        def frames1():
            Frame(LG,bg=safecolor,width=width3,height=width500).place(x=var4,y=width150)
        var4=(width20);frames1();var4=(width200);frames1();var4=(width380);frames1();var4=(width560);frames1();var4=(width740);frames1();var4=(width920);frames1();var4=(width1100);frames1()
        Frame(LG,bg=safecolor,width=width,height=width3).place(x=0,y=width145)
        Frame(LG,bg=safecolor,width=width,height=width3).place(x=0,y=width150)
        Frame(LG,bg=safecolor,width=width,height=width3).place(x=0,y=width650)
        Frame(LG,bg=safecolor,width=width,height=width3).place(x=0,y=width655)
        datum1=int 
        datum1=(20)
        datum7="26"
        jaar1="2019"
        for char in '-.,\n': Text=localtime.replace(char,' ')
        Text=Text.lower();word_list=Text.split();maand=word_list[1];jaar=word_list[4];dag=word_list[0];datum=word_list[2]
        if maand=="may":maand="Mei"
        if maand=="june":maand="Juni"
        if maand=="jul":maand="Juli"
        if dag=="mon":color1="gray80"
        else:color1="white"
        if dag=="tue":color2="gray80"
        else:color2="white"
        if dag=="wed":color3="gray80"
        else:color3="white"
        if dag=="thu":color4="gray80"
        else:color4="white"
        if dag=="fri":color5="gray80"
        else:color5="white"
        if dag=="sat":color6="gray80"
        else:color6="white"
        if dag=="sun" and jaar==jaar1 and datum==datum7:color7="gray80"
        else:color7="white"
        Frame(LG,width=width180,height=width55,bg=color1).place(x=width20,y=width90);Label(LG,text="Maandag",font=('arial',width15,'bold'),bg=color1).place(x=width30,y=width100)
        Frame(LG,width=width180,height=width55,bg=color2).place(x=width200,y=width90);Label(LG,text="Dinsdag",font=('arial',width15,'bold'),bg=color2).place(x=width210,y=width100)
        Frame(LG,width=width180,height=width55,bg=color3).place(x=width380,y=width90);Label(LG,text="Woensdag",font=('arial',width15,'bold'),bg=color3).place(x=width390,y=width100)
        Frame(LG,width=width180,height=width55,bg=color4).place(x=width560,y=width90);Label(LG,text="Donderdag",font=('arial',width15,'bold'),bg=color4).place(x=width570,y=width100)
        Frame(LG,width=width180,height=width55,bg=color5).place(x=width740,y=width90);Label(LG,text="Vrijdag",font=('arial',width15,'bold'),bg=color5).place(x=width750,y=width100)
        Frame(LG,width=width180,height=width55,bg=color6).place(x=width920,y=width90);Label(LG,text="Zaterdag",font=('arial',width15,'bold'),bg=color6).place(x=width930,y=width100)
        Frame(LG,width=width180,height=width55,bg=color7).place(x=width1100,y=width90);Label(LG,text="Zondag",font=('arial',width15,'bold'),bg=color7).place(x=width1110,y=width100)
        Label(LG,text=maand + jaar1,font=('arial',width20,'bold'),bg="white").place(x=width100,y=width20)
        h1 = open("gebruiker1.txt", "r").readlines()[77]; huiswerk1=h1.strip()
        h2 = open("gebruiker1.txt", "r").readlines()[78]; huiswerk2=h2.strip()
        h3 = open("gebruiker1.txt", "r").readlines()[79]; huiswerk3=h3.strip()
        h4 = open("gebruiker1.txt", "r").readlines()[80]; huiswerk4=h4.strip()
        h5 = open("gebruiker1.txt", "r").readlines()[86]; huiswerk5=h5.strip()
        h6 = open("gebruiker1.txt", "r").readlines()[87]; huiswerk6=h6.strip()
        h7 = open("gebruiker1.txt", "r").readlines()[88]; huiswerk7=h7.strip()
        h8 = open("gebruiker1.txt", "r").readlines()[89]; huiswerk8=h8.strip()
        h9 = open("gebruiker1.txt", "r").readlines()[95]; huiswerk9=h9.strip()
        h10 = open("gebruiker1.txt", "r").readlines()[96]; huiswerk10=h10.strip()
        h11 = open("gebruiker1.txt", "r").readlines()[97]; huiswerk11=h11.strip()
        h12 = open("gebruiker1.txt", "r").readlines()[98]; huiswerk12=h12.strip()
        h13 = open("gebruiker1.txt", "r").readlines()[104]; huiswerk13=h13.strip()
        h14 = open("gebruiker1.txt", "r").readlines()[105]; huiswerk14=h14.strip()
        h15 = open("gebruiker1.txt", "r").readlines()[106]; huiswerk15=h15.strip()
        h16 = open("gebruiker1.txt", "r").readlines()[107]; huiswerk16=h16.strip()
        h17 = open("gebruiker1.txt", "r").readlines()[113]; huiswerk17=h17.strip()
        h18 = open("gebruiker1.txt", "r").readlines()[114]; huiswerk18=h18.strip()
        h19 = open("gebruiker1.txt", "r").readlines()[115]; huiswerk19=h19.strip()
        h20 = open("gebruiker1.txt", "r").readlines()[116]; huiswerk20=h20.strip()
        def test(self):
                counterA=float;counterA=(0)
                tk=Tk();tk.geometry(str(width420)+"x"+str(width300));tk.title("Planning maken");tk.configure(background="white");tk.resizable(False, False)
                def r1(var1):replace_line('agendacounter5.txt', var1, '0\n')
                r1(0);r1(1);r1(2);r1(3)
                entryvar1=str
                aboutStud = Entry(tk,textvariable=entryvar1,font=('arial',width12),bg="gray80",bd=0)
                aboutStud.insert(END, "Eigen invoer")
                aboutStud.place(x=width220,y=width10)
                Frame(tk,bg=safecolor,width=width3,height=width300).place(x=width200,y=0)
                def c10():
                    def c2(line,line2,tedoen,locatie):
                        a4 = open('agendacounter5.txt', "r").readlines()[0]; line1=a4.strip()
                        a4 = open('agendacounter5.txt', "r").readlines()[1]; line2=a4.strip()
                        a4 = open('agendacounter5.txt', "r").readlines()[2]; line3=a4.strip()
                        a4 = open('agendacounter5.txt', "r").readlines()[3]; line4=a4.strip()
                        if line1 == "0" and line2 == "0" and line3 == "0" and line4 == "0":
                            a4 = open('agendacounter5.txt', "r").readlines()[line]; oneclick=a4.strip()
                            if oneclick == "1":replace_line('agendacounter5.txt', line, '0\n')
                            if oneclick == "0":replace_line('agendacounter5.txt', line, '1\n')
                            #replace_line('agendacounter1.txt', 0, str(huiswerk1) + '\n')
                            c3(line, tedoen, locatie)
                        else:pass
                    def c3(line,text,place):
                        a4 = open('agendacounter5.txt', "r").readlines()[line]; oneclick=a4.strip()
                        def d6(): c8(place,text,line)
                        def d7(): c7(place,text,line)
                        if oneclick == "1":Button(tk,text=text,font=('arial',width10),bd=0,bg="gray80",command=d7).grid(row=place,column=1)
                        if oneclick == "0":Button(tk,text=text,font=('arial',width10),bd=0,bg="white",command=d6).grid(row=place,column=1)
                    def c4():
                        a4 = open('agendacounter1.txt', "r").readlines()[2]; line3=a4.strip(); line1 = int(line3)
                        a4 = open('agendacounter1.txt', "r").readlines()[3]; line3=a4.strip(); line2 = int(line3)
                        a4 = open('agendacounter1.txt', "r").readlines()[4]; tedoen=a4.strip()
                        a4 = open('agendacounter1.txt', "r").readlines()[5]; locatie=a4.strip()
                        c2(line1,line2,tedoen,locatie)
                    def c5():
                        replace_line('agendacounter1.txt', 3, '1\n')
                        a4 = open('agendacounter1.txt', "r").readlines()[2]; line3=a4.strip(); line1 = int(line3)
                        a4 = open('agendacounter1.txt', "r").readlines()[3]; line3=a4.strip(); line2 = int(line3)
                        a4 = open('agendacounter1.txt', "r").readlines()[4]; tedoen=a4.strip()
                        a4 = open('agendacounter1.txt', "r").readlines()[5]; locatie=a4.strip()
                        c2(line1,line2,tedoen,locatie)
                    def c6():
                        replace_line('agendacounter1.txt', 3, '0\n')
                        a4 = open('agendacounter1.txt', "r").readlines()[2]; line3=a4.strip(); line1 = int(line3)
                        a4 = open('agendacounter1.txt', "r").readlines()[3]; line3=a4.strip(); line2 = int(line3)
                        a4 = open('agendacounter1.txt', "r").readlines()[4]; tedoen=a4.strip()
                        a4 = open('agendacounter1.txt', "r").readlines()[5]; locatie=a4.strip()
                        c2(line1,line2,tedoen,locatie)
                    def c7(place,text,line):
                        replace_line('agendacounter5.txt', line, '0\n')
                        Button(tk,text=text,font=('arial',width10),bd=0,bg="white",command=c6).grid(row=place,column=1)
                    def c8(place,text,line):
                        replace_line('agendacounter5.txt', line, '0\n')
                        Button(tk,text=text,font=('arial',width10),bd=0,bg="gray80",command=c6).grid(row=place,column=1)
                    c4()
                def f1(var1,var2,var3,var4,var5):
                    replace_line('agendacounter1.txt', 0, str(var1)+'\n')
                    a4 = open('agendacounter5.txt', "r").readlines()[0]; line1=a4.strip()
                    a4 = open('agendacounter5.txt', "r").readlines()[1]; line2=a4.strip()
                    a4 = open('agendacounter5.txt', "r").readlines()[2]; line3=a4.strip()
                    a4 = open('agendacounter5.txt', "r").readlines()[3]; line4=a4.strip()
                    if line1 == "0" and line2 == "0" and line3 == "0" and line4 == "0":
                        replace_line('agendacounter1.txt', 2, str(var2)+'\n')
                        replace_line('agendacounter1.txt', 3, str(var3)+'\n')
                        replace_line('agendacounter1.txt', 4, str(var4)+'\n')
                        replace_line('agendacounter1.txt', 5, str(var5)+'\n')
                        c10()
                    else: pass
                if huiswerk1 != "":
                    def s1(): f1('1','0','1',huiswerk1,counterB)
                    counterA = counterA + (1);counterB = counterA; Button(tk,text=huiswerk1,font=('arial',width10),bd=0,bg="white",command=s1).grid(row=counterA,column=1)
                if huiswerk2 != "":
                    def s2(): f1('2','1','0',huiswerk2,counterC)
                    counterA = counterA + (1);counterC = counterA; Button(tk,text=huiswerk2,font=('arial',width10),bd=0,bg="white",command=s2).grid(row=counterA,column=1)
                if huiswerk3 != "":
                    def s3(): f1('3','0','1',huiswerk3,counterD)
                    counterA = counterA + (1);counterD = counterA; Button(tk,text=huiswerk3,font=('arial',width10),bd=0,bg="white",command=s3).grid(row=counterA,column=1)
                if huiswerk4 != "":
                    def s4(): f1('4','0','1',huiswerk4,counterE)
                    counterA = counterA + (1);counterE = counterA; Button(tk,text=huiswerk4,font=('arial',width10),bd=0,bg="white",command=s4).grid(row=counterA,column=1)

                if huiswerk5 != "":
                    def s1(): f1('5','0','1',huiswerk5,counterF)
                    counterA = counterA + (1);counterF = counterA; Button(tk,text=huiswerk5,font=('arial',width10),bd=0,bg="white",command=s1).grid(row=counterA,column=1)
                if huiswerk6 != "":
                    def s2(): f1('6','1','0',huiswerk6,counterG)
                    counterA = counterA + (1);counterG = counterA; Button(tk,text=huiswerk6,font=('arial',width10),bd=0,bg="white",command=s2).grid(row=counterA,column=1)
                if huiswerk7 != "":
                    def s3(): f1('7','0','1',huiswerk7,counterH)
                    counterA = counterA + (1);counterH = counterA; Button(tk,text=huiswerk7,font=('arial',width10),bd=0,bg="white",command=s3).grid(row=counterA,column=1)
                if huiswerk8 != "":
                    def s4(): f1('8','0','1',huiswerk8,counterI)
                    counterA = counterA + (1);counterI = counterA; Button(tk,text=huiswerk8,font=('arial',width10),bd=0,bg="white",command=s4).grid(row=counterA,column=1)

                if huiswerk9 != "":
                    def s1(): f1('9','0','1',huiswerk9,counterJ)
                    counterA = counterA + (1);counterJ = counterA; Button(tk,text=huiswerk9,font=('arial',width10),bd=0,bg="white",command=s1).grid(row=counterA,column=1)
                if huiswerk10 != "":
                    def s2(): f1('10','1','0',huiswerk10,counterK)
                    counterA = counterA + (1);counterK = counterA; Button(tk,text=huiswerk10,font=('arial',width10),bd=0,bg="white",command=s2).grid(row=counterA,column=1)
                if huiswerk11 != "":
                    def s3(): f1('11','0','1',huiswerk11,counterL)
                    counterA = counterA + (1);counterL = counterA; Button(tk,text=huiswerk11,font=('arial',width10),bd=0,bg="white",command=s3).grid(row=counterA,column=1)
                if huiswerk12 != "":
                    def s4(): f1('12','0','1',huiswerk12,counterM)
                    counterA = counterA + (1);counterM = counterA; Button(tk,text=huiswerk12,font=('arial',width10),bd=0,bg="white",command=s4).grid(row=counterA,column=1)

                if huiswerk13 != "":
                    def s1(): f1('13','0','1',huiswerk13,counterN)
                    counterA = counterA + (1);counterN = counterA; Button(tk,text=huiswerk13,font=('arial',width10),bd=0,bg="white",command=s1).grid(row=counterA,column=1)
                if huiswerk14 != "":
                    def s2(): f1('14','1','0',huiswerk14,counterO)
                    counterA = counterA + (1);counterO = counterA; Button(tk,text=huiswerk14,font=('arial',width10),bd=0,bg="white",command=s2).grid(row=counterA,column=1)
                if huiswerk15 != "":
                    def s3(): f1('15','0','1',huiswerk15,counterP)
                    counterA = counterA + (1);counterP = counterA; Button(tk,text=huiswerk15,font=('arial',width10),bd=0,bg="white",command=s3).grid(row=counterA,column=1)
                if huiswerk16 != "":
                    def s4(): f1('16','0','1',huiswerk16,counterQ)
                    counterA = counterA + (1);counterQ = counterA; Button(tk,text=huiswerk16,font=('arial',width10),bd=0,bg="white",command=s4).grid(row=counterA,column=1)

                if huiswerk17 != "":
                    def s1(): f1('17','0','1',huiswerk17,counterR)
                    counterA = counterA + (1);counterR = counterA; Button(tk,text=huiswerk17,font=('arial',width10),bd=0,bg="white",command=s1).grid(row=counterA,column=1)
                if huiswerk18 != "":
                    def s2(): f1('18','1','0',huiswerk18,counterS)
                    counterA = counterA + (1);counterS = counterA; Button(tk,text=huiswerk18,font=('arial',width10),bd=0,bg="white",command=s2).grid(row=counterA,column=1)
                if huiswerk19 != "":
                    def s3(): f1('19','0','1',huiswerk19,counterT)
                    counterA = counterA + (1);counterT = counterA; Button(tk,text=huiswerk19,font=('arial',width10),bd=0,bg="white",command=s3).grid(row=counterA,column=1)
                if huiswerk20 != "":
                    def s4(): f1('20','0','1',huiswerk20,counterU)
                    counterA = counterA + (1);counterU = counterA; Button(tk,text=huiswerk20,font=('arial',width10),bd=0,bg="white",command=s4).grid(row=counterA,column=1)
                    
                def save():
                    w5 = open("agendacounter2.txt", "r").readlines()[1]; clickedx=w5.strip();w6 = open("agendacounter2.txt", "r").readlines()[2]; clickedy=w6.strip()
                    t1 = Canvas(LG,width=width170,height=width43,bg=safecolor,bd=0)
                    #t1.bind("<ButtonRelease-1>", lambda event: test())
                    t1.place(x=clickedx,y=clickedy)
                    w5 = open("agendacounter1.txt", "r").readlines()[0]; agendacounter=w5.strip()
                    def savestandard(var1):
                        w5 = open("agendacounter3.txt", "r").readlines()[0]; r1=w5.strip(); reader1 = int(r1)
                        w5 = open("agendacounter3.txt", "r").readlines()[1]; r2=w5.strip(); reader2 = int(r2)
                        w5 = open("agendacounter3.txt", "r").readlines()[2]; r3=w5.strip(); reader3 = int(r3)
                        
                        replace_line('agendacounter2.txt', reader1, str(clickedx)+'\n');replace_line('agendacounter2.txt', reader2, str(clickedy)+'\n');replace_line('agendacounter2.txt', reader3, str(var1)+'\n')

                        varA = int(reader1) + (3)
                        varB = int(reader2) + (3)
                        varC = int(reader3) + (3)
                        
                        replace_line('agendacounter3.txt', 0, str(varA)+'\n')
                        replace_line('agendacounter3.txt', 1, str(varB)+'\n')
                        replace_line('agendacounter3.txt', 2, str(varC)+'\n')
                        
                        t1.create_text (85, 20, text =var1, font = ("arial", width10,'bold'))

                        def r1(var2):replace_line('agendacounter5.txt', var2, '0\n')
                        r1(0);r1(1);r1(2);r1(3)
                        tk.destroy()
                    if agendacounter == "1":savestandard(huiswerk1)
                    if agendacounter == "2":savestandard(huiswerk2)
                    if agendacounter == "3":savestandard(huiswerk3)
                    if agendacounter == "4":savestandard(huiswerk4)
                    if agendacounter == "5":savestandard(huiswerk5)
                    if agendacounter == "6":savestandard(huiswerk6)
                    if agendacounter == "7":savestandard(huiswerk7)
                    if agendacounter == "8":savestandard(huiswerk8)
                    if agendacounter == "9":savestandard(huiswerk9)
                    if agendacounter == "10":savestandard(huiswerk10)
                    if agendacounter == "11":savestandard(huiswerk11)
                    if agendacounter == "12":savestandard(huiswerk12)
                    if agendacounter == "13":savestandard(huiswerk13)
                    if agendacounter == "14":savestandard(huiswerk14)
                    if agendacounter == "15":savestandard(huiswerk15)
                    if agendacounter == "16":savestandard(huiswerk16)
                    if agendacounter == "17":savestandard(huiswerk17)
                    if agendacounter == "18":savestandard(huiswerk18)
                    if agendacounter == "19":savestandard(huiswerk19)
                    if agendacounter == "20":savestandard(huiswerk20)
                Button(tk,text="Opslaan",font=('arial',12),bd=0,bg="gray80",relief="ridge",command=save).place(x=340,y=260)
        def s1(x1,y1):
            replace_line('agendacounter2.txt', 1, str(x1)+'\n')
            replace_line('agendacounter2.txt', 2, str(y1)+'\n')
        def k1(self): s1(width25,width155); test(self)
        def k2(self): s1(width25,width205); test(self)
        def k3(self): s1(width25,width255); test(self)
        def k4(self): s1(width25,width305); test(self)
        def k5(self): s1(width25,width355); test(self)
        def k6(self): s1(width25,width405); test(self)
        def k7(self): s1(width25,width455); test(self)
        def k8(self): s1(width25,width505); test(self)
        def k9(self): s1(width25,width555); test(self)
        def k10(self):s1(width25,width605); test(self)

        def k11(self): s1(width205,width155); test(self)
        def k12(self): s1(width205,width205); test(self)
        def k13(self): s1(width205,width255); test(self)
        def k14(self): s1(width205,width305); test(self)
        def k15(self): s1(width205,width355); test(self)
        def k16(self): s1(width205,width405); test(self)
        def k17(self): s1(width205,width455); test(self)
        def k18(self): s1(width205,width505); test(self)
        def k19(self): s1(width205,width555); test(self)
        def k20(self): s1(width205,width605); test(self)

        def k21(self): s1(width385,width155); test(self)
        def k22(self): s1(width385,width205); test(self)
        def k23(self): s1(width385,width255); test(self)
        def k24(self): s1(width385,width305); test(self)
        def k25(self): s1(width385,width355); test(self)
        def k26(self): s1(width385,width405); test(self)
        def k27(self): s1(width385,width455); test(self)
        def k28(self): s1(width385,width505); test(self)
        def k29(self): s1(width385,width555); test(self)
        def k30(self): s1(width385,width605); test(self)

        def k31(self): s1(width565,width155); test(self)
        def k32(self): s1(width565,width205); test(self)
        def k33(self): s1(width565,width255); test(self)
        def k34(self): s1(width565,width305); test(self)
        def k35(self): s1(width565,width355); test(self)
        def k36(self): s1(width565,width405); test(self)
        def k37(self): s1(width565,width455); test(self)
        def k38(self): s1(width565,width505); test(self)
        def k39(self): s1(width565,width555); test(self)
        def k40(self): s1(width565,width605); test(self)

        def k41(self): s1(width745,width155); test(self)
        def k42(self): s1(width745,width205); test(self)
        def k43(self): s1(width745,width255); test(self)
        def k44(self): s1(width745,width305); test(self)
        def k45(self): s1(width745,width355); test(self)
        def k46(self): s1(width745,width405); test(self)
        def k47(self): s1(width745,width455); test(self)
        def k48(self): s1(width745,width505); test(self)
        def k49(self): s1(width745,width555); test(self)
        def k50(self): s1(width745,width605); test(self)
        
        def z1(var1,var2,var3):t1 = Frame(LG,width=width170,height=width43,bg="white",bd=0);t1.bind("<ButtonRelease-1>", var1);t1.place(x=var2,y=var3)
        z1(k1,width25,width155);z1(k2,width25,width205);z1(k3,width25,width255);z1(k4,width25,width305)
        z1(k5,width25,width355);z1(k6,width25,width405);z1(k7,width25,width455);z1(k8,width25,width505)
        z1(k9,width25,width555);z1(k10,width25,width605)
        
        z1(k11,width205,width155);z1(k12,width205,width205);z1(k13,width205,width255);z1(k14,width205,width305)
        z1(k15,width205,width355);z1(k16,width205,width405);z1(k17,width205,width455);z1(k18,width205,width505)
        z1(k19,width205,width555);z1(k20,width205,width605)
        
        z1(k21,width385,width155);z1(k22,width385,width205);z1(k23,width385,width255);z1(k24,width385,width305)
        z1(k25,width385,width355);z1(k26,width385,width405);z1(k27,width385,width455);z1(k28,width385,width505)
        z1(k29,width385,width555);z1(k30,width385,width605)
        
        z1(k31,width565,width155);z1(k32,width565,width205);z1(k33,width565,width255);z1(k34,width565,width305)
        z1(k35,width565,width355);z1(k36,width565,width405);z1(k37,width565,width455);z1(k38,width565,width505)
        z1(k39,width565,width555);z1(k40,width565,width605)
        
        z1(k41,width745,width155);z1(k42,width745,width205);z1(k43,width745,width255);z1(k44,width745,width305)
        z1(k45,width745,width355);z1(k46,width745,width405);z1(k47,width745,width455);z1(k48,width745,width505)
        z1(k49,width745,width555);z1(k50,width745,width605)
        def times():
            c.create_text (10, var5, text =tijd, font = ("times", width10,'bold'))
        tijd=(12);var5=(width175);times();tijd=(13);var5=(width225);times();tijd=(14);var5=(width275);times();tijd=(13);var5=(width325);times()
        tijd=(14);var5=(width375);times();tijd=(15);var5=(width425);times();tijd=(16);var5=(width475);times();tijd=(17);var5=(width525);times()
        tijd=(18);var5=(width575);times();tijd=(19);var5=(width625);times()
        def lines():
            def l():c.create_text (var1, var2, text = "-------------------------------------------", font = ("times", width9))
            var2=(width200);l();var2=(width250);l();var2=(width300);l();var2=(width350);l();var2=(width400);l();var2=(width450);l();var2=(width500);l();var2=(width550);l();var2=(width600);l();var2=(width650);l();
        var1=(width110);lines();var1=(width290);lines();var1=(width470);lines();var1=(width650);lines();var1=(width830);lines();var1=(width1010);lines();var1=(width1190);lines()

        w5=open("agendacounter2.txt","r").readlines()[7];task1a=w5.strip();w6=open("agendacounter2.txt","r").readlines()[8];task1b=w6.strip();w7=open("agendacounter2.txt","r").readlines()[9];huiswerkvar1=w7.strip()
        w5=open("agendacounter2.txt","r").readlines()[10];task2a=w5.strip();w6=open("agendacounter2.txt","r").readlines()[11];task2b=w6.strip();w7=open("agendacounter2.txt","r").readlines()[12];huiswerkvar2=w7.strip()
        w5=open("agendacounter2.txt","r").readlines()[13];task3a=w5.strip();w6=open("agendacounter2.txt","r").readlines()[14];task3b=w6.strip();w7=open("agendacounter2.txt","r").readlines()[15];huiswerkvar3=w7.strip()
        w5=open("agendacounter2.txt","r").readlines()[16];task4a=w5.strip();w6=open("agendacounter2.txt","r").readlines()[17];task4b=w6.strip();w7=open("agendacounter2.txt","r").readlines()[18];huiswerkvar4=w7.strip()
        w5=open("agendacounter2.txt","r").readlines()[19];task5a=w5.strip();w6=open("agendacounter2.txt","r").readlines()[20];task5b=w6.strip();w7=open("agendacounter2.txt","r").readlines()[21];huiswerkvar5=w7.strip()
        w5=open("agendacounter2.txt","r").readlines()[22];task6a=w5.strip();w6=open("agendacounter2.txt","r").readlines()[23];task6b=w6.strip();w7=open("agendacounter2.txt","r").readlines()[24];huiswerkvar6=w7.strip()
        w5=open("agendacounter2.txt","r").readlines()[25];task7a=w5.strip();w6=open("agendacounter2.txt","r").readlines()[26];task7b=w6.strip();w7=open("agendacounter2.txt","r").readlines()[27];huiswerkvar7=w7.strip()
        w5=open("agendacounter2.txt","r").readlines()[28];task8a=w5.strip();w6=open("agendacounter2.txt","r").readlines()[29];task8b=w6.strip();w7=open("agendacounter2.txt","r").readlines()[30];huiswerkvar8=w7.strip()
        w5=open("agendacounter2.txt","r").readlines()[31];task9a=w5.strip();w6=open("agendacounter2.txt","r").readlines()[32];task9b=w6.strip();w7=open("agendacounter2.txt","r").readlines()[33];huiswerkvar9=w7.strip()
        w5=open("agendacounter2.txt","r").readlines()[34];task10a=w5.strip();w6=open("agendacounter2.txt","r").readlines()[35];task10b=w6.strip();w7=open("agendacounter2.txt","r").readlines()[36];huiswerkvar10=w7.strip()
                
        def agendacounter(var1,var2,var3):t6=Canvas(LG,width=width170,height=width43,bg=safecolor,bd=0);t6.place(x=var1,y=var2);t6.create_text(85,20,text=var3,font=("arial",width10,'bold'))

        def check1(var1,var2,var3):
            if var1 != "": agendacounter(var1,var2,var3)
        check1(task1a,task1b,huiswerkvar1)
        check1(task2a,task2b,huiswerkvar2)
        check1(task3a,task3b,huiswerkvar3)
        check1(task4a,task4b,huiswerkvar4)
        check1(task5a,task5b,huiswerkvar5)
        check1(task6a,task6b,huiswerkvar6)
        check1(task7a,task7b,huiswerkvar7)
        check1(task8a,task8b,huiswerkvar8)
        check1(task9a,task9b,huiswerkvar9)
        check1(task10a,task10b,huiswerkvar10)
def gebruikers():
    r1 = open("gebruiker1.txt", "r").readlines()[11]; rechten1=r1.strip()
    r1 = open("gebruiker1.txt", "r").readlines()[12]; rechten2=r1.strip()
    r1 = open("gebruiker1.txt", "r").readlines()[13]; rechten3=r1.strip()
    r1 = open("gebruiker1.txt", "r").readlines()[14]; rechten4=r1.strip()
    r1 = open("gebruiker1.txt", "r").readlines()[15]; rechten5=r1.strip()
    r1 = open("gebruiker1.txt", "r").readlines()[21]; user1=r1.strip()
    if rechten1 == "1" and user1 == "1" or rechten2 == "1" and user1 == "2" or rechten3 == "1" and user1 == "3" or rechten4 == "1" and user1 == "4" or rechten5 == "1" and user1 == "5":
        c1 = open("gebruiker1.txt", "r").readlines()[10]; counter1=c1.strip()
        with open('safecolor.txt', 'r') as f: safecolor = f.read()
        def sluiten(): HoverButton(LG, image=img1,bg="white",bd=0,command=LG.destroy).place(x=1240,y=5); HoverButton(LG, image=img2,bg="white",bd=0,command=homepage).place(x=1210,y=5)
        Frame(LG,width=1300,height=800,bg="white").place(x=0,y=0)
        Frame(LG,width=200,height=800,bg="gray20").place(x=0,y=0); sluiten()
        var1=IntVar(); var1.set(0)
        def test():
            Label(LG,text="Persoonlijke informatie",font=('arial',25,'bold'),bg="white").place(x=600,y=20)
            Frame(LG,width=800,height=2,bg=safecolor).place(x=400,y=100)
            Frame(LG,width=800,height=2,bg=safecolor).place(x=400,y=104)
            Frame(LG,width=800,height=2,bg=safecolor).place(x=400,y=400)
            Frame(LG,width=800,height=2,bg=safecolor).place(x=400,y=404)
            Frame(LG,width=2,height=304,bg=safecolor).place(x=400,y=100)
            Frame(LG,width=2,height=296,bg=safecolor).place(x=404,y=104)
            Frame(LG,width=2,height=296,bg=safecolor).place(x=1196,y=104)
            Frame(LG,width=2,height=304,bg=safecolor).place(x=1200,y=100)
            a4 = open("gebruiker1.txt", "r").readlines()[16]; aantal4=a4.strip()
            g1 = open("gebruiker1.txt", "r").readlines()[0]; gebruiker1 = g1.strip()
            g1 = open("gebruiker1.txt", "r").readlines()[5]; wachtwoord1 = g1.strip()
            g1 = open("gebruiker1.txt", "r").readlines()[22]; leeftijd1 = g1.strip()
            g1 = open("gebruiker1.txt", "r").readlines()[27]; email1 = g1.strip()
            Label(LG,text=str(gebruiker1)+"heeft"+str(aantal4)+"keer ingelogd",bg="white",font=('arial',15,'bold')).place(x=430,y=200)
            class HoverLabel(tk.Button):
                def __init__(self, master, **kw):
                    tk.Label.__init__(self,master=master,**kw)
                    self.bind("<Enter>", self.on_enter)
                    self.bind("<Leave>", self.on_leave)
                def on_enter(self, e):
                    Label(LG,text="Hiermee geeft u de gebruiker het recht \n om andere gebruikers te verwijderen",bd=0, font=('arial',8)).place(x=663,y=150)
                def on_leave(self, e):
                    Frame(LG,bg="white",width=190,height=40,bd=0).place(x=663,y=150)
            HoverLabel(LG,image=img10).place(x=653,y=125)
            s = ttk.Style()
            s.configure('my.TCheckbutton', font=('arial', 15,'bold'),bg="white")
            ttk.Checkbutton(LG,text="Administrator rechten",style='my.TCheckbutton',variable=var1).place(x=430,y=140)
            Label(LG,text="Wachtwoord is: "+str(wachtwoord1),font=('arial',15,'bold'),bg="white").place(x=430,y=260)
            Label(LG,text="Email is: "+str(email1),font=('arial',15,'bold'),bg="white").place(x=860,y=140)
            Label(LG,text="Leeftijd is: "+str(leeftijd1),font=('arial',15,'bold'),bg="white").place(x=860,y=200)
            def opslaan():
                if var1.get() == 1:
                    data[11] = '1' + '\n'
                    with open('gebruiker1.txt', 'w') as file: file.writelines( data )
                else:
                    data[11] = '0' + '\n'
                    with open('gebruiker1.txt', 'w') as file: file.writelines( data )
            g1 = open("safecolor.txt", "r").readlines()[0]; safecolor12 = g1.strip()
            if safecolor12 == "white":
                fg1="black"
            else:
                fg1="white"
            Button(LG,text="Opslaan",command=opslaan,bg=safecolor,bd=0,relief="groove",fg=fg1 ,font=('arial',12,'bold')).place(x=1130,y=410)
        if counter1 == '1':
            g1 = open("gebruiker1.txt", "r").readlines()[0]; gebruiker1=g1.strip()
            w1 = open("gebruiker1.txt", "r").readlines()[5]; wachtwoord1=w1.strip()
            HoverButton(LG,text=gebruiker1,bd=0,fg="white",font=('arial', 15, 'bold'), width= 15, height=1,bg="gray20",activebackground="gray30").place(x=0,y=0)
        if counter1 == '2':
            g1 = open("gebruiker1.txt", "r").readlines()[0]; gebruiker1=g1.strip()
            g2 = open("gebruiker1.txt", "r").readlines()[1]; gebruiker2=g2.strip()
            w1 = open("gebruiker1.txt", "r").readlines()[5]; wachtwoord1=w1.strip()
            w2 = open("gebruiker1.txt", "r").readlines()[6]; wachtwoord2=w2.strip()
            HoverButton(LG,text=gebruiker1,bd=0,fg="white",font=('arial', 15, 'bold'), width= 15, height=1,bg="gray20",activebackground="gray30").place(x=0,y=0)
            HoverButton(LG,text=gebruiker2,bd=0,fg="white",font=('arial', 15, 'bold'), width= 15, height=1,bg="gray20",activebackground="gray30").place(x=0,y=50)
        if counter1 == '3':
            g1 = open("gebruiker1.txt", "r").readlines()[0]; gebruiker1=g1.strip()
            g2 = open("gebruiker1.txt", "r").readlines()[1]; gebruiker2=g2.strip()
            g3 = open("gebruiker1.txt", "r").readlines()[2]; gebruiker3=g3.strip()
            w1 = open("gebruiker1.txt", "r").readlines()[5]; wachtwoord1=w1.strip()
            w2 = open("gebruiker1.txt", "r").readlines()[6]; wachtwoord2=w2.strip()
            w3 = open("gebruiker1.txt", "r").readlines()[7]; wachtwoord3=w3.strip()
            HoverButton(LG,text=gebruiker1,bd=0,fg="white",font=('arial', 15, 'bold'), width= 15, height=1,bg="gray20",activebackground="gray30").place(x=0,y=0)
            HoverButton(LG,text=gebruiker2,bd=0,fg="white",font=('arial', 15, 'bold'), width= 15, height=1,bg="gray20",activebackground="gray30").place(x=0,y=50)
            HoverButton(LG,text=gebruiker3,bd=0,fg="white",font=('arial', 15, 'bold'), width= 15, height=1,bg="gray20",activebackground="gray30").place(x=0,y=100)
        if counter1 == '4':
            g1 = open("gebruiker1.txt", "r").readlines()[0]; gebruiker1=g1.strip()
            g2 = open("gebruiker1.txt", "r").readlines()[1]; gebruiker2=g2.strip()
            g3 = open("gebruiker1.txt", "r").readlines()[2]; gebruiker3=g3.strip()
            g4 = open("gebruiker1.txt", "r").readlines()[3]; gebruiker4=g4.strip()
            w1 = open("gebruiker1.txt", "r").readlines()[5]; wachtwoord1=w1.strip()
            w2 = open("gebruiker1.txt", "r").readlines()[6]; wachtwoord2=w2.strip()
            w3 = open("gebruiker1.txt", "r").readlines()[7]; wachtwoord3=w3.strip()
            w4 = open("gebruiker1.txt", "r").readlines()[8]; wachtwoord4=w4.strip()
            HoverButton(LG,text=gebruiker1,bd=0,fg="white",font=('arial', 15, 'bold'), width= 15, height=1,bg="gray20",command=test,activebackground="gray30").place(x=0,y=15)
            HoverButton(LG,text=gebruiker2,bd=0,fg="white",font=('arial', 15, 'bold'), width= 15, height=1,bg="gray20",activebackground="gray30").place(x=0,y=65)
            HoverButton(LG,text=gebruiker3,bd=0,fg="white",font=('arial', 15, 'bold'), width= 15, height=1,bg="gray20",activebackground="gray30").place(x=0,y=115)
            HoverButton(LG,text=gebruiker4,bd=0,fg="white",font=('arial', 15, 'bold'), width= 15, height=1,bg="gray20",activebackground="gray30").place(x=0,y=165)
        if counter1 == '5':
            g1 = open("gebruiker1.txt", "r").readlines()[0]; gebruiker1=g1.strip()
            g2 = open("gebruiker1.txt", "r").readlines()[1]; gebruiker2=g2.strip()
            g3 = open("gebruiker1.txt", "r").readlines()[2]; gebruiker3=g3.strip()
            g4 = open("gebruiker1.txt", "r").readlines()[3]; gebruiker4=g4.strip()
            g5 = open("gebruiker1.txt", "r").readlines()[4]; gebruiker5=g5.strip()
            w1 = open("gebruiker1.txt", "r").readlines()[5]; wachtwoord1=w1.strip()
            w2 = open("gebruiker1.txt", "r").readlines()[6]; wachtwoord2=w2.strip()
            w3 = open("gebruiker1.txt", "r").readlines()[7]; wachtwoord3=w3.strip()
            w4 = open("gebruiker1.txt", "r").readlines()[8]; wachtwoord4=w4.strip()
            w5 = open("gebruiker1.txt", "r").readlines()[9]; wachtwoord5=w5.strip()
            HoverButton(LG,text=gebruiker1,bd=0,fg="white",font=('arial', 15, 'bold'), width= 15, height=1,bg="gray20",activebackground="gray30").place(x=0,y=0)
            HoverButton(LG,text=gebruiker2,bd=0,fg="white",font=('arial', 15, 'bold'), width= 15, height=1,bg="gray20",activebackground="gray30").place(x=0,y=50)
            HoverButton(LG,text=gebruiker3,bd=0,fg="white",font=('arial', 15, 'bold'), width= 15, height=1,bg="gray20",activebackground="gray30").place(x=0,y=100)
            HoverButton(LG,text=gebruiker4,bd=0,fg="white",font=('arial', 15, 'bold'), width= 15, height=1,bg="gray20",activebackground="gray30").place(x=0,y=150)
            HoverButton(LG,text=gebruiker5,bd=0,fg="white",font=('arial', 15, 'bold'), width= 15, height=1,bg="gray20",activebackground="gray30").place(x=0,y=200)
    else:
        messagebox.showinfo("Systeem", "Je hebt geen toegang tot dit")
class instellingen:
    def safecolor1(self): GU = "grey99";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor2(self): GU = "grey75";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor3(self): GU = "grey60";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor4(self): GU = "grey40";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor5(self): GU = "grey30";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor6(self): GU = "grey20";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor7(self): GU = "grey10";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor8(self): GU = "grey1";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor9(self): GU = "Bisque";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor10(self): GU = "Bisque2";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor11(self): GU = "Bisque3";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor12(self): GU = "Bisque4";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor13(self): GU = "RoyalBlue1";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor14(self): GU = "RoyalBlue2";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor15(self): GU = "RoyalBlue3";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor16(self): GU = "RoyalBlue4";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor17(self): GU = "LightSteelBlue1";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor18(self): GU = "LightSteelBlue2";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor19(self): GU = "LightSteelBlue3";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor20(self): GU = "LightSteelBlue4";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor21(self): GU = "cyan1";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor22(self): GU = "cyan2";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor23(self): GU = "cyan3";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor24(self): GU = "cyan4";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor25(self): GU = "lawn Green";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor26(self): GU = "green2";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor27(self): GU = "green3";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor28(self): GU = "green4";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor29(self): GU = "khaki1";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor30(self): GU = "khaki2";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor31(self): GU = "khaki3";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor32(self): GU = "khaki4";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor33(self): GU = "yellow";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor34(self): GU = "yellow2";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor35(self): GU = "yellow3";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor36(self): GU = "yellow4";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor37(self): GU = "red";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor38(self): GU = "red2";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor39(self): GU = "red3";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor40(self): GU = "red4";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor41(self): GU = "coral1";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor42(self): GU = "coral2";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor43(self): GU = "coral3";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor44(self): GU = "coral4";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor45(self): GU = "Orange Red";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor46(self): GU = "Orangered2";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor47(self): GU = "Orangered3";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor48(self): GU = "Orangered4";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor49(self): GU = "Maroon1";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor50(self): GU = "Maroon2";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor51(self): GU = "Maroon3";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor52(self): GU = "Maroon4";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor53(self): GU = "plum1";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor54(self): GU = "plum2";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor55(self): GU = "plum3";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor56(self): GU = "plum4";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor57(self): GU = "purple1";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor58(self): GU = "purple2";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor59(self): GU = "purple3";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor60(self): GU = "purple4";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor61(self): GU = "thistle1";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor62(self): GU = "thistle1";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor63(self): GU = "thistle1";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor64(self): GU = "thistle1";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor101(self): GU = "grey99";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor102(self): GU = "grey75";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor103(self): GU = "grey60";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor104(self): GU = "grey40";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor105(self): GU = "grey30";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor106(self): GU = "grey20";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor107(self): GU = "grey10";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor108(self): GU = "grey1";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor109(self): GU = "Bisque";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor110(self): GU = "Bisque2";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor111(self): GU = "Bisque3";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor112(self): GU = "Bisque4";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor113(self): GU = "RoyalBlue1";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor114(self): GU = "RoyalBlue2";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor115(self): GU = "RoyalBlue3";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor116(self): GU = "RoyalBlue4";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor117(self): GU = "LightSteelBlue1";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor118(self): GU = "LightSteelBlue2";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor119(self): GU = "LightSteelBlue3";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor120(self): GU = "LightSteelBlue4";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor121(self): GU = "cyan1";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor122(self): GU = "cyan2";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor123(self): GU = "cyan3";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor124(self): GU = "cyan4";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor125(self): GU = "lawn Green";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor126(self): GU = "green2";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor127(self): GU = "green3";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor128(self): GU = "green4";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor129(self): GU = "khaki1";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor130(self): GU = "khaki2";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor131(self): GU = "khaki3";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor132(self): GU = "khaki4";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor133(self): GU = "yellow";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor134(self): GU = "yellow2";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor135(self): GU = "yellow3";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor136(self): GU = "yellow4";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor137(self): GU = "red";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor138(self): GU = "red2";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor139(self): GU = "red3";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor140(self): GU = "red4";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor141(self): GU = "coral1";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor142(self): GU = "coral2";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor143(self): GU = "coral3";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor144(self): GU = "coral4";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor145(self): GU = "Orange Red";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor146(self): GU = "Orangered2";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor147(self): GU = "Orangered3";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor148(self): GU = "Orangered4";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor149(self): GU = "Maroon1";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor150(self): GU = "Maroon2";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor151(self): GU = "Maroon3";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor152(self): GU = "Maroon4";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor153(self): GU = "plum1";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor154(self): GU = "plum2";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor155(self): GU = "plum3";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor156(self): GU = "plum4";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor157(self): GU = "purple1";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor158(self): GU = "purple2";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor159(self): GU = "purple3";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor160(self): GU = "purple4";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor161(self): GU = "thistle1";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor162(self): GU = "thistle1";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor163(self): GU = "thistle1";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor164(self): GU = "thistle1";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def thema(self):
        def call_me1(): clr1 = colorchooser.askcolor(title="select color");cl1 = str(clr1);print(cl1)#;oTF = open('safecolor.txt', 'w'); oTF.write(cl1); oTF.close() 
        def call_me2(): clr2 = colorchooser.askcolor(title="select color");cl2 = str(clr2);oTF = open('safecolor2.txt', 'w'); oTF.write(cl2); oTF.close()
        with open('safecolor.txt', 'r') as f: safecolor = f.read()
        with open('safecolor2.txt', 'r') as f: safecolor = f.read()
        Canvas(LG,width=1000,height=750,bg="white",bd=0).place(x=300,y=0);sluiten(); Label(LG,font=('arial', 25),bg='white',fg="black",text="Thema's").place(x=350,y=30); Label(LG,text="Hoofd kleur",font=('arial', 18, 'bold'),bg="white").place(x=690,y=150); f1 = Frame(LG,width=870,bg="grey85",bd=0,height=200).place(x=335,y=185)
        #Button(LG,text="change color1",command=call_me1).place(x=100,y=400)
        #Button(LG,text="change color2",command=call_me2).place(x=100,y=450)
        HoverButton(LG,bg="grey99",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor1).place(x=350,y=200); HoverButton(LG,bg="grey75",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor2).place(x=400,y=200); HoverButton(LG,bg="grey60",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor3).place(x=450,y=200); HoverButton(LG,bg="grey40",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor4).place(x=500,y=200); HoverButton(LG,bg="grey30",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor5).place(x=550,y=200); HoverButton(LG,bg="grey20",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor6).place(x=600,y=200); HoverButton(LG,bg="grey10",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor7).place(x=650,y=200); HoverButton(LG,bg="grey1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor8).place(x=700,y=200); HoverButton(LG,bg="Bisque",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor9).place(x=350,y=245); HoverButton(LG,bg="Bisque2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor10).place(x=400,y=245); HoverButton(LG,bg="Bisque3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor11).place(x=450,y=245); HoverButton(LG,bg="Bisque4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor12).place(x=500,y=245); HoverButton(LG,bg="RoyalBlue1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor13).place(x=550,y=245); HoverButton(LG,bg="RoyalBlue2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor14).place(x=600,y=245); HoverButton(LG,bg="RoyalBlue3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor15).place(x=650,y=245); HoverButton(LG,bg="RoyalBlue4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor16).place(x=700,y=245); HoverButton(LG,bg="LightSteelBlue1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor17).place(x=350,y=290); HoverButton(LG,bg="LightSteelBlue2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor18).place(x=400,y=290); HoverButton(LG,bg="LightSteelBlue3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor19).place(x=450,y=290); HoverButton(LG,bg="LightSteelBlue4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor20).place(x=500,y=290); HoverButton(LG,bg="cyan1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor21).place(x=550,y=290); HoverButton(LG,bg="cyan2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor22).place(x=600,y=290); HoverButton(LG,bg="cyan3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor23).place(x=650,y=290); HoverButton(LG,bg="cyan4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor24).place(x=700,y=290); HoverButton(LG,bg="lawn Green",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor25).place(x=350,y=335); HoverButton(LG,bg="green2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor26).place(x=400,y=335); HoverButton(LG,bg="green3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor27).place(x=450,y=335); HoverButton(LG,bg="green4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor28).place(x=500,y=335); HoverButton(LG,bg="khaki1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor29).place(x=550,y=335); HoverButton(LG,bg="khaki2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor30).place(x=600,y=335); HoverButton(LG,bg="khaki3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor31).place(x=650,y=335); HoverButton(LG,bg="khaki4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor32).place(x=700,y=335); HoverButton(LG,bg="yellow",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor33).place(x=800,y=200); HoverButton(LG,bg="yellow2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor34).place(x=850,y=200); HoverButton(LG,bg="yellow3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor35).place(x=900,y=200); HoverButton(LG,bg="yellow4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor36).place(x=950,y=200); HoverButton(LG,bg="red",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor37).place(x=1000,y=200); HoverButton(LG,bg="red2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor38).place(x=1050,y=200); HoverButton(LG,bg="red3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor39).place(x=1100,y=200); HoverButton(LG,bg="red4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor40).place(x=1150,y=200); HoverButton(LG,bg="coral1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor41).place(x=800,y=245); HoverButton(LG,bg="coral2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor42).place(x=850,y=245); HoverButton(LG,bg="coral3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor43).place(x=900,y=245); HoverButton(LG,bg="coral4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor44).place(x=950,y=245); HoverButton(LG,bg="orange red",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor45).place(x=1000,y=245); HoverButton(LG,bg="Orangered2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor46).place(x=1050,y=245); HoverButton(LG,bg="Orangered3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor47).place(x=1100,y=245); HoverButton(LG,bg="Orangered4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor48).place(x=1150,y=245); HoverButton(LG,bg="Maroon1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor49).place(x=800,y=290); HoverButton(LG,bg="Maroon2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor50).place(x=850,y=290); HoverButton(LG,bg="Maroon3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor51).place(x=900,y=290); HoverButton(LG,bg="Maroon4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor52).place(x=950,y=290); HoverButton(LG,bg="plum1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor53).place(x=1000,y=290); HoverButton(LG,bg="plum2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor54).place(x=1050,y=290); HoverButton(LG,bg="plum3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor55).place(x=1100,y=290); HoverButton(LG,bg="plum4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor56).place(x=1150,y=290); HoverButton(LG,bg="purple1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor57).place(x=800,y=335); HoverButton(LG,bg="purple2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor58).place(x=850,y=335); HoverButton(LG,bg="purple3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor59).place(x=900,y=335); HoverButton(LG,bg="purple4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor60).place(x=950,y=335); HoverButton(LG,bg="thistle1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor61).place(x=1000,y=335); HoverButton(LG,bg="thistle2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor62).place(x=1050,y=335); HoverButton(LG,bg="thistle3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor63).place(x=1100,y=335); HoverButton(LG,bg="thistle4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor64).place(x=1150,y=335); Label(LG,text="Tweede kleur",font=('arial', 18, 'bold'),bg="white").place(x=690,y=450); f1 = Frame(LG,width=870,bg="grey85",bd=0,height=200).place(x=335,y=485); HoverButton(LG,bg="grey99",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor101).place(x=350,y=500); HoverButton(LG,bg="grey75",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor102).place(x=400,y=500); HoverButton(LG,bg="grey60",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor103).place(x=450,y=500); HoverButton(LG,bg="grey40",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor104).place(x=500,y=500); HoverButton(LG,bg="grey30",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor105).place(x=550,y=500); HoverButton(LG,bg="grey20",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor106).place(x=600,y=500); HoverButton(LG,bg="grey10",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor107).place(x=650,y=500); HoverButton(LG,bg="grey1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor108).place(x=700,y=500); HoverButton(LG,bg="Bisque",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor109).place(x=350,y=545); HoverButton(LG,bg="Bisque2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor110).place(x=400,y=545); HoverButton(LG,bg="Bisque3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor111).place(x=450,y=545); HoverButton(LG,bg="Bisque4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor112).place(x=500,y=545); HoverButton(LG,bg="RoyalBlue1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor113).place(x=550,y=545); HoverButton(LG,bg="RoyalBlue2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor114).place(x=600,y=545); HoverButton(LG,bg="RoyalBlue3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor115).place(x=650,y=545); HoverButton(LG,bg="RoyalBlue4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor116).place(x=700,y=545); HoverButton(LG,bg="LightSteelBlue1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor117).place(x=350,y=590); HoverButton(LG,bg="LightSteelBlue2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor118).place(x=400,y=590); HoverButton(LG,bg="LightSteelBlue3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor119).place(x=450,y=590); HoverButton(LG,bg="LightSteelBlue4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor120).place(x=500,y=590); HoverButton(LG,bg="cyan1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor121).place(x=550,y=590); HoverButton(LG,bg="cyan2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor122).place(x=600,y=590); HoverButton(LG,bg="cyan3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor123).place(x=650,y=590); HoverButton(LG,bg="cyan4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor124).place(x=700,y=590); HoverButton(LG,bg="lawn Green",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor125).place(x=350,y=635); HoverButton(LG,bg="green2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor126).place(x=400,y=635); HoverButton(LG,bg="green3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor127).place(x=450,y=635); HoverButton(LG,bg="green4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor128).place(x=500,y=635); HoverButton(LG,bg="khaki1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor129).place(x=550,y=635); HoverButton(LG,bg="khaki2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor130).place(x=600,y=635); HoverButton(LG,bg="khaki3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor131).place(x=650,y=635); HoverButton(LG,bg="khaki4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor132).place(x=700,y=635); HoverButton(LG,bg="yellow",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor133).place(x=800,y=500); HoverButton(LG,bg="yellow2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor134).place(x=850,y=500); HoverButton(LG,bg="yellow3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor135).place(x=900,y=500); HoverButton(LG,bg="yellow4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor136).place(x=950,y=500); HoverButton(LG,bg="red",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor137).place(x=1000,y=500); HoverButton(LG,bg="red2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor138).place(x=1050,y=500); HoverButton(LG,bg="red3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor139).place(x=1100,y=500); HoverButton(LG,bg="red4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor140).place(x=1150,y=500); HoverButton(LG,bg="coral1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor141).place(x=800,y=545); HoverButton(LG,bg="coral2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor142).place(x=850,y=545); HoverButton(LG,bg="coral3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor143).place(x=900,y=545); HoverButton(LG,bg="coral4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor144).place(x=950,y=545); HoverButton(LG,bg="orange red",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor145).place(x=1000,y=545); HoverButton(LG,bg="Orangered2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor146).place(x=1050,y=545); HoverButton(LG,bg="Orangered3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor147).place(x=1100,y=545); HoverButton(LG,bg="Orangered4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor148).place(x=1150,y=545); HoverButton(LG,bg="Maroon1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor149).place(x=800,y=590); HoverButton(LG,bg="Maroon2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor150).place(x=850,y=590); HoverButton(LG,bg="Maroon3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor151).place(x=900,y=590); HoverButton(LG,bg="Maroon4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor152).place(x=950,y=590); HoverButton(LG,bg="plum1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor153).place(x=1000,y=590); HoverButton(LG,bg="plum2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor154).place(x=1050,y=590); HoverButton(LG,bg="plum3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor155).place(x=1100,y=590); HoverButton(LG,bg="plum4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor156).place(x=1150,y=590); HoverButton(LG,bg="purple1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor157).place(x=800,y=635); HoverButton(LG,bg="purple2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor158).place(x=850,y=635); HoverButton(LG,bg="purple3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor159).place(x=900,y=635); HoverButton(LG,bg="purple4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor160).place(x=950,y=635); HoverButton(LG,bg="thistle1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor161).place(x=1000,y=635); HoverButton(LG,bg="thistle2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor162).place(x=1050,y=635); HoverButton(LG,bg="thistle3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor163).place(x=1100,y=635); HoverButton(LG,bg="thistle4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor164).place(x=1150,y=635)
    def wachtwoord(self):
        Canvas(LG,width=1000,height=750,bg="white",bd=0).place(x=300,y=0)
        e2=Entry(LG,bd=2,font=('arial',15),textvariable=wachtwoord2,relief="groove").place(x=400,y=360)
        e3=Entry(LG,bd=2,font=('arial',15),textvariable=gebruiker10,relief="groove").place(x=400,y=300)
        box=ttk.Combobox(LG,textvariable=loginofniet10,font=small_font,state='readonly'); box['values']=('Als ik het programma opstart','Nooit'); remembertest=box.current(0); box.place(x=400,y=190)
        Label(LG,text="Nieuwe gebruikersnaam:",font=('arial', 10),bg="white").place(x=400,y=270)
        Label(LG,text="Nieuw wachtwoord:",font=('arial', 10),bg="white").place(x=400,y=330)
        Label(LG,text="Aanmeldingsopties",font=('arial', 20),bg="white").place(x=400,y=30)
        Label(LG,text="Aanmelding vereisen",font=('arial', 16),bg="white").place(x=400,y=130)
        Label(LG,text="Wanneer moet er een log in scherm getoont worden?",font=('arial', 12),bg="white").place(x=400,y=160)
        Frame(LG,width=1,height=110,bg="gray20").place(x=380,y=120)
        Frame(LG,width=1,height=106,bg="gray20").place(x=382,y=122)
        Frame(LG,width=1,height=106,bg="gray20").place(x=780,y=122)
        Frame(LG,width=1,height=110,bg="gray20").place(x=782,y=120)
        Frame(LG,width=402,height=1,bg="gray20").place(x=380,y=120)
        Frame(LG,width=398,height=1,bg="gray20").place(x=382,y=122)
        Frame(LG,width=398,height=1,bg="gray20").place(x=382,y=228)
        Frame(LG,width=402,height=1,bg="gray20").place(x=380,y=230)

        Frame(LG,width=1,height=140,bg="gray20").place(x=380,y=260)
        Frame(LG,width=1,height=136,bg="gray20").place(x=382,y=262)
        Frame(LG,width=1,height=136,bg="gray20").place(x=740,y=262)
        Frame(LG,width=1,height=140,bg="gray20").place(x=742,y=260)
        Frame(LG,width=362,height=1,bg="gray20").place(x=380,y=260)
        Frame(LG,width=358,height=1,bg="gray20").place(x=382,y=262)
        Frame(LG,width=358,height=1,bg="gray20").place(x=382,y=398)
        Frame(LG,width=362,height=1,bg="gray20").place(x=380,y=400)
        g5 = open("gebruiker1.txt", "r").readlines()[10]; counter2=g5.strip()
        def nieuwwachtwoord(): fline=wachtwoord2.get();replace_line("gebruiker1.txt",counter2,fline)
        def nieuwegebruiker():
            GU = gebruiker10.get()
            replace_line("gebruiker1.txt",counter2,GU)
        def loginofnietsafe(): GU = loginofniet10.get(); oTF = open('loginofniet.txt', 'w'); oTF.write(GU); oTF.close(); return
        def loginofniet(): loginofnietsafe(); homepage()
        def loginofniet2(): loginofnietsafe(); LG.destroy()
        HoverButton(LG, image=img1,bg="white",bd=0,command=loginofniet2).place(x=1240,y=5); HoverButton(LG, image=img2,bg="white",bd=0,command=loginofniet).place(x=1210,y=5)
        Button(LG,text="update",font=('arial', 15),bd=0,bg="gray80",command=nieuwegebruiker).place(x=640,y=300)
        Button(LG,text="update",font=('arial', 15),bd=0,bg="gray80",command=nieuwwachtwoord).place(x=640,y=350)
    def gebruikersnaam(self):
        r1 = open("gebruiker1.txt", "r").readlines()[11]; rechten1=r1.strip()
        r1 = open("gebruiker1.txt", "r").readlines()[12]; rechten2=r1.strip()
        r1 = open("gebruiker1.txt", "r").readlines()[13]; rechten3=r1.strip()
        r1 = open("gebruiker1.txt", "r").readlines()[14]; rechten4=r1.strip()
        r1 = open("gebruiker1.txt", "r").readlines()[15]; rechten5=r1.strip()
        r1 = open("gebruiker1.txt", "r").readlines()[21]; user1=r1.strip()
        g1 = open("gebruiker1.txt", "r").readlines()[0]; gebruiker1=g1.strip()
        g2 = open("gebruiker1.txt", "r").readlines()[1]; gebruiker2=g2.strip()
        g3 = open("gebruiker1.txt", "r").readlines()[2]; gebruiker3=g3.strip()
        g4 = open("gebruiker1.txt", "r").readlines()[3]; gebruiker4=g4.strip()
        g5 = open("gebruiker1.txt", "r").readlines()[4]; gebruiker5=g5.strip()
        if rechten1 == "1" and user1 == "1" or rechten2 == "1" and user1 == "2" or rechten3 == "1" and user1 == "3" or rechten4 == "1" and user1 == "4" or rechten5 == "1" and user1 == "5":
            def del1(): messagebox.showinfo("Systeem", "Deze gebruiker kun je niet verwijderen")
            def del2():
                def run():
                    with open('gebruiker1.txt', 'w') as file: file.writelines( data )
                g5 = open("gebruiker1.txt", "r").readlines()[5]; gebruiker5=g5.strip()
                g5 = open("gebruiker1.txt", "r").readlines()[10]; wachtwoord=g5.strip()
                if wachtwoord=="5": data[10]='4' + '\n'; run()
                if wachtwoord=="4": data[10]='3' + '\n'; run()
                if wachtwoord=="3": data[10]='2' + '\n'; run()
                if wachtwoord=="2": data[10]='1' + '\n'; run()
                g5 = open("gebruiker1.txt", "r").readlines()[10]; wachtwoord=g5.strip()
                data[5]= '' + '\n' + gebruiker5 + '\n'; run()
                data[10]= '' + '\n' + wachtwoord + '\n'; run()
                data[1]=''; run(); data[6]=''; run()
                messagebox.showinfo("Systeem", "De gebruiker is verwijderd"); gebruikersnaam()
            def del3():
                def run():
                    with open('gebruiker1.txt', 'w') as file: file.writelines( data )
                g5 = open("gebruiker1.txt", "r").readlines()[5]; gebruiker5=g5.strip()
                g5 = open("gebruiker1.txt", "r").readlines()[10]; wachtwoord=g5.strip()
                if wachtwoord=="5": data[10]='4' + '\n'; run()
                if wachtwoord=="4": data[10]='3' + '\n'; run()
                if wachtwoord=="3": data[10]='2' + '\n'; run()
                g5 = open("gebruiker1.txt", "r").readlines()[10]; wachtwoord=g5.strip()
                data[5]= '' + '\n' + gebruiker5 + '\n'; run()
                data[10]= '' + '\n' + wachtwoord + '\n'; run()
                data[2]=''; run(); data[7]=''; run()
                messagebox.showinfo("Systeem", "De gebruiker is verwijderd"); gebruikersnaam()
            def del4():
                def run():
                    with open('gebruiker1.txt', 'w') as file: file.writelines( data )
                g5 = open("gebruiker1.txt", "r").readlines()[5]; gebruiker5=g5.strip()
                g5 = open("gebruiker1.txt", "r").readlines()[10]; wachtwoord=g5.strip()
                if wachtwoord=="5": data[10]='4' + '\n'; run()
                if wachtwoord=="4": data[10]='3' + '\n'; run()
                g5 = open("gebruiker1.txt", "r").readlines()[10]; wachtwoord=g5.strip()
                data[5]= '' + '\n' + gebruiker5 + '\n'; run()
                data[10]= '' + '\n' + wachtwoord + '\n'; run()
                data[3]=''; run(); data[8]=''; run()
                messagebox.showinfo("Systeem", "De gebruiker is verwijderd"); gebruikersnaam()
            def del5():
                def run():
                    with open('gebruiker1.txt', 'w') as file: file.writelines( data )
                g5 = open("gebruiker1.txt", "r").readlines()[5]; gebruiker5=g5.strip()
                data[10]='4' + '\n'; run()
                g5 = open("gebruiker1.txt", "r").readlines()[10]; wachtwoord=g5.strip()
                data[5]= '' + '\n' + gebruiker5 + '\n'; run()
                data[10]= '' + '\n' + wachtwoord + '\n'; run()
                data[4]=''; run(); data[9]=''; run()
                messagebox.showinfo("Systeem", "De gebruiker is verwijderd"); gebruikersnaam()
            def a1(): g1 = open("gebruiker1.txt", "r").readlines()[0]; gebruiker1=g1.strip(); HoverButton(LG,text=gebruiker1,bd=0,bg='gray80',font=('arial', 15),width=20,activebackground='gray30').place(x=900,y=160);HoverButton(LG,bg='red',activebackground='red4',bd=0,font=('arial', 24),text='x',width=2,command=del1).place(x=1120,y=150)
            def a2(): g2 = open("gebruiker1.txt", "r").readlines()[1]; gebruiker2=g2.strip(); HoverButton(LG,text=gebruiker2,bd=0,bg='gray80',font=('arial', 15),width=20,activebackground='gray30').place(x=900,y=210);HoverButton(LG,bg='red',activebackground='red4',bd=0,font=('arial', 24),text='x',width=2,command=del2).place(x=1120,y=200)
            def a3(): g3 = open("gebruiker1.txt", "r").readlines()[2]; gebruiker3=g3.strip(); HoverButton(LG,text=gebruiker3,bd=0,bg='gray80',font=('arial', 15),width=20,activebackground='gray30').place(x=900,y=260);HoverButton(LG,bg='red',activebackground='red4',bd=0,font=('arial', 24),text='x',width=2,command=del3).place(x=1120,y=250)
            def a4(): g4 = open("gebruiker1.txt", "r").readlines()[3]; gebruiker4=g4.strip(); HoverButton(LG,text=gebruiker4,bd=0,bg='gray80',font=('arial', 15),width=20,activebackground='gray30').place(x=900,y=310);HoverButton(LG,bg='red',activebackground='red4',bd=0,font=('arial', 24),text='x',width=2,command=del4).place(x=1120,y=300)
            def a5(): g5 = open("gebruiker1.txt", "r").readlines()[4]; gebruiker5=g5.strip(); HoverButton(LG,text=gebruiker5,bd=0,bg='gray80',font=('arial', 15),width=20,activebackground='gray30').place(x=900,y=360);HoverButton(LG,bg='red',activebackground='red4',bd=0,font=('arial', 24),text='x',width=2,command=del5).place(x=1120,y=350)
            Canvas(LG,width=1000,height=750,bg="white",bd=0).place(x=300,y=0)
            Entry(LG,font=('arial', 15),bd=2,relief="groove",textvariable=gebruiker10).place(x=400,y=200)
            wachtwoord2 = StringVar()
            wachtwoord3 = StringVar()
            leeftijd = StringVar()
            email = StringVar()
            Entry(LG,show='*',font=('arial', 15),bd=2,relief="groove",textvariable=wachtwoord2).place(x=400,y=250)
            Entry(LG,show='*',font=('arial', 15),bd=2,relief="groove",textvariable=wachtwoord3).place(x=400,y=300)
            Entry(LG,font=('arial', 15),bd=2,relief="groove",textvariable=leeftijd).place(x=400,y=350)
            Entry(LG,font=('arial', 15),bd=2,relief="groove",textvariable=email).place(x=400,y=400)
            Label(LG,text="Nieuwe gebruiker toevoegen / verwijderen",font=('arial', 20,'bold'),bg="white").place(x=400,y=30)
            Label(LG,text="Gebruikersnaam:",font=('arial', 10),bg="white").place(x=400,y=178)
            Label(LG,text="Wachtwoord:",font=('arial', 10),bg="white").place(x=400,y=228)
            Label(LG,text="Herhaal Wachtwoord:",font=('arial', 10),bg="white").place(x=400,y=278)
            Label(LG,text="Leeftijd:",font=('arial', 10),bg="white").place(x=400,y=328)
            Label(LG,text="Email:",font=('arial', 10),bg="white").place(x=400,y=378)
            Frame(LG,width=1,height=280,bg="gray20").place(x=380,y=168)
            Frame(LG,width=1,height=276,bg="gray20").place(x=382,y=170)
            Frame(LG,width=1,height=276,bg="gray20").place(x=645,y=170)
            Frame(LG,width=1,height=280,bg="gray20").place(x=647,y=168)

            Frame(LG,width=267,height=1,bg="gray20").place(x=380,y=168)
            Frame(LG,width=263,height=1,bg="gray20").place(x=382,y=170)
            Frame(LG,width=263,height=1,bg="gray20").place(x=382,y=446)
            Frame(LG,width=267,height=1,bg="gray20").place(x=380,y=448)
            r1 = open("gebruiker1.txt", "r").readlines()[10]; counter1=r1.strip()
            stop=StringVar()
            stop.set("0")
            def degebruikers():
                r1 = open("gebruiker1.txt", "r").readlines()[10]; counter1=r1.strip()
                if counter1 == "3":
                    xwidth= 156
                if counter1 == "4":
                    xwidth= 209
                else:
                    xwidth=156
                Frame(LG,width=220,height=xwidth,bg="gray80").place(x=900,y=150)
                if counter1 == '1': a1()
                if counter1 == '2': a1();a2()
                if counter1 == '3': a1();a2();a3()
                if counter1 == '4': a1();a2();a3();a4()
                if counter1 == '5': a1();a2();a3();a4();a5()
            degebruikers()
            def nieuwegebruiker1():
                if wachtwoord2.get()=="" or wachtwoord3.get()=="" or gebruiker10.get()=="" or leeftijd.get()=="" or email.get()=="":
                    messagebox.showinfo("Systeem", "Je mag geen velden leeg laten")
                    stop.set("1")
                    degebruikers()
                if gebruiker10.get() == gebruiker1 or gebruiker10.get() == gebruiker2 or gebruiker10.get() == gebruiker3 or gebruiker10.get() == gebruiker4 or gebruiker10.get() == gebruiker5:
                    messagebox.showinfo("Systeem", "Deze gebruikersnaam word al gebruikt")
                    stop.set("1")
                    degebruikers()
                if wachtwoord2.get() == wachtwoord3.get() and stop.get() == "0":
                    c1 = open("gebruiker1.txt", "r").readlines()[10]; counter1=c1.strip()
                    if counter1 == '1':
                        data[10]='2' + '\n'
                        with open('gebruiker1.txt', 'w') as file: file.writelines( data )
                    if counter1 == '2':
                        data[10]='3' + '\n'
                        with open('gebruiker1.txt', 'w') as file: file.writelines( data )
                    if counter1 == '3':
                        data[10]='4' + '\n'
                        with open('gebruiker1.txt', 'w') as file: file.writelines( data )
                    if counter1 == '4':
                        data[10]='5' + '\n'
                        with open('gebruiker1.txt', 'w') as file: file.writelines( data )
                    if counter1 == '5':
                        messagebox.showinfo("Systeem", "Je hebt al het maximaal aantal gebruikers")
                    def writeit1():
                        def run():
                            with open('gebruiker1.txt', 'w') as file: file.writelines( data )
                        if counter1 == '1':
                            data[1] = gebruiker10.get() + '\n'; run()
                            data[6] = wachtwoord2.get() + '\n'; run()
                            data[23] = leeftijd.get() + '\n'; run()
                            data[28] = email.get() + '\n'; run()
                        if counter1 == '2':
                            data[2] = gebruiker10.get() + '\n'; run()
                            data[7] = wachtwoord2.get() + '\n'; run()
                            data[24] = leeftijd.get() + '\n'; run()
                            data[29] = email.get() + '\n'; run()
                        if counter1 == '3':
                            data[3] = gebruiker10.get() + '\n'; run()
                            data[8] = wachtwoord2.get() + '\n'; run()
                            data[25] = leeftijd.get() + '\n'; run()
                            data[30] = email.get() + '\n'; run()
                        if counter1 == '4':
                            data[4] = gebruiker10.get() + '\n'; run()
                            data[9] = wachtwoord2.get() + '\n'; run()
                            data[26] = leeftijd.get() + '\n'; run()
                            data[31] = email.get() + '\n'; run()
                        if counter1 == '5':
                            pass
                    writeit1()
                    messagebox.showinfo("Systeem", "gelukt de gebruiker is toegevoegd")
                    degebruikers()
                else:
                    messagebox.showinfo("Systeem", "Wachtwoorden komen niet overeen")
                    gebruikersnaam()
            def loginofniet(): homepage()
            def loginofniet2(): LG.destroy()
            HoverButton(LG, image=img1,bg="white",bd=0,command=loginofniet2).place(x=1240,y=5); HoverButton(LG, image=img2,bg="white",bd=0,command=loginofniet).place(x=1210,y=5)
            Button(LG,text="Update",font=('arial', 13),bd=0,bg="gray80",relief="ridge",command=nieuwegebruiker1,fg="white").place(x=585,y=455)
        else:
            messagebox.showinfo("Systeem", "Je hebt geen toegang tot dit")
    def __init__(self):
        Canvas(LG,width=1280,height=750,bd=0,bg="white").place(x=0,y=0);sluiten()
        Frame(LG,width=300,height=1000,bg='gray20',bd=0).place(x=0,y=0)
        Label(LG,font=('arial', 15, 'bold'),bg='gray20',fg="white",text="Systeem").place(x=20,y=30)
        Button(LG,font=('arial', 15),bg='gray20',fg="white",text="Thema's",bd=0,command=self.thema).place(x=40,y=65)
        Button(LG,font=('arial', 15),bg='gray20',fg="white",text="Wachtwoord",bd=0,command=self.wachtwoord).place(x=40,y=100)
        Button(LG,font=('arial', 15),bg='gray20',fg="white",text="gebruikersnaam",bd=0,command=self.gebruikersnaam).place(x=40,y=145)
def forgotLG():
    Frame(LG,width=500,height=750,bd=0,bg="white").place(x=0,y=0)
    Label(LG,font=('arial',15, 'bold'),text="Op welk huis nummer woon ik").place(x=50,y=50)
    Button(LG,text="<--",command=LG.destroy).place(x=0,y=0)
    def wachtwoordverkrijgen():
        if wachtwoordherstel.get() == "68":
            Label(LG,text=wachtwoord1,font=('arial',15,'bold'),width=10).place(x=50,y=200)
        else:
            Label(LG,text="Antwoord is fout",fg="red",font=('arial',15,'bold')).place(x=50,y=200)
    e1=Entry(LG,textvariable=wachtwoordherstel).place(x=50,y=100)
    Button(LG,text="Herstel",command=wachtwoordverkrijgen).place(x=50,y=150)
def knorth():
    Canvas(LG,bg='white',bd=0,width=width,height=height).place(x=0,y=0)
    #================= vakken
    c1 = open("gebruiker1.txt", "r").readlines()[32]; f_contents1=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[33]; f_contents2=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[34]; f_contents3=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[35]; f_contents4=c1.strip()

    c1 = open("gebruiker1.txt", "r").readlines()[41]; f_contents5=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[42]; f_contents6=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[43]; f_contents7=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[44]; f_contents8=c1.strip()

    c1 = open("gebruiker1.txt", "r").readlines()[50]; f_contents9=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[51]; f_contents10=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[52]; f_contents11=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[53]; f_contents12=c1.strip()

    c1 = open("gebruiker1.txt", "r").readlines()[59]; f_contents13=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[60]; f_contents14=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[61]; f_contents15=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[62]; f_contents16=c1.strip()

    c1 = open("gebruiker1.txt", "r").readlines()[68]; f_contents17=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[69]; f_contents18=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[70]; f_contents19=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[71]; f_contents20=c1.strip()
    #================ week1 huiswerk
    c1 = open("gebruiker1.txt", "r").readlines()[77]; f_contents21=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[78]; f_contents22=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[79]; f_contents23=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[80]; f_contents24=c1.strip()

    c1 = open("gebruiker1.txt", "r").readlines()[86]; f_contents25=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[87]; f_contents26=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[88]; f_contents27=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[89]; f_contents28=c1.strip()

    c1 = open("gebruiker1.txt", "r").readlines()[95]; f_contents29=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[96]; f_contents30=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[97]; f_contents31=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[98]; f_contents32=c1.strip()

    c1 = open("gebruiker1.txt", "r").readlines()[104]; f_contents33=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[105]; f_contents34=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[106]; f_contents35=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[107]; f_contents36=c1.strip()

    c1 = open("gebruiker1.txt", "r").readlines()[113]; f_contents37=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[114]; f_contents38=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[115]; f_contents39=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[116]; f_contents40=c1.strip()
    #==============================

    c1 = open("toetsen.txt", "r").readlines()[0]; maandagtoetsen=c1.strip()
    c1 = open("toetsen.txt", "r").readlines()[1]; dinsdagtoetsen=c1.strip()
    c1 = open("toetsen.txt", "r").readlines()[2]; woensdagtoetsen=c1.strip()
    c1 = open("toetsen.txt", "r").readlines()[3]; donderdagtoetsen=c1.strip()
    c1 = open("toetsen.txt", "r").readlines()[4]; vrijdagtoetsen=c1.strip()
    c1 = open("toetsen.txt", "r").readlines()[5]; maandagtoetsen2=c1.strip()
    c1 = open("toetsen.txt", "r").readlines()[6]; dinsdagtoetsen2=c1.strip()
    c1 = open("toetsen.txt", "r").readlines()[7]; woensdagtoetsen2=c1.strip()
    c1 = open("toetsen.txt", "r").readlines()[8]; donderdagtoetsen2=c1.strip()
    c1 = open("toetsen.txt", "r").readlines()[9]; vrijdagtoetsen2=c1.strip()
    with open('safecolor.txt', 'r') as f: safecolor = f.read()
    with open('safecolor2.txt', 'r') as f: safecolor2 = f.read()
    def weekvooruitspoelen():
        GT = ""
        # Alle toetsen die in week 2 stonden worden naar week1 geschoven
        replace_line('toetsen.txt', 0, str(f_contents47) + '\n')
        replace_line('toetsen.txt', 1, str(f_contents48) + '\n')
        replace_line('toetsen.txt', 2, str(f_contents49) + '\n')
        replace_line('toetsen.txt', 3, str(f_contents50) + '\n')
        replace_line('toetsen.txt', 4, str(f_contents51) + '\n')
        # Alle toetsen uit week 2 worden leeg gemaakt of hervuld met toetsen uit week 3
        replace_line('toetsen.txt', 5, ' \n')
        replace_line('toetsen.txt', 6, ' \n')
        replace_line('toetsen.txt', 7, ' \n')
        replace_line('toetsen.txt', 8, ' \n')
        replace_line('toetsen.txt', 9, ' \n')
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

    var1=StringVar()
    var2=StringVar()
    var3=StringVar()
    var4=StringVar()
    var5=StringVar()
    var6=StringVar()
    var7=StringVar()
    var8=StringVar()
    var9=StringVar()
    var10=StringVar()
    var11=StringVar()
    var12=StringVar()
    var13=StringVar()
    var14=StringVar()
    var15=StringVar()
    var16=StringVar()
    var17=StringVar()
    var18=StringVar()
    var19=StringVar()
    var20=StringVar()
    #-------dagen die naar huiswerk lijden----------#
    class MouseControl1(tk.Button):
        def __init__(self, master, **kw):
            tk.Button.__init__(self,master=master,**kw)
            self.bind('<Double-1>', self.double_click)
            #f.bind("<Button-1>", self.left1)
            self.bind("<Button-3>", self.right1)
            self.defaultBackground = self["background"];self.bind("<Enter>", self.on_enter);self.bind("<Leave>", self.on_leave)
        def right1(self,event):
            addhomework14=StringVar()
            Label(LG,text="Huiswerk toevoegen",font=('arial',15),bg="white").place(x=55,y=20)
            Entry(LG,textvariable=addhomework14,font=('arial',15),bd=2,relief="sunken",bg="white").place(x=35,y=50)
            Label(LG,text="Dit huiswerk kun je in je agenda inplannen \n om ervoor te zorgen dat je een duidelijk \n overzicht hebt.",font=('arial', 10),bg="white").place(x=30,y=80)
            def save():
                c1 = open("agendacounter4.txt", "r").readlines()[7]; line1=c1.strip(); line = int(line1)
                #addhomework12=addhomework14.get(); homework1=addhomework12.strip()
                #print(addhomework14.get())
                #if homework1 == "test":
                #    print("gelukt")
                #else:
                #    print(homework1)
                #print(addhomework1)
                replace_line('gebruiker1.txt', line, str(addhomework14.get()) + '\n')

                lineA = line + (1)
                replace_line('agendacounter4.txt', 7, str(lineA) + '\n')
            Button(LG,text="Opslaan",command=save,bg="gray80",bd=0,font=('arial',12)).place(x=280,y=50)
        def on_enter(self, e):self['background'] = self['activebackground']
        def on_leave(self, e):self['background'] = self.defaultBackground
        def double_click(self, event):
            c1 = open("agendacounter4.txt", "r").readlines()[0]; x1=c1.strip()
            c1 = open("agendacounter4.txt", "r").readlines()[1]; y1=c1.strip()
            c1 = open("agendacounter4.txt", "r").readlines()[2]; x2=c1.strip()
            c1 = open("agendacounter4.txt", "r").readlines()[3]; y2=c1.strip()
            Entry(LG,textvariable=var1,font=('arial',width9,'bold'),bd=2,relief="sunken").place(x=x1,y=y1);Button(LG,text=">>",font=('arial',width10,'bold'),bd=0,bg="white",command=self.b).place(x=x2,y=y2)
        def b(self):
            if var1.get() == "":messagebox.showinfo("Systeem", "Je kunt dit veld niet leeg laten")
            else:
                c1 = open("agendacounter4.txt", "r").readlines()[4]; line1=c1.strip(); line = int(line1)
                c1 = open("agendacounter4.txt", "r").readlines()[5]; x3=c1.strip()
                c1 = open("agendacounter4.txt", "r").readlines()[6]; y3=c1.strip()
                test = var1.get();replace_line('gebruiker1.txt', line, var1.get() + '\n');MouseControl1(LG,bg='white',bd=0,width=width16,text=test,font=('arial', width15)).place(x=x3,y=y3)
    def e1(w1,w2,w3,w4,w5,w6,w7,w8):
        replace_line('agendacounter4.txt', 0, str(w1) + '\n')
        replace_line('agendacounter4.txt', 1, str(w2) + '\n')
        replace_line('agendacounter4.txt', 2, str(w3) + '\n')
        replace_line('agendacounter4.txt', 3, str(w4) + '\n')
        replace_line('agendacounter4.txt', 4, str(w5) + '\n')
        replace_line('agendacounter4.txt', 5, str(w6) + '\n')
        replace_line('agendacounter4.txt', 6, str(w7) + '\n')
        replace_line('agendacounter4.txt', 7, str(w8) + '\n')
    def d1(): e1(width139,width170,width240,width170,"32",width110,width160,77)
    def d2(): e1(width139,width210,width240,width210,"33",width110,width200,78)
    def d3(): e1(width139,width250,width240,width250,"34",width110,width240,79)
    def d4(): e1(width139,width290,width240,width290,"35",width110,width280,80)
    def d5(): e1(width350,width170,width450,width170,"41",width320,width160,81)
    def d6(): e1(width350,width210,width450,width210,"42",width320,width200,82)
    def d7(): e1(width350,width250,width450,width250,"43",width320,width240,83)
    def d8(): e1(width350,width290,width450,width290,"44",width320,width280,84)
    def d9(): e1(width560,width170,width660,width170,"50",width530,width160,85)
    def d10(): e1(width560,width210,width660,width210,"51",width530,width200,86)
    def d11(): e1(width560,width250,width660,width250,"52",width530,width240,87)
    def d12(): e1(width560,width290,width660,width290,"53",width530,width280,88)
    def d13(): e1(width770,width170,width870,width170,"59",width740,width160,89)
    def d14(): e1(width770,width210,width870,width210,"60",width740,width200,90)
    def d15(): e1(width770,width250,width870,width250,"61",width740,width240,91)
    def d16(): e1(width770,width290,width870,width290,"62",width740,width280,92)
    def d17(): e1(width980,width170,width1080,width170,"68",width950,width160,93)
    def d18(): e1(width980,width210,width1080,width210,"69",width950,width200,94)
    def d19(): e1(width980,width250,width1080,width250,"70",width950,width240,95)
    def d20(): e1(width980,width290,width1080,width290,"71",width950,width280,96)
    def vakkenmetdagen():
        MouseControl1(LG,bg='white',bd=0,width=width15,text=f_contents20,font=('arial', width15),command=d20).place(x=width940,y=width280)
        MouseControl1(LG,bg='white',bd=0,width=width15,text=f_contents19,font=('arial', width15),command=d19).place(x=width940,y=width240)
        MouseControl1(LG,bg='white',bd=0,width=width15,text=f_contents18,font=('arial', width15),command=d18).place(x=width940,y=width200)
        MouseControl1(LG,bg='white',bd=0,width=width15,text=f_contents17,font=('arial', width15),command=d17).place(x=width940,y=width160)
        MouseControl1(LG,bg='white',bd=0,width=width15,text=f_contents16,font=('arial', width15),command=d16).place(x=width730,y=width280)
        MouseControl1(LG,bg='white',bd=0,width=width15,text=f_contents15,font=('arial', width15),command=d15).place(x=width730,y=width240)
        MouseControl1(LG,bg='white',bd=0,width=width15,text=f_contents14,font=('arial', width15),command=d14).place(x=width730,y=width200)
        MouseControl1(LG,bg='white',bd=0,width=width15,text=f_contents13,font=('arial', width15),command=d13).place(x=width730,y=width160)
        MouseControl1(LG,bg='white',bd=0,width=width15,text=f_contents12,font=('arial', width15),command=d12).place(x=width520,y=width280)
        MouseControl1(LG,bg='white',bd=0,width=width15,text=f_contents11,font=('arial', width15),command=d11).place(x=width520,y=width240)
        MouseControl1(LG,bg='white',bd=0,width=width15,text=f_contents10,font=('arial', width15),command=d10).place(x=width520,y=width200)
        MouseControl1(LG,bg='white',bd=0,width=width15,text=f_contents9,font=('arial', width15),command=d9).place(x=width520,y=width160)
        MouseControl1(LG,bg='white',bd=0,width=width15,text=f_contents8,font=('arial', width15),command=d8).place(x=width320,y=width280)
        MouseControl1(LG,bg='white',bd=0,width=width15,text=f_contents7,font=('arial', width15),command=d7).place(x=width320,y=width240)
        MouseControl1(LG,bg='white',bd=0,width=width15,text=f_contents6,font=('arial', width15),command=d6).place(x=width320,y=width200)
        MouseControl1(LG,bg='white',bd=0,width=width15,text=f_contents5,font=('arial', width15),command=d5).place(x=width320,y=width160)
        MouseControl1(LG,bg='white',bd=0,width=width15,text=f_contents4,font=('arial', width15),command=d4).place(x=width110,y=width280)
        MouseControl1(LG,bg='white',bd=0,width=width15,text=f_contents3,font=('arial', width15),command=d3).place(x=width110,y=width240)
        MouseControl1(LG,bg='white',bd=0,width=width15,text=f_contents2,font=('arial', width15),command=d2).place(x=width110,y=width200)
        MouseControl1(LG,bg='white',bd=0,width=width15,text=f_contents1,font=('arial', width15),command=d1).place(x=width110,y=width160)
    vakkenmetdagen()
    #-------labels met de toetsen erin--------------#
    class HoverLabel1(tk.Label):
        def __init__(self, master, **kw):tk.Label.__init__(self,master=master,**kw);self.bind('<Double-1>', self.changetoetsen)
        def changetoetsen(self,event):
            ct1=StringVar();Entry(LG,textvariable=ct1,font=('arial',10),bd=2,relief="sunken",bg="white").place(x=width150,y=width600)
            def b():A8 = ct1.get();replace_line('toetsen.txt', 0, str(A8) + '\n');HoverLabel1(LG,bg='white',bd=0,width=17,height=6,text=A8,font=('arial', 15)).place(x=width110,y=width540)
            Button(LG,text=">>",font=('arial',width10,'bold'),bd=0,bg="white",command=b).place(x=width280,y=width600)
    class HoverLabel2(tk.Label):
        def __init__(self, master, **kw):tk.Label.__init__(self,master=master,**kw);self.bind('<Double-1>', self.changetoetsen)
        def changetoetsen(self,event):
            ct1=StringVar();Entry(LG,textvariable=ct1,font=('arial',10),bd=2,relief="sunken",bg="white").place(x=width360,y=width600)
            def b():A8 = ct1.get();replace_line('toetsen.txt', 1, str(A8) + '\n');HoverLabel2(LG,bg='white',bd=0,width=17,height=6,text=A8,font=('arial', 15)).place(x=width320,y=width540)
            Button(LG,text=">>",font=('arial',width10,'bold'),bd=0,bg="white",command=b).place(x=width490,y=width600)
    class HoverLabel3(tk.Label):
        def __init__(self, master, **kw):tk.Label.__init__(self,master=master,**kw);self.bind('<Double-1>', self.changetoetsen)
        def changetoetsen(self,event):
            ct1=StringVar();Entry(LG,textvariable=ct1,font=('arial',10),bd=2,relief="sunken",bg="white").place(x=width570,y=width600)
            def b():A8 = ct1.get();replace_line('toetsen.txt', 2, str(A8) + '\n');HoverLabel3(LG,bg='white',bd=0,width=17,height=6,text=A8,font=('arial', 15)).place(x=width530,y=width540)
            Button(LG,text=">>",font=('arial',width10,'bold'),bd=0,bg="white",command=b).place(x=width700,y=width600)
    class HoverLabel4(tk.Label):
        def __init__(self, master, **kw):tk.Label.__init__(self,master=master,**kw);self.bind('<Double-1>', self.changetoetsen)
        def changetoetsen(self,event):
            ct1=StringVar();Entry(LG,textvariable=ct1,font=('arial',10),bd=2,relief="sunken",bg="white").place(x=width780,y=width600)
            def b():A8 = ct1.get();replace_line('toetsen.txt', 3, str(A8) + '\n');HoverLabel4(LG,bg='white',bd=0,width=17,height=6,text=A8,font=('arial', 15)).place(x=width740,y=width540)
            Button(LG,text=">>",font=('arial',width10,'bold'),bd=0,bg="white",command=b).place(x=width910,y=width600)
    class HoverLabel5(tk.Label):
        def __init__(self, master, **kw):tk.Label.__init__(self,master=master,**kw);self.bind('<Double-1>', self.changetoetsen)
        def changetoetsen(self,event):
            ct1=StringVar();Entry(LG,textvariable=ct1,font=('arial',10),bd=2,relief="sunken",bg="white").place(x=width990,y=width600)
            def b():A8 = ct1.get();replace_line('toetsen.txt', 4, str(A8) + '\n');HoverLabel5(LG,bg='white',bd=0,width=17,height=6,text=A8,font=('arial', 15)).place(x=width950,y=width540)
            Button(LG,text=">>",font=('arial',width10,'bold'),bd=0,bg="white",command=b).place(x=width1120,y=width600)
        
    def labelsmettoetsen(v1,v2,v3,v4,v5):
        HoverLabel1(LG,bg='white',bd=0,width=17,height=7,text=v1,font=('arial', 15)).place(x=width110,y=width540)
        HoverLabel2(LG,bg='white',bd=0,width=17,height=7,text=v2,font=('arial', 15)).place(x=width310,y=width540)
        HoverLabel3(LG,bg='white',bd=0,width=17,height=7,text=v3,font=('arial', 15)).place(x=width520,y=width540)
        HoverLabel4(LG,bg='white',bd=0,width=17,height=7,text=v4,font=('arial', 15)).place(x=width730,y=width540)
        HoverLabel5(LG,bg='white',bd=0,width=17,height=7,text=v5,font=('arial', 15)).place(x=width940,y=width540)
    labelsmettoetsen(maandagtoetsen,dinsdagtoetsen,woensdagtoetsen,donderdagtoetsen,vrijdagtoetsen)
    def labelsmetdagen():
        Label(LG,bg='white',bd=0,width=width10,height=width3,text="Maandag",font=('arial', width15, 'bold')).place(x=width110,y=width60)
        Label(LG,bg='white',bd=0,width=width10,height=width3,text="Dinsdag",font=('arial', width15, 'bold')).place(x=width320,y=width60)
        Label(LG,bg='white',bd=0,width=width10,height=width3,text="Woensdag",font=('arial', width15, 'bold')).place(x=width530,y=width60)
        Label(LG,bg='white',bd=0,width=width10,height=width3,text="Donderdag",font=('arial', width15, 'bold')).place(x=width740,y=width60)
        Label(LG,bg='white',bd=0,width=width10,height=width3,text="Vrijdag",font=('arial', width15, 'bold')).place(x=width950,y=width60)
    #-------de datum bovenaan-----------------------#
    def datum(datum):Label(LG,bg='white',bd=0,height=2,text=datum,font=('arial', width40, 'bold')).place(x=width490,y=0)
    datum("Deze week")
    #-------de lijnen die als kader zijn------------#
    def lijnen():
        # liggenlijnen voor vakken
        def ligvakken(y1):Canvas(LG,bg=safecolor,bd=0,height=width1,width=width1050,highlightthickness=0).place(x=width100,y=y1)
        ligvakken(width135);ligvakken(width139);ligvakken(width416);ligvakken(width420)
        
        # liggende lijnen voor toetsen
        def ligtoetsen(y1):Canvas(LG,bg=safecolor2,bd=0,height=width1,width=width1050).place(x=width100,y=y1)
        ligtoetsen(width525);ligtoetsen(width530);ligtoetsen(width685);ligtoetsen(width690)
        
        # rechtopstaande lijnen voor vakken
        def rechtvakken(x1):Canvas(LG,bg=safecolor,bd=0,height=width285,width=width1,highlightthickness=0).place(x=x1,y=width135)
        rechtvakken(width98);rechtvakken(width102);rechtvakken(width308);rechtvakken(width312);rechtvakken(width518);rechtvakken(width522);rechtvakken(width728);rechtvakken(width732);rechtvakken(width938);rechtvakken(width942);rechtvakken(width1148);rechtvakken(width1152)

        # rechtopstaande lijnen voor toetsen
        def rechttoetsen(x1):Canvas(LG,bg=safecolor2,bd=0,height=width164,width=width1).place(x=x1,y=width525)
        rechttoetsen(width98);rechttoetsen(width102);rechttoetsen(width308);rechttoetsen(width312);rechttoetsen(width518);rechttoetsen(width522);rechttoetsen(width728);rechttoetsen(width732);rechttoetsen(width938);rechttoetsen(width942);rechttoetsen(width1148);rechttoetsen(width1152)
    def volgendeweek1():
        Frame(LG,width=width,height=height,bg="white").place(x=0,y=0)
        labelsmetdagen()
        sluiten()
        datum("volgende Week")
        labelsmettoetsen(maandagtoetsen2,dinsdagtoetsen2,woensdagtoetsen2,donderdagtoetsen2,vrijdagtoetsen2)
        lijnen()
    lijnen()
    b21=HoverButton(LG,bg=safecolor,bd=0,width=width3,height=width10,text=">",font=('arial', width20),activebackground='gray79',command=volgendeweek1).place(x=width1190,y=width200)
    def komendeweken():
        with open('dezemaand1.txt', 'r') as f: dezemaand1 = f.read()
        wekende=Tk(); wekende.attributes('-fullscreen',True); wekende.configure(background='white')
        def dezeweekmaand1():
            f= open("dezemaand1.txt"); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(1.0, studGradeString); f.close(); return
        def openFiles1(selection):
            if selection == "februari/april": dezeweekmaand1()
        def maandopslaan1():
             GU = aboutStud.get(1.0,END)
             oTF = open('dezemaand1.txt', 'w'); oTF.write(GU); oTF.close(); return

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
        Label(t1,font=('arial',15),text=f_contents21,bg="white",bd=0).place(x=300,y=35)
        Label(t1,font=('arial',15),text=f_contents22,bg="white",bd=0).place(x=300,y=85)
        Label(t1,font=('arial',15),text=f_contents23,bg="white",bd=0).place(x=300,y=135)
        Label(t1,font=('arial',15),text=f_contents24,bg="white",bd=0).place(x=300,y=185)
        Label(t1,font=('arial',15),text=f_contents25,bg="white",bd=0).place(x=300,y=235)
        Label(t1,font=('arial',15),text=f_contents26,bg="white",bd=0).place(x=300,y=285)
        Label(t1,font=('arial',15),text=f_contents27,bg="white",bd=0).place(x=300,y=335)
        Label(t1,font=('arial',15),text=f_contents28,bg="white",bd=0).place(x=300,y=385)
        Label(t1,font=('arial',15),text=f_contents29,bg="white",bd=0).place(x=300,y=435)
        Label(t1,font=('arial',15),text=f_contents30,bg="white",bd=0).place(x=300,y=485)
        Label(t1,font=('arial',15),text=f_contents31,bg="white",bd=0).place(x=300,y=535)
        Label(t1,font=('arial',15),text=f_contents32,bg="white",bd=0).place(x=300,y=585)
        Label(t1,font=('arial',15),text=f_contents33,bg="white",bd=0).place(x=970,y=35)
        Label(t1,font=('arial',15),text=f_contents34,bg="white",bd=0).place(x=970,y=85)
        Label(t1,font=('arial',15),text=f_contents35,bg="white",bd=0).place(x=970,y=135)
        Label(t1,font=('arial',15),text=f_contents36,bg="white",bd=0).place(x=970,y=185)
        Label(t1,font=('arial',15),text=f_contents37,bg="white",bd=0).place(x=970,y=235)
        Label(t1,font=('arial',15),text=f_contents38,bg="white",bd=0).place(x=970,y=285)
        Label(t1,font=('arial',15),text=f_contents39,bg="white",bd=0).place(x=970,y=335)
        Label(t1,font=('arial',15),text=f_contents40,bg="white",bd=0).place(x=970,y=385)
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
    Button(LG, image=img7 ,bd=0,bg="white",command=waarschuwing).place(x=width10,y=width660)
def algemeen():
    pass
def baas():
    pass
def personeel():
    pass
class app():
    def __init__(self):
        #Button(LG,text="run",command=self.run_progressBar).place(x=0,y=0)
        Label(LG,text="Bezig met Updaten", font=('arial',20,'bold'),bg="white").place(x=530,y=400)
        s = ttk.Style()
        s.theme_use('default')
        s.configure("Horizontal.TProgressbar", foreground='red', background='red')
        self.progress_bar = ttk.Progressbar(LG,style="Horizontal.TProgressbar", orient = 'horizontal', length = 400)
        self.progress_bar.place(x=450,y=500)
        #def run_progressBar(self):
         
        self.progress_bar['maximum']=100

        for i in range(101):
            time.sleep(0.03)
            self.progress_bar["value"] = i
            self.progress_bar.update()
        self.progress_bar["value"] = 0
def internet_on():
    def wifi():
        data = urllib2.urlopen('https://github.com/bramteunis/-myprogram/blob/master/test.txt').read()
        data1 = re.findall(r'<td id="LC1" class="blob-code blob-code-inner js-file-line">(.*?)</td>',str(data))
        if data1[0] == needed: pass
        else:
            if messagebox.askyesno("Systeem", "Je hebt een update nodig. Wil je deze downloaden") == True:
                access1 = (1)
                webbrowser.open_new_tab('https://github.com/bramteunis/code/archive/master.zip')
                for x in range (0,500):
                    app()
                    my_file = Path('C:/Users/'+str(username)+'/Downloads/code-master.zip')
                    if my_file.is_file():
                        shutil.rmtree('C:/Users/'+str(username)+'/Downloads/SchoolSysteem/code-master')   
                        #shutil.move('-myprogram-master.zip','C:/Users/bramt/Desktop')
                        zib_obj = zipfile.ZipFile('C:/Users/'+str(username)+'/Downloads/code-master.zip','r')
                        zib_obj.extractall('C:/Users/'+str(username)+'/Downloads/SchoolSysteem')
                        zib_obj.close()
                        os.remove("C:/Users/"+str(username)+"/Downloads/code-master.zip")
                        break
                    else:
                        #counter = float
                        #counter += (1)
                        #if counter == (99):
                        #    messagebox.showinfo("Systeem", "Controleer of je Internet hebt en probeer het opnieuw")
                        pass
            else: app()
        

    def geenwifi():
        messagebox.showinfo("Systeem", "Zorg ervoor dat je wifi hebt");internet_on()
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
        wifi()
    except urllib2.URLError as err:
        geenwifi()
        
if loginofniet11 == "Nooit":
    internet_on()
    homepage()
    if test == "green":
        #data[0] = width1 + '\n'
        #with open('lastwidth.txt', 'w') as file: file.writelines( data )
        #data[1] = height1 + '\n'
        #with open('lastwidth.txt', 'w') as file: file.writelines( data )
        pass
else:
    internet_on()
    if access1 == (0):
        Button(LG,image=img11,bd=0).place(x=width500,y=-3)
        var = IntVar()
        #frame1.place(x=500,y=-3)

        Button(LG,image=img12,bd=0,bg="white").place(x=width10,y=width30)
        
        #Button(LG,image=img13,bd=0,bg="white").place(x=width50,y=width685)
        
        Button(LG,text='Wachtwoord vergeten?',width=20,bd=0,height=1,font=('arial', width12),bg="white",fg="blue",command=forgotLG).place(x=width140,y=width600)
        Button(LG,text='Afsluiten',width=7,bd=0,height=1,font=('arial', width10),bg="white",command=LG.destroy).place(x=width25,y=width685)

        Label(LG,text='Gebruikersnaam:',bd=0,font=('arial', width10),bg="white").place(x=width70,y=width270)
        Label(LG,text='Wachtwoord:',bd=0,font=('arial', width10),bg="white").place(x=width70,y=width370)
        Label(LG,text='Goede avond,',bd=0,font=('arial', width14, 'bold'),bg="white").place(x=width70,y=width180)
        Label(LG,text='welkom terug!',bd=0,font=('arial', width14),bg="white").place(x=width210,y=width180)
        Label(LG,text='Voel je vrij om op ieder moment in te loggen.',bd=0,font=('arial', width11),bg="white").place(x=width70,y=width210)
        Checkbutton(LG,text="Onthoud mij",bg="white",variable=var3,font=('arial',width10),onvalue=1,offvalue=0).place(x=width70,y=width470)
        t1=Entry(LG,show='*',textvariable=value1,bd=2,font=('arial', width20),relief="groove").place(x=width70,y=width400)
        if counter1 == '1':
            g1 = open("gebruiker1.txt", "r").readlines()[0]; gebruiker1=g1.strip()
            w1 = open("gebruiker1.txt", "r").readlines()[5]; wachtwoord1=w1.strip()
            Button(LG,text='login',bd=0,fg="black",font=('arial', width20), width= width20, height=1, command= Gebruikersnaam1,bg=safecolor,relief="ridge").place(x=width70,y=width540)
            box=ttk.Combobox(LG,textvariable=value3,font=medium_font,state='readonly'); box['values']=(gebruiker1); remembertest=box.current(0)
            box.place(x=width70,y=width300)
        if counter1 == '2':
            g1 = open("gebruiker1.txt", "r").readlines()[0]; gebruiker1=g1.strip()
            g2 = open("gebruiker1.txt", "r").readlines()[1]; gebruiker2=g2.strip()
            w1 = open("gebruiker1.txt", "r").readlines()[5]; wachtwoord1=w1.strip()
            w2 = open("gebruiker1.txt", "r").readlines()[6]; wachtwoord2=w2.strip()
            Button(LG,text='login',bd=0,fg="black",font=('arial', width20), width= width20, height=1, command= Gebruikers2,bg=safecolor,relief="ridge").place(x=width70,y=width540)
            box=ttk.Combobox(LG,textvariable=value3,font=medium_font,state='readonly'); box['values']=(gebruiker1,gebruiker2); remembertest=box.current(0)
            box.place(x=width70,y=width300)
        if counter1 == '3':
            g1 = open("gebruiker1.txt", "r").readlines()[0]; gebruiker1=g1.strip()
            g2 = open("gebruiker1.txt", "r").readlines()[1]; gebruiker2=g2.strip()
            g3 = open("gebruiker1.txt", "r").readlines()[2]; gebruiker3=g3.strip()
            w1 = open("gebruiker1.txt", "r").readlines()[5]; wachtwoord1=w1.strip()
            w2 = open("gebruiker1.txt", "r").readlines()[6]; wachtwoord2=w2.strip()
            w3 = open("gebruiker1.txt", "r").readlines()[7]; wachtwoord3=w3.strip()
            Button(LG,text='login',bd=0,fg="black",font=('arial', width20), width= width20, height=1, command= Gebruikers3,bg=safecolor,relief="ridge").place(x=width70,y=width540)
            box=ttk.Combobox(LG,textvariable=value3,font=medium_font,state='readonly'); box['values']=(gebruiker1,gebruiker2,gebruiker3); remembertest=box.current(0)
            box.place(x=width70,y=width300)
        if counter1 == '4':
            g1 = open("gebruiker1.txt", "r").readlines()[0]; gebruiker1=g1.strip()
            g2 = open("gebruiker1.txt", "r").readlines()[1]; gebruiker2=g2.strip()
            g3 = open("gebruiker1.txt", "r").readlines()[2]; gebruiker3=g3.strip()
            g4 = open("gebruiker1.txt", "r").readlines()[3]; gebruiker4=g4.strip()
            w1 = open("gebruiker1.txt", "r").readlines()[5]; wachtwoord1=w1.strip()
            w2 = open("gebruiker1.txt", "r").readlines()[6]; wachtwoord2=w2.strip()
            w3 = open("gebruiker1.txt", "r").readlines()[7]; wachtwoord3=w3.strip()
            w4 = open("gebruiker1.txt", "r").readlines()[8]; wachtwoord4=w4.strip()
            Button(LG,text='login',bd=0,fg="black",font=('arial', width20), width= width20, height=1, command= Gebruikers4,bg=safecolor,relief="ridge").place(x=width70,y=width540)
            box=ttk.Combobox(LG,textvariable=value3,font=medium_font,state='readonly'); box['values']=(gebruiker1,gebruiker2,gebruiker3,gebruiker4); remembertest=box.current(0)
            box.place(x=width70,y=width300)
        if counter1 == '5':
            g1 = open("gebruiker1.txt", "r").readlines()[0]; gebruiker1=g1.strip()
            g2 = open("gebruiker1.txt", "r").readlines()[1]; gebruiker2=g2.strip()
            g3 = open("gebruiker1.txt", "r").readlines()[2]; gebruiker3=g3.strip()
            g4 = open("gebruiker1.txt", "r").readlines()[3]; gebruiker4=g4.strip()
            g5 = open("gebruiker1.txt", "r").readlines()[4]; gebruiker5=g5.strip()
            w1 = open("gebruiker1.txt", "r").readlines()[5]; wachtwoord1=w1.strip()
            w2 = open("gebruiker1.txt", "r").readlines()[6]; wachtwoord2=w2.strip()
            w3 = open("gebruiker1.txt", "r").readlines()[7]; wachtwoord3=w3.strip()
            w4 = open("gebruiker1.txt", "r").readlines()[8]; wachtwoord4=w4.strip()
            w5 = open("gebruiker1.txt", "r").readlines()[9]; wachtwoord5=w5.strip()
            Button(LG,text='login',bd=0,fg="black",font=('arial', width20), width= width20, height=1, command= Gebruikers5,bg=safecolor,relief="ridge").place(x=width70,y=width540)
            box=ttk.Combobox(LG,textvariable=value3,font=medium_font,state='readonly'); box['values']=(gebruiker1,gebruiker2,gebruiker3,gebruiker4,gebruiker5); box.current(0)
            box.place(x=width70,y=width300)
        def sluiten1(): LG.destroy()
    else:
        LG.destroy()
        
LG.mainloop()
