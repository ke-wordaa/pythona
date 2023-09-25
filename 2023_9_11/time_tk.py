from tkinter import *
import time,os,math
root = Tk()
root.title("main")
root.geometry("200x200")
time_le= Label(root,text="時間計時",font=((""),(30)))
time_le.pack()
i = 0
s=False
def mytime():
    global i,s
    minn =60
    if s== True:
        i += 1
        a=math.trunc(i/minn)
        b= i%minn
        print(a,b)
        time_le_text['text']="%s分%s秒" %(a,b)
        root.after(1000,mytime)
    else:
        time_le_text['text']="%s分%s秒" %(0,0)
def bt_1_f():
    global s
    if s==True:
        bt_1['text']="開始計時"
        s=False
        mytime()
    else:
        bt_1['text']="停止計時"
        s=True
        mytime()

time_le_text= Label(root,text="",font=((""),(30)))

time_le_text.pack()
bt_1= Button(root,text="開始計時",font=((""),(30)),command=bt_1_f)
bt_1.pack()
root.mainloop()
