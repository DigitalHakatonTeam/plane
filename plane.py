from tkinter import *
from PIL import Image, ImageTk
from threading import Timer
from tkinter.messagebox import *
import random
import time
root = Tk()
class C:
    a = 0
    b = 0
    z = 0
    f = 0
    counter = 0
    currenttime = time.time()
    string = ""
arr = ['k5.bmp','k6.bmp','k7.bmp','k8.bmp']
for i in arr:
    img = Image.open(i)
    resized_img = img.resize((800, 500), Image.ANTIALIAS)
    resized_img.save(i)
C.a = random.randrange(1, 800)
C.b = random.randrange(1, 500)
img = [ImageTk.PhotoImage(Image.open(arr[0])),ImageTk.PhotoImage(Image.open(arr[1])),ImageTk.PhotoImage(Image.open(arr[2])),ImageTk.PhotoImage(Image.open(arr[3]))]
plane = ImageTk.PhotoImage(Image.open('plane_1.png'))
canvas = Canvas(root,width=800,height=500)
but = Button(root,text="Next")
var=StringVar()
var.set(0)
lab = Label(root, textvariable=var)
canvas.grid(row = 0, column = 0,rowspan = 3)
but.grid(row = 0, column = 1)
lab.grid(row = 1, column = 1)
class perpetualTimer():
   def __init__(self,t,hFunction):
      self.t=t
      self.hFunction = hFunction
      self.thread = Timer(self.t,self.handle_function)

   def handle_function(self):
      self.hFunction()
      self.thread = Timer(self.t,self.handle_function)
      self.thread.start()

   def start(self):
      self.thread.start()

   def cancel(self):
      self.thread.cancel()

def printer():
    while(C.counter < 15):
        C.z = time.time() - C.currenttime
        var.set("%.3f" % C.z)
t = perpetualTimer(0,printer)
t.start()
canvas.create_image(0,0,image=img[C.a%4], anchor = NW)
canvas.create_image(C.a,C.b,image=plane, anchor = NW)

def on_click(event):
    if event.x >= C.a and event.y >= C.b and event.x <= C.a + 17 and event.y <= C.b + 17:
        C.currenttime = time.time()
        canvas.delete("all")
        C.a = random.randrange(1, 800)
        C.b = random.randrange(1, 500)
        canvas.create_image(0, 0, image=img[C.a%4], anchor=NW)
        canvas.create_image(C.a, C.b, image=plane, anchor=NW)
        C.f = C.f + 1
        C.string += "Під час спроби №" + str(C.f) + " Літачок була знайдено за " + str("%.2f" % C.z) + " сек\n"
        C.counter = C.counter + 1
        C.z = 0
        if C.counter > 14:
            t.cancel()
            showinfo("Conclusion", C.string)
def on_click_listener(event):
    C.currenttime = time.time()
    canvas.delete("all")
    C.a = random.randrange(1, 800)
    C.b = random.randrange(1, 500)
    canvas.create_image(0, 0, image=img[C.a%4], anchor=NW)
    canvas.create_image(C.a, C.b, image=plane, anchor=NW)
    C.f = C.f + 1
    C.string += "Під час спроби №" + str(C.f) + " користувач так і не знайшов літачок за " + str("%.2f" % C.z) + " сек\n"
    C.counter = C.counter + 1
    C.z = 0
    if C.counter > 14:
        t.cancel()
        showinfo("Conclusion", C.string)
canvas.bind('<1>', on_click)
but.bind('<1>', on_click_listener)
root.minsize(width=1000, height=500)
root.maxsize(width=1000, height=500)
root.mainloop()
