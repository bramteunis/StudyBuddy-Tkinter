from tkinter import *
#addhomework12=StringVar()
#addhomework1=StringVar()
homework=Tk()
homework.geometry("270x200")
homework.resizable(False, False)
homework.title("Huiswerk toevoegen")
addhomework14=StringVar()
Label(homework,text="Huiswerk toevoegen",font=('arial',15)).place(x=30,y=20)
Entry(homework,textvariable=addhomework14,font=('arial',15),bd=2,relief="sunken").place(x=20,y=50)
Label(homework,text="Dit huiswerk kun je in je agenda inplannen \n om ervoor te zorgen dat je een duidelijk \n overzicht hebt.",font=('arial', 10)).place(x=20,y=80)
def save():
    #c1 = open("agendacounter4.txt", "r").readlines()[7]; line1=c1.strip(); line = int(line1)
    addhomework12=addhomework14.get(); homework1=addhomework12.strip()
    print(addhomework14.get())
    #if homework1 == "test":
    #    print("gelukt")
    #else:
    #    print(homework1)
    #print(addhomework1)
    #replace_line('gebruiker1.txt', 77, str(addhomework14.get()) + '\n')
    homework.destroy()
Button(homework,text="Opslaan",command=save).place(x=35,y=120)
