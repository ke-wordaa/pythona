from tkinter import *
import time,os
root = Tk()
root.title("main")
root.geometry("200x200")
time_le= Label(root,text="時間計時",font=((""),(30)))
time_le.pack()
def mytime():
    i = 0
    minn =60
    os.system("cls")
    os.system("color a")
    print("計時開始!")
    while True:
        i += 1
        if i % minn == 0:
            mina = int(i/ minn)
            print(mina,"分鐘")
            time_le_text['text']=mina,"分鐘"
        else:
            time_le_text['text']=i
            print(i)
        time.sleep(1)
time_le_text= Label(root,text="",font=((""),(30)))
time_le_text.pack()
root.mainloop()
mytime()
