import tkinter as tk
from PIL import Image, ImageTk
from functools import partial


HOME_TEAM_NAME_INDEX = 0
VISITOR_TEAM_NAME_INDEX = 1
CHUKKER_INDEX = 2
TIME_MIN_INDEX = 3
TIME_SEC_INDEX = 4

INIT_CHUKKER = 1
INIT_MIN_IN_A_CHUKKER = 7
INIT_SEC_IN_A_CHUKKER = 30 

class LabelEntry(tk.Frame):

    def onlyNumbers(self, char):
        return char.isdigit()

    def __init__(self, parent, text, button=None, validate_num=False):
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

            if (validate_num):
                vcmd = self.register(self.onlyNumbers)
                entry = tk.Entry(self,
                        validate="key",validatecommand=(vcmd,'%S'))
            else: entry = tk.Entry(self)
            entry.pack(side=tk.LEFT, fill=tk.X, padx=5)

        self.entry=entry


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.myLift()


class Page1(Page):

    def bindKeys(self):
        self.bind_all('<F1>', lambda event: self.keyF1Pressed()) 
        self.bind_all('<Escape>', lambda event: self.keyESCPressed()) 
        self.bind_all('<Return>',lambda event: self.keyEnterPressed())

    def myLift(self):
        print ("Page1 lift")
        self.bindKeys()

        #set focus
        self.entries[0].entry.focus() 

        self.lift()

    def keyEnterPressed(self):

        print ("Page1 Return key pressed")
        # move focus to next label
        if (self.current_focus_index >= (len(self.entries)-1)):
            self.current_focus_index = 0
        else: 
            self.current_focus_index +=1 

        self.entries[self.current_focus_index].entry.focus() 

    def keyESCPressed(self):
        print ("Page1 ESC pressed")
        self.page2.myLift(self)

    def keyF1Pressed(self):
        print ("Page1 F1 pressed")
        quit()

    def setPage2(self, p2):
        self.page2 = p2;
       
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.root = args[0]

        # current_focus_index = current focused entry.  Move to next by hitting
        # return key 
        self.current_focus_index = 0

        self.entries = []
        field = "Home TEAM NAME"
        self.entries.append(LabelEntry(self, field))
 
        field = "Visitor TEAM NAME"
        self.entries.append(LabelEntry(self, field))
 
        field = "Chukker"
        l = LabelEntry(self, field, validate_num=True)
        l.entry.insert(0,str(INIT_CHUKKER))
        self.entries.append(l)
 
        field = "Timer (Minutes)"
        l = LabelEntry(self, field, validate_num=True)
        l.entry.insert(0,str(INIT_MIN_IN_A_CHUKKER))
        self.entries.append(l)

        field = "Timer(Seconds)"
        l = LabelEntry(self, field, validate_num=True)
        l.entry.insert(0,str(INIT_SEC_IN_A_CHUKKER))
        self.entries.append(l)

class Page2(Page):

    # copy current timer to F1 since Page2 might be updated
    def backToPage1(self) :

        # need to delete before insert the value
        self.page1.entries[CHUKKER_INDEX].entry.delete(0,tk.END)
        print ("Chukker %d"%(self.chukker.get()))
        self.page1.entries[CHUKKER_INDEX].entry.insert(0,str(self.chukker.get()))

        m, s = divmod(self.timer_count,60)
        self.page1.entries[TIME_MIN_INDEX].entry.delete(0,tk.END)
        self.page1.entries[TIME_MIN_INDEX].entry.insert(0,str(m))
        self.page1.entries[TIME_SEC_INDEX].entry.delete(0,tk.END)
        self.page1.entries[TIME_SEC_INDEX].entry.insert(0,str(s))
        self.page1.myLift()


    def keyEscapePressed(self):
        print ("Page2 Escape key pressed")
        # stop the counter before switching to page 1 
        self.is_timer_running=False
        self.backToPage1()

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
    def keyF1Pressed(self):
        print ("Page 2 F1 Pressed")
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

    def _popupDestroy(self):

        # increment chukker and reset timer before destroy popup
        if (self.chukker.get() < 3):
            self.chukker.set(str(self.chukker.get()+1)) 

            print ("new Chukker %d"%(self.chukker.get()))
            self.timer_min = INIT_MIN_IN_A_CHUKKER
            self.timer_sec =INIT_SEC_IN_A_CHUKKER
            self.timer_count= self.timer_min*60 +self.timer_sec 

            strx = str(self.timer_min) + ":" + str(self.timer_sec)
            self.timer.set(str(strx))

        self.popup.destroy()

    def _popupCallBack(self,event):
        self._popupDestroy()


    def timesUpPopUp(self):
        self.popup = tk.Tk()
        label= tk.Label(self.popup, text="TIMES UP !", font=("Arial",100),
                    bg='#f00', fg='#fff')
        label.pack(side="top", fill="x", pady=10)
        self.popup.bind ('<Return>',self._popupCallBack)
        self.popup.bind ('<Escape>',self._popupCallBack)
        self.popup.mainloop()


    def decrementCounter(self):
        if self.is_timer_running:
             self.timer_count = int(self.timer_count) -1

             if self.timer_count > 0:  ## time is not up
                self.root.after(1000, self.decrementCounter)  ## every second

             #convert count into min and second
             m, s = divmod(self.timer_count,60)
             print ("count: %d, Min: %d, Sec: %d"%(self.timer_count,m,s))
             strx = str(m) + ":" + str(s)
             self.timer.set(str(strx))

             if (self.timer_count ==0) :     ## time is up so exit
                self.is_timer_running=False
                self.timesUpPopUp()

    def pauseCounter(self):
        self.is_timer_running = False

    def bindKeys(self):
        self.bind_all('<Escape>',lambda event: self.keyEscapePressed())
        self.bind('<w>',lambda event: self.keyWPressed())
        self.bind('<s>', lambda event: self.keySPressed())
        self.bind('<i>', lambda event: self.keyIPressed())
        self.bind('<k>', lambda event: self.keyKPressed())
        self.bind('<t>', lambda event: self.keyTPressed())
        self.bind('<e>', lambda event: self.keyEPressed())
        self.bind('<F1>', lambda event: self.keyF1Pressed())

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
        self.chukker = tk.IntVar()
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
#        visitor_label.grid(row=0, column=2, pady=8)
        visitor_label.grid(row=0, column=2, sticky="nsew", pady=8)
    
        home_score_label = tk. Label(self, textvariable=self.fin, bg='blue', height=2,  font=("Arial",200))
        home_score_label.grid(row=1, column=0, sticky="nsew", pady=10)
    
        time_label = tk.Label(self, textvariable=self.timer, bg='grey', font=("Arial",100))
        time_label.grid(row=1, column=1, sticky="ew", pady=8)
    
        visitor_score_label = tk.Label(self, textvariable=self.fin2, bg='green',height=2,  font=("Arial", 200))
        visitor_score_label.grid(row=1, column=2, sticky="nsew", pady=10)
    
        game_time_label = tk.Label(self, text=self.timer, bg='grey', font=("Arial",100))
        game_time_label.grid(row=2, column=1, sticky="ew", pady=8)
    
        chukker_label = tk.Label(self, textvariable = self.chukker, bg='grey', font=("Arial",100))
        chukker_label.grid(row=2, column=1, sticky="ew", pady=8)
    
    
        self.bindKeys()
    
    def myLift(self,p1):
        print("page2 lift")
        s = p1.entries[VISITOR_TEAM_NAME_INDEX].entry.get()
        self.visitor_name.set(str(s))

        a = p1.entries[HOME_TEAM_NAME_INDEX].entry.get()
        self.home_name.set(str(a))

        d = p1.entries[CHUKKER_INDEX].entry.get()
        self.chukker.set(str(d))
        
        m = p1.entries[TIME_MIN_INDEX].entry.get()
        if (m==""): self.timer_min = 0
        else: self.timer_min=int(m)

        s = p1.entries[TIME_SEC_INDEX].entry.get()
        if (s==""): self.timer_sec = 0
        else:self.timer_sec= int(s)

        self.timer_count= self.timer_min*60 +self.timer_sec 

        strx = m + ":" + s
        self.timer.set(str(strx))

        self.bindKeys()
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

        p1.myLift()

if __name__ == "__main__":
    root = tk.Tk()
    width = root.winfo_screenwidth()
    height =  root.winfo_screenheight()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry('%dx%d'%(width,height))
    root.mainloop()
