from tkinter import *
from main import mytime
import time 
def gettime():
    get = mytime.timew()
    return(get)
print(gettime())
time.sleep(1)
print(gettime())
# root = Tk()
# root.title("main")
# root.geometry("200x200")
# time_le= Label(root,text="時間計時",font=((""),(30)))
# time_le.pack()
# time_le_text= Label(root,text="",font=((""),(30)))
# time_le_text.pack()
# root.mainloop()
