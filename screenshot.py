import pyautogui
from Tkinter import *
import time
import PIL
import random
class s:
    def __init__(self,root):
        self.t=0
        self.i=0
        self.n=10
        self.root=root
        self.clip = Button(root,text="cshot.",command=self.clipshot)
        self.clip.pack(side=LEFT)
        self.done = Button(root,text="DONE",command=self.dn)
        self.done.pack(side=LEFT)
        self.singleshot = Button(root,text="Capture",command=self.scrshot)
        self.singleshot.pack(side=LEFT)
        self.multipleshot = Button(root,text="MLTC",command=self.mltshot)
        self.multipleshot.pack(side=LEFT)
        self.setinterval = Button(root,text="Delay",command=self.intrvl)
        self.setinterval.pack(side=LEFT)
        self.stop = Button(root,text="SCOUNT.",command=self.setn)
        self.stop.pack(side=LEFT)
        self.ent = Entry(root,width=10,font=("Courier", 10))
        self.ent.pack(side=RIGHT, expand=YES, fill=X)
        self.s=0
    def scrshot(self):
        self.root.attributes('-alpha', 0)
        name=self.ent.get()
        pyautogui.screenshot(name+str(self.i)+".png")
        self.i+=1
        self.root.attributes('-alpha', 1)
    def clipshot(self):
        if self.s==0:
            self.root.attributes('-alpha', 0.6)
            self.root.minsize(20,20)
            self.s+=1
        else:    
            name=self.ent.get()
            self.root.attributes('-alpha', 0)
            print(root.winfo_x(), root.winfo_y(),root.winfo_width(), root.winfo_height())
            left=root.winfo_x()
            top=root.winfo_y()
            width=root.winfo_width()
            im = pyautogui.screenshot(region=(left+8, top+30,width, root.winfo_height()))
            self.root.attributes('-alpha', 0.6)
            im.save(name+str(self.i)+".png")
            self.i+=1
    def dn(self):
        self.root.attributes('-alpha', 1)
        self.s=0
    def mltshot(self):
        self.i=0
        self.root.attributes('-alpha', 0)
        start=True
        while start:
            name=self.ent.get()
            pyautogui.screenshot(name+str(self.i)+".png")
            self.i+=1
            time.sleep(float(self.t))
            if self.i==int(self.n):
                start=False
                self.root.attributes('-alpha', 1)
                
    def setn(self):
        try:
            self.n=self.ent.get()
            self.root.title("Delay: "+str(int(self.t))+"       "+"No Of Scrn-Shots(mltC): "+str(int(self.n)))
        except:
            pass
    def intrvl(self):
        try:
            self.t=self.ent.get()
            self.root.title("Delay: "+str(int(self.t))+"       "+"No Of SCRN-SHOTS (mltC) : "+str(int(self.n)))
        except:
            pass

root = Tk()
app=s(root)    
root.title("Delay: "+str(app.t)+"       "+"No Of Scrn-Shots(mltC): "+str(app.n))
root.mainloop()

