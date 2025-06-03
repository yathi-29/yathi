from tkinter import *
#include 
#/c/Users/ya2at/AppData/Roaming/SPB_Data/yathi

def run():
    def page2(player1,player2,):
        window.destroy()
        def pressed(place,lcheck,l):
            c=lcheck.pop(0)
            if place==1: 
                    a=0
                    b=0
                    if c%2==0:
                        b1txt.set("X")
                        b1.configure(disabledforeground="pink")

                    else:
                        b1txt.set("O")
                    b1.config(state=DISABLED)
            elif place==2:
                    a=0
                    b=1
                    if c%2==0:
                        b2txt.set("X")
                    else:
                        b2txt.set("O")
                    b2.config(state=DISABLED)
            elif place==3:
                    a=0
                    b=2
                    if c%2==0:
                        b3txt.set("X")
                    else:
                        b3txt.set("O")
                    b3.config(state=DISABLED)
                    
            elif place==4:
                    a=1
                    b=0
                    if c%2==0:
                        b4txt.set("X")
                    else:
                        b4txt.set("O")
                    b4.config(state=DISABLED)
            elif place==5:
                    a=1
                    b=1
                    if c%2==0:
                        b5txt.set("X")
                    else:
                        b5txt.set("O")
                    b5.config(state=DISABLED)
            elif place==6:
                    a=1
                    b=2
                    if c%2==0:
                        b6txt.set("X")
                    else:
                        b6txt.set("O")
                    b6.config(state=DISABLED)
                    
            elif place==7:
                    a=2
                    b=0
                    if c%2==0:
                        b7txt.set("X")
                    else:
                        b7txt.set("O")
                    b7.config(state=DISABLED)
            elif place==8:
                    a=2
                    b=1
                    if c%2==0:
                        b8txt.set("X")
                    else:
                        b8txt.set("O")
                    b8.config(state=DISABLED)
            elif place==9:
                    a=2
                    b=2
                    if c%2==0:
                        b9txt.set("X")
                        
                
                    else:
                        b9txt.set("O")
                        b9.config(fg="red")
                    b9.config(state=DISABLED)
            def disable():
                b1.config(state=DISABLED)
                b2.config(state=DISABLED)
                b3.config(state=DISABLED)
                b4.config(state=DISABLED)
                b5.config(state=DISABLED)
                b6.config(state=DISABLED)
                b7.config(state=DISABLED)
                b8.config(state=DISABLED)
                b9.config(state=DISABLED)
                
            def check(l):
                d={'r1':[l[0][0],l[0][1],l[0][2]],'r2':[l[1][0],l[1][1],l[1][2]],'r3':[l[2][0],l[2][1],l[2][2]],'c1':[l[0][0],l[1][0],l[2][0]],'c2':[l[0][1],l[1][1],l[2][1]],'c3':[l[0][2],l[1][2],l[2][2]],'d1':[l[0][0],l[1][1],l[2][2]],'d2':[l[0][2],l[1][1],l[2][0]]}
                for i in d:
                    first=d[i][0]
                    if first!=0:
                        
                        if first==d[i][1] and first==d[i][2]:
                            if i =="r1":
                                b1.config(bg="light green")
                                b2.config(bg="light green")
                                b3.config(bg="light green")
                            elif i =="r2":
                                b4.config(bg="light green")
                                b5.config(bg="light green")
                                b6.config(bg="light green")
                            elif i =="r3":
                                b7.config(bg="light green")
                                b8.config(bg="light green")
                                b9.config(bg="light green")
                            elif i =="c1":
                                b1.config(bg="light green")
                                b4.config(bg="light green")
                                b7.config(bg="light green")
                            elif i =="c2":
                                b2.config(bg="light green")
                                b5.config(bg="light green")
                                b8.config(bg="light green")
                            elif i =="c3":
                                b3.config(bg="light green")
                                b6.config(bg="light green")
                                b9.config(bg="light green")
                            if i =="d1":
                                b1.config(bg="light green")
                                b5.config(bg="light green")
                                b9.config(bg="light green")
                            elif i =="d2":
                                b3.config(bg="light green")
                                b5.config(bg="light green")
                                b7.config(bg="light green")
                            
                            print(d[i][0],d[i][1],d[i][2])
                            disable()
                            return first
                            

            if c%2==0:
                nplayertxt.set(player2+"\'s turn")
                l[int(a)][int(b)]='x' 
                res=check(l)
                if res=='x' :
                    print(res)
                    winer_label=Label(window1,font=("Helvetica bold",25),text="winers is "+player1)
                    #winer_label.place(x=0,y=0)
                    winer_label.grid(row=0,column=1)
                    plr.destroy()
                elif res=='o':
                    print(res)
                    winer_label=Label(window1,font=("Helvetica bold",25),text="winers is "+player2)
                    #winer_label.place(x=0,y=0)
                    winer_label.grid(row=0,column=1)
                    plr.destroy()
            else:
                l[int(a)][int(b)]='o'
                nplayertxt.set(player1+"\'s turn")
                res=check(l)
                if res=='x':
                    print(res)
                    winer_label=Label(window1,font=("Helvetica bold",25),text="winers is "+player1)
                    #winer_label.place(x=0,y=0)
                    winer_label.grid(row=0,column=1)
                    plr.destroy()

                elif res=='o':
                    print(res)
                    winer_label=Label(window1,font=("Helvetica bold",25),text="winers is "+player2)
                    #winer_label.place(x=0,y=0)
                    winer_label.grid(row=0,column=1)
                    plr.destroy()
            print(l)
            fg=1
            for i in l:
                for j in i:
                    if j==0:
                        fg=0
            if fg==1:
                print("draw")
                dra=Label(window1,font=("Helvetica bold",25),text="DRAW")
                dra.grid(row=0,column=1)
                plr.destroy()

        
        window1=Tk()
        l=[]
        for i in range(3):
            l1=[]
            for j in range(3):
                l1.append(0)
            l.append(l1)
        lcheck=[0,1,2,3,4,5,6,7,8]

        
        global nplayertxt
        nplayertxt=StringVar() 
        plr=Label(window1,font=("Helvetica bold",25),textvariable=nplayertxt)
        plr.grid(row=0,column=1)
        #b1.size(height=100, width=100)

     

        global b1txt
        b1txt = StringVar()
        b1=Button(window1,textvariable=b1txt,height = 5, width = 10,command=lambda:pressed(1,lcheck,l))
        b1.grid(row=1,column=0)
        global b2txt
        b2txt = StringVar()
        b2=Button(window1,textvariable=b2txt,height = 5, width = 10,command=lambda:pressed(2,lcheck,l))
        b2.grid(row=1,column=1)

        global b3txt
        b3txt = StringVar()
        b3=Button(window1,textvariable=b3txt,height = 5, width = 10,command=lambda:pressed(3,lcheck,l))
        b3.grid(row=1,column=2)

        global b4txt
        b4txt = StringVar()
        b4=Button(window1,textvariable=b4txt,height = 5, width = 10,command=lambda:pressed(4,lcheck,l))
        b4.grid(row=2,column=0)

        global b5txt
        b5txt = StringVar()
        b5=Button(window1,textvariable=b5txt,height = 5, width = 10,command=lambda:pressed(5,lcheck,l))
        b5.grid(row=2,column=1)

        global b6txt
        b6txt = StringVar()
        b6=Button(window1,textvariable=b6txt,height = 5, width = 10,command=lambda:pressed(6,lcheck,l))
        b6.grid(row=2,column=2)

        global b7txt
        b7txt = StringVar()
        b7=Button(window1,textvariable=b7txt,height = 5, width = 10,command=lambda:pressed(7,lcheck,l))
        b7.grid(row=3,column=0)

        global b8txt
        b8txt = StringVar()
        b8=Button(window1,textvariable=b8txt,height = 5, width = 10,command=lambda:pressed(8,lcheck,l))
        b8.grid(row=3,column=1)

        global b9txt
        b9txt = StringVar()
        b9=Button(window1,fg="red",textvariable=b9txt,height = 5, width = 10,command=lambda:pressed(9,lcheck,l))
        b9.grid(row=3,column=2)
        window1.mainloop()
    
    global window
    window=Tk()

    window.title("TIC TAC TOE")

    window.geometry("500x500")

    head=Label(window,text="TIC TAC TOE")
    head.pack()

    player1=Label(window,text="X - Player 1 Name ")
    player1.place(x=10,y=30)

    player1_entry=Entry(window)
    player1_entry.place(x=160,y=30)

    player2=Label(window,text="O - Player 2 Name ")
    player2.place(x=10,y=60)

    player2_entry=Entry(window)
    player2_entry.place(x=160,y=60)


    
    start_button=Button(window,text="START",command=lambda: page2(player1_entry.get(),player2_entry.get()))
    start_button.place(x=200,y=200)

    window.mainloop()
run()


'''
def check(l):
    d={'r1':[l[0][0],l[0][1],l[0][2]],'r2':[l[1][0],l[1][1],l[1][2]],'r3':[l[2][0],l[2][1],l[2][2]],'c1':[l[0][0],l[1][0],l[2][0]],'c2':[l[0][1],l[1][1],l[2][1]],'c3':[l[0][2],l[1][2],l[2][2]],'d1':[l[0][0],l[1][1],l[2][2]],'d2':[l[0][2],l[1][1],l[2][0]]}
    for i in d:
        first=d[i][0]
        if first!=0:
            
            if first==d[i][1] and first==d[i][2]:
                return first
l=[]
for i in range(3):
    l1=[]
    for j in range(3):
        l1.append(0)
    l.append(l1)
print(l)
for i in range(9):
    po=input('Enter the pos')
    l3=po.split(',')
    a=l3[0]
    b=l3[1]
    if i%2==0:
        l[int(a)][int(b)]='x'
        res=check(l)
        if res=='x' or res=='o':
            print(res)
            break
        
       
    else:
        l[int(a)][int(b)]='o'
        r=check(l)
        if r=='x' or r=='o':
            print(r)
            break
        
    print(l)
'''
