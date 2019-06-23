# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 21:00:18 2019

@author: Deepali
"""

from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import os

root=Tk()
root.title("Ready to play!!...Here you GO")

chances=6
img_paths=["hangmanid7.png","hangmanid6.png","hangmanid5.png","hangmanid4.png","hangmanid3.png","hangmanid2.png","hangmanid1.png"]
img=Image.open(img_paths[chances])
img=ImageTk.PhotoImage(img)
panel=Label(root,image=img)
panel.grid(row=2,column=2)
answer_arr=[]

def clicked(char):
    word='PYTHON'
    global chances;answer_arr;
    
    if char in word:
        answer_arr.append(char)
        if char=='P':
            b1["text"]=char
        elif char=='Y':
            b2['text']=char
        elif char=='T':
            b3['text']=char
        elif char=='H':
            b4['text']=char
        elif char=='O':
            b5['text']=char
        elif char=='N':
            b6['text']=char
    else:
        chances-=1
        txt="Chances remaining are "+str(chances);
        label.configure(text=txt)
        image=Image.open(img_paths[chances])
        imgnew=ImageTk.PhotoImage(image)
        panel.configure(image=imgnew)
        panel.image=imgnew
        
        if chances<=0 :
            messagebox.showinfo("Lost to guess","Hanged")
            root.destroy()
    if len(answer_arr)==6: 
            messagebox.showinfo('Congrats','You WON :):)')
            root.destroy();
    
    
b1=Button(root,text='',bg='White',fg='Black',width=3,height=1,font=('Helvetica','20'))
b1.grid(row=2,column=3)
b2=Button(root,text='',bg='White',fg='Black',width=3,height=1,font=('Helvetica','20'))
b2.grid(row=2,column=4)
b3=Button(root,text='',bg='White',fg='Black',width=3,height=1,font=('Helvetica','20'))
b3.grid(row=2,column=5)
b4=Button(root,text='',bg='White',fg='Black',width=3,height=1,font=('Helvetica','20'))
b4.grid(row=2,column=6)
b5=Button(root,text='',bg='White',fg='Black',width=3,height=1,font=('Helvetica','20'))
b5.grid(row=2,column=7)
b6=Button(root,text='',bg='White',fg='Black',width=3,height=1,font=('Helvetica','20'))
b6.grid(row=2,column=8)

bn1=Button(root,text='Y',bg='Blue',fg='Black',width=3,height=1,font=('Helvetica','20'),command= lambda:clicked('Y'))
bn1.grid(row=5,column=3)
bn2=Button(root,text='A',bg='Blue',fg='Black',width=3,height=1,font=('Helvetica','20'),command= lambda:clicked('A'))
bn2.grid(row=5,column=4)
bn3=Button(root,text='C',bg='Blue',fg='Black',width=3,height=1,font=('Helvetica','20'),command= lambda:clicked('C'))
bn3.grid(row=5,column=5)
bn4=Button(root,text='N',bg='Blue',fg='Black',width=3,height=1,font=('Helvetica','20'),command= lambda:clicked('N'))
bn4.grid(row=5,column=6)
bn5=Button(root,text='T',bg='Blue',fg='Black',width=3,height=1,font=('Helvetica','20'),command= lambda:clicked('T'))
bn5.grid(row=5,column=7)
bn6=Button(root,text='B',bg='Blue',fg='Black',width=3,height=1,font=('Helvetica','20'),command= lambda:clicked('B'))
bn6.grid(row=5,column=8)
bn7=Button(root,text='R',bg='Blue',fg='Black',width=3,height=1,font=('Helvetica','20'),command= lambda:clicked('R'))
bn7.grid(row=6,column=4)
bn8=Button(root,text='P',bg='Blue',fg='Black',width=3,height=1,font=('Helvetica','20'),command= lambda:clicked('P'))
bn8.grid(row=6,column=5)
bn9=Button(root,text='H',bg='Blue',fg='Black',width=3,height=1,font=('Helvetica','20'),command= lambda:clicked('H'))
bn9.grid(row=6,column=6)
bn10=Button(root,text='D',bg='Blue',fg='Black',width=3,height=1,font=('Helvetica','20'),command= lambda:clicked('D'))
bn10.grid(row=6,column=7)
bn11=Button(root,text='O',bg='Blue',fg='Black',width=3,height=1,font=('Helvetica','20'),command= lambda:clicked('O'))
bn11.grid(row=7,column=5)
bn12=Button(root,text='G',bg='Blue',fg='Black',width=3,height=1,font=('Helvetica','20'),command= lambda:clicked('G'))
bn12.grid(row=7,column=6)

label=Label(root,text="chances remaining are : 6")
label.grid()

root.mainloop()

