from tkinter import *
import time
from tkinter import ttk
import random
from PIL import ImageTk,Image


def display(take,flaimage):

        black_screen=Label(window,bg="black",width=110,height=8)
        black_screen.place(x=0,y=360)

        label_show=Label(window,text=take.upper(),font=("arial", 40,"bold"),
                         foreground="green",bg="black")
        label_show.place(x=255,y=385)

        open_photo = Image.open(flaimage)
        resize_photo = open_photo.resize((163,100))
        edit_photo = ImageTk.PhotoImage(resize_photo)

        label_image = Label(window, image=edit_photo,bg="black")
        label_image.image=edit_photo
        label_image.place(x=95,y=380)

def rest():

    window.destroy()
    run()

def cal(boy_nam,girl_nam):

    l=[]
    l1=[]

    global boy_name
    boy_name=boy_nam.lower()

    global girl_name
    girl_name=girl_nam.lower()


    for boy_name_letter in boy_name:
        if boy_name_letter.isalpha():
            l.append(boy_name_letter)

    for girl_name_letter in girl_name:
        if girl_name_letter.isalpha():

            if girl_name_letter in l:
                l1.append(girl_name_letter)

            if girl_name_letter not in l:
                l.append(girl_name_letter)

    for repeated_letter in l1:
        while repeated_letter in l:
            l.remove(repeated_letter)

    len1=len(l)

    if len1>0:
        l2=['f','l','a','m','e','s']

        while len(l2)>1:
            x=len1%len(l2)
            ind=x-1
            (l2.pop(ind))

            if l2==['f']:
                print('Friends')
                take="Friends"
                flaimage="frd.png"

            elif l2==['l']:
                print('Lovers')
                take="Lovers"
                flaimage="lov.png"

            elif l2==['a']:
                print('Affectionate')
                take="Affectionate"
                flaimage="aff.png"

            elif l2==['m']:
                print('Marriage')
                take="Marriage"
                flaimage="mar.png"

            elif l2==['e']:
                print('Enimes')
                take="Enemies"
                flaimage="ene.png"

            elif l2==['s']:
                print('Siblings')
                take="Sibling"
                flaimage="sib.png"

    s=ttk.Style()
    s.theme_use("clam")
    s.configure("#00FFF3.Horizontal.TProgressbar",background="#00FFF3",bordercolor="#00FFF3")

    global bar1
    bar1 = ttk.Progressbar(window,orient=HORIZONTAL,style="#00FFF3.Horizontal.TProgressbar",length=120)
    bar1.place(x=0,y=420)

    def start1():

        GB1=10
        download1 = 0

        while(download1<GB1):
            time.sleep(1)
            bar1['value']+=100
            download1+=10
            window.update_idletasks()
            break

        if download1==10:
            global Friend
            Friend=Label(window,text="Friends",bg="black",font=("arial", 25,"bold"),foreground="#FF00D8")
            Friend.place(x=7,y=445)

    window.after(1,start1)


    s2=ttk.Style()
    s2.theme_use("clam")
    s2.configure("#FF00D8.Horizontal.TProgressbar",background="#FF00D8",bordercolor="#FF00D8")

    global bar2
    bar2 = ttk.Progressbar(window,orient=HORIZONTAL,style="#FF00D8.Horizontal.TProgressbar",length=120)
    bar2.place(x=120,y=420)

    def start2():

        GB2=10
        download2 = 0

        while(download2<GB2):
            time.sleep(1)
            bar2['value']+=100
            download2+=10
            window.update_idletasks()
            break

        if download2==10:
            global Lovers
            Lovers=Label(window,text="Lovers",bg="black",font=("arial", 25, "bold"),foreground="#00FFF3")
            Lovers.place(x=123,y=370)

    window.after(1,start2)


    s3=ttk.Style()
    s3.theme_use("clam")
    s3.configure("#00FFF3.Horizontal.TProgressbar",background="#00FFF3",bordercolor="#00FFF3")

    global bar3
    bar3 = ttk.Progressbar(window,orient=HORIZONTAL,style="#00FFF3.Horizontal.TProgressbar",length=120)
    bar3.place(x=240,y=420)

    def start3():

        GB3=10
        download3 = 0

        while(download3<GB3):
            time.sleep(1)
            bar3['value']+=100
            download3+=10
            window.update_idletasks()
            break

        if download3==10:
            global Affectionate
            Affectionate=Label(window,text="Affectionate",bg="black",font=("arial",20, "bold"),foreground="#FF00D8")
            Affectionate.place(x=220,y=450)

    window.after(1,start3)

    s4=ttk.Style()
    s4.theme_use("clam")
    s4.configure("#FF00D8.Horizontal.TProgressbar",background="#FF00D8",bordercolor="#FF00D8")

    global bar4
    bar4 = ttk.Progressbar(window,orient=HORIZONTAL,style="#FF00D8.Horizontal.TProgressbar",length=120)
    bar4.place(x=360,y=420)

    def start4():

        GB4=10
        download4 = 0

        while(download4<GB4):
            time.sleep(1)
            bar4['value']+=100
            download4+=10
            window.update_idletasks()
            break

        if download4==10:
            global Marriage
            Marriage=Label(window,text="Marriage",bg="black",font=("arial", 20, "bold"),foreground="#00FFF3")
            Marriage.place(x=360,y=370)

    window.after(1,start4)

    s5=ttk.Style()
    s5.theme_use("clam")
    s5.configure("#00FFF3.Horizontal.TProgressbar",background="#00FFF3",bordercolor="#00FFF3")

    global bar5
    bar5 = ttk.Progressbar(window,orient=HORIZONTAL,style="#00FFF3.Horizontal.TProgressbar",length=120)
    bar5.place(x=480,y=420)

    def start5():

        GB5=10
        download5 = 0

        while(download5<GB5):
            time.sleep(1)
            bar5['value']+=100
            download5+=10
            window.update_idletasks()
            break

        if download5==10:
            global Enemies
            Enemies=Label(window,text="Enemies",bg="black",font=("arial", 20, "bold"),foreground="#FF00D8")
            Enemies.place(x=480,y=450)

    window.after(1,start5)

    s6=ttk.Style()
    s6.theme_use("clam")
    s6.configure("#FF00D8.Horizontal.TProgressbar",background="#FF00D8",bordercolor="#FF00D8")

    global bar6
    bar6 = ttk.Progressbar(window,orient=HORIZONTAL,style="#FF00D8.Horizontal.TProgressbar",length=120)
    bar6.place(x=600,y=420)

    def start6():

        GB6=10
        download6 = 0

        while(download6<GB6):
            time.sleep(1)
            bar6['value']+=100
            download6+=10
            window.update_idletasks()
            break

        if download6==10:
            global Sibling
            Sibling=Label(window,text="Sibling",bg="black",font=("arial", 20, "bold"),foreground="#00FFF3")
            Sibling.place(x=610,y=370)

    window.after(1,start6)

    l3=["Friend","Lovers","Affectionate","Marriage","Enemies","Sibling"]

    if l2==['f']:
        l3.remove("Friend")

    elif l2==['l']:
        l3.remove("Lovers")

    elif l2==['a']:
        l3.remove("Affectionate")

    elif l2==['m']:
        l3.remove("Marriage")

    elif l2==['e']:
        l3.remove("Enemies")

    elif l2==['s']:
        l3.remove("Sibling")

    def removing():

        while len(l3)>0:

            time.sleep(0.5)

            index_destroy=random.randrange(0,len(l3))
            removed=l3.pop(index_destroy)

            if removed=="Sibling":
                Sibling.destroy()

            elif removed=="Friend":
                Friend.destroy()

            elif removed=="Enemies":
                Enemies.destroy()

            elif removed=="Marriage":
                Marriage.destroy()

            elif removed=="Affectionate":
                Affectionate.destroy()

            elif removed=="Lovers":
                Lovers.destroy()

        window.after(2000,lambda:display(take,flaimage))

    window.after(6500,lambda: removing())

def run():

    global window
    window=Tk()
    window.title("FLAMES")
    window.config(bg="black")
    window.geometry("723x500")
    window.resizable(0,0)
    icon_photo=PhotoImage(file="icon_image.png")
    window.iconphoto(False,icon_photo)

    label = Label(window,text="FLA",font=("arial", 30, "bold"),foreground="#00FFF3", bg="#FF00D8",width=3, height=1)
    label.place(x=282, y=30)

    label1 = Label(window,text="MES",font=("arial", 30, "bold"),foreground="#FF00D8", bg="#00FFF3",width=3, height=1)
    label1.place(x=360, y=30)

    boy_label = Label(window,font=("arial", 18, "bold"), bg="#00FFF3",width=20, height=5)
    boy_label.place(x=20, y=110)

    girl_label = Label(window, font=("arial", 18, "bold"), bg="#FF00D8",width=20, height=5)
    girl_label.place(x=400, y=110)

    boy_name=Label(window,text="Name: ",font=("arial",20,"bold"),foreground="#FF00D8",bg="#00FFF3")
    boy_name.place(x=20,y=130)

    girl_name=Label(window,text="Name: ",font=("arial",20,"bold"),foreground="#00FFF3",bg="#FF00D8")
    girl_name.place(x=400,y=130)

    boy_entry=Entry(window,font=("Helvetica",18,"bold"))
    boy_entry.place(x=50,y=190)

    girl_entry=Entry(window,font=("Helvetica",18,"bold"))
    girl_entry.place(x=430,y=190)

    submit_button=Button(window,text="CALCULATE",font=("Helvetica",18,"bold"),command=lambda:cal(boy_entry.get(),girl_entry.get()),bg="#00FFF3",foreground="#FF00D8")
    submit_button.place(x=220,y=300)

    reset_button=Button(window,text="RESET",font=("Helvetica",18,"bold"),bg="#FF00D8",foreground="#00FFF3",command=lambda:rest())
    reset_button.place(x=400,y=300)

    window.mainloop()

run()
