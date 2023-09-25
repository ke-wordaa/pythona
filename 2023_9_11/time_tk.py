from tkinter import *
import time,os,math
root = Tk()
root.title("main")
root.geometry("300x400")
time_le= Label(root,text="時間計時",font=((""),(30)))
time_le.pack()
i = 0
start_c=False
stop= False
minn =60
def mytime():
    global i,start_c,minn,stop
    if start_c== True:
        a=math.trunc(i/minn)
        b= i%minn
        if stop ==True:
            time_le_text['text']="%s分%s秒" %(a,b)
            start_c=False
            stop= False
            bt_start['text']="開始計時"
            start_c=False
            i=0
        else:
            i += 1
        print(a,b)
        time_le_text['text']="%s分%s秒" %(a,b)
        root.after(1000,mytime)
       
def start():
    global start_c
    if start_c==True:
        time_le_text['text']="%s分%s秒" %(0,0)
        bt_start['text']="開始計時"
        start_c=False
        mytime()
    else:
        bt_start['text']="停止計時"
        start_c=True
        mytime()
        bt_stop['state']=NORMAL
def stop_but():
    global stop
    bt_stop['state']=DISABLED
    stop= True 
    mytime()
time_le_text= Label(root,text="",font=((""),(30)))

time_le_text.pack()
bt_start= Button(root,text="開始計時",font=((""),(30)),command=start)
bt_start.pack()
bt_stop= Button(root,text="暫停計時",font=((""),(30)),command=stop_but,state=DISABLED)
bt_stop.pack(pady=20)
bt_quit= Button(root,text="離開",font=((""),(30)),command=quit)
bt_quit.pack(pady=20)
root.mainloop()
