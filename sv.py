import tkinter as tk
from PIL import Image, ImageTk
from functools import partial


class LabelEntry(tk.Frame):
    def __init__(self, parent, text, button=None):
        super().__init__(parent)
        self.pack(fill=tk.X)

        lbl = tk.Label(self, text=text, width=14, anchor='w')
        lbl.pack(side=tk.LEFT, padx=5, pady=5)

        if button:
            frame2 = tk.Frame(self)
            frame2.pack(side=tk.LEFT, expand=True)

            entry = tk.Entry(frame2)
            entry.pack(side=tk.LEFT, fill=tk.X, padx=5)

            button.pack(in_=frame2, side=tk.LEFT, padx=5, pady=5)
        else:
            entry = tk.Entry(self)
            entry.pack(side=tk.LEFT, fill=tk.X, padx=5)

        self.entry=entry


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.myLift()


class Page1(Page):
    def myLift(self):
        self.bind_all('<Return>',lambda event: self.keyEnterPressed())
        self.focus_set()
        self.lift()

    def keyEnterPressed(self):
        print ("Page1 Return key pressed")
        self.page2.myLift(self)
    def keyQPressed(self):
        print ("Page1 Q pressed")
        quit()

    def setPage2(self, p2):
        self.page2 = p2;
       
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.root = args[0]

        self.entries = []
        field = "Home TEAM NAME"
        self.entries.append(LabelEntry(self, field))
 
        field = "Visitor TEAM NAME"
        self.entries.append(LabelEntry(self, field))
 
        field = "Quarter"
        self.entries.append(LabelEntry(self, field))
 
        field = "Timer (Minutes)"
        self.entries.append(LabelEntry(self, field))
 
        field = "Timer(Seconds)"
        self.entries.append(LabelEntry(self,field))

        self.bind_all('<q>', lambda event: self.keyQPressed()) 
        self.bind_all('<Return>',lambda event: self.keyEnterPressed())
        self.focus_set()


class Page2(Page):

    def keyEnterPressed(self):
        print ("Page2 Return key pressed")
        self.page1.myLift()
    def keyWPressed(self):
        print ("Page2 W key pressed")
        self.score1 += 1
        self.fin.set(str(self.score1))
    def keySPressed(self):
        print ("Page2 S pressed")
        self.score1 -= 1
        self.fin.set(str(self.score1))
    def keyIPressed(self):
        print ("Page 2 I pressed")
        self.score2 += 1
        self.fin2.set(str(self.score2))
    def keyKPressed(self):
        print ("Page 2 K Pressed")
        self.score2 -= 1
        self.fin2.set(str(self.score2))
    def keyQPressed(self):
        print ("quit p2")
        quit()
    def keyTPressed(self):
        print ("start timer")
        self.startCounter()
    def keyEPressed(self):
        print ("stop timer")
        self.pauseCounter()
    def setPage1(self, p1):
        self.page1 = p1;


    def startCounter(self):
        if not self.is_timer_running:  ## avoid 2 button pushes
            self.is_timer_running=True
            self.decrementCounter()

    def decrementCounter(self):
        if self.is_timer_running:
             self.timer_count = int(self.timer_count) -1

             if self.timer_count > 0:  ## time is not up
                 self.root.after(1000, self.decrementCounter)  ## every second
             else:     ## time is up so exit
                 self.is_timer_running=False
                 print ("TIMES UP!")

             #convert count into min and second
             m, s = divmod(self.timer_count,60)
             print ("count: %d, Min: %d, Sec: %d"%(self.timer_count,m,s))
             strx = str(m) + ":" + str(s)
             self.timer.set(str(strx))

    def pauseCounter(self):
        self.is_timer_running = False


    def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)


       self.root = args[0]
       self.fin = tk.StringVar()
       self.fin2 = tk.StringVar()

       self.fin.set("0")
       self.fin2.set("0")
       self.score1 = 0
       self.score2 = 0
       self.home_name = tk.StringVar()
       self.visitor_name =tk.StringVar()
       self.quarter_time = tk.StringVar()
       self.timer = tk.StringVar()
       self.timer_min = 0
       self.timer_sec = 0 
       self.timer_count= 0

       self.is_timer_running=False  ## timer is or is not running

       image = Image.open("poway2.png")
       image=image.resize((300,300), Image.ANTIALIAS)
       self.my_img = ImageTk.PhotoImage(image)
       poway_logo = tk.Label(self,image=self.my_img)
       poway_logo.grid(row=0, column = 1, sticky ="ew", pady =4)


       home_label = tk.Label(self, textvariable=self.home_name, bg='blue', width= 15, height=2, font=("Arial",50))
       home_label.grid(row=0, column= 0, sticky ="nsew", pady=8)


       visitor_label = tk.Label(self, textvariable=self.visitor_name, bg='green',width= 15, height=2, font=("Arial", 50))
#       visitor_label.grid(row=0, column=2, pady=8)
       visitor_label.grid(row=0, column=2, sticky="nsew", pady=8)

       home_score_label = tk. Label(self, textvariable=self.fin, bg='blue', height=2,  font=("Arial",200))
       home_score_label.grid(row=1, column=0, sticky="nsew", pady=10)

       time_label = tk.Label(self, textvariable=self.timer, bg='grey', font=("Arial",100))
       time_label.grid(row=1, column=1, sticky="ew", pady=8)

       visitor_score_label = tk.Label(self, textvariable=self.fin2, bg='green',height=2,  font=("Arial", 200))
       visitor_score_label.grid(row=1, column=2, sticky="nsew", pady=10)

       game_time_label = tk.Label(self, text=self.timer, bg='grey', font=("Arial",100))
       game_time_label.grid(row=2, column=1, sticky="ew", pady=8)

       quarter_label = tk.Label(self, textvariable = self.quarter_time, bg='grey', font=("Arial",100))
       quarter_label.grid(row=2, column=1, sticky="ew", pady=8)




       self.bind_all('<Return>',lambda event: self.keyEnterPressed())
       self.bind_all('<w>',lambda event: self.keyWPressed())
       self.bind_all('<s>', lambda event: self.keySPressed())
       self.bind_all('<i>', lambda event: self.keyIPressed())
       self.bind_all('<k>', lambda event: self.keyKPressed())
       self.bind_all('<q>', lambda event: self.keyQPressed())
       self.bind_all('<t>', lambda event: self.keyTPressed())
       self.bind_all('<e>', lambda event: self.keyEPressed())
       self.focus_set()




    def myLift(self,p1):
        print("here")
        s = p1.entries[1].entry.get()
        print("entry0 %s"%s)
        self.visitor_name.set(str(s))

        a = p1.entries[0].entry.get()
        self.home_name.set(str(a))

        d = p1.entries[2].entry.get()
        self.quarter_time.set(str(d))
        
        m = p1.entries[3].entry.get()
        if (m==""): self.timer_min = 0
        else: self.timer_min=int(m)

        s = p1.entries[4].entry.get()
        if (s==""): self.timer_sec = 0
        else:self.timer_sec= int(s)

        print ("Min(%s) Sec(%s)"%(m,s))
        
        self.timer_count= self.timer_min*60 +self.timer_sec 

        strx = m + ":" + s
        self.timer.set(str(strx))

        self.bind_all('<Return>',lambda event: self.keyEnterPressed())
        self.focus_set()
       
        self.lift()


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        p1 = Page1(self)
        p2 = Page2(self)

        p1.setPage2(p2)
        p2.setPage1(p1)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)        

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    width = root.winfo_screenwidth()
    height =  root.winfo_screenheight()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry('%dx%d'%(width,height))
    root.mainloop()
