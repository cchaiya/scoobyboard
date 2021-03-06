#!/usr/bin/python3
import os
import tkinter as tk
from PIL import Image, ImageTk
from functools import partial

#these are variable setups. 
HOME_TEAM_NAME_INDEX = 0
VISITOR_TEAM_NAME_INDEX = 1
CHUKKER_INDEX = 2
TIME_MIN_INDEX = 3
TIME_SEC_INDEX = 4
HOME_BG_INDEX = 5
HOME_FG_INDEX = 6
HOME_LOGO_INDEX = 7
VISITOR_BG_INDEX = 8
VISITOR_FG_INDEX = 9
VISITOR_LOGO_INDEX = 10

CHUCKER_MAX =12
INIT_CHUKKER = 1
INIT_MIN_IN_A_CHUKKER = 7
INIT_SEC_IN_A_CHUKKER = 30

#change the green text to any RGB Hex code to change colors.
# You can also set colors as 'black' or 'white'
HOME_FONT_COLOR = 'black'
VISITOR_FONT_COLOR ='black'

#Change the last /filename.png to the name of your image in the
#Team_Logos_PNG file.
HOME_PNG_FILE_NAME = './Team_Logos_PNG/poway1.png'
VISITOR_PNG_FILE_NAME = './Team_Logos_PNG/lakeside1.png'

COLOR_CODE={
     "Red": "#d45047",
     "Blue": "#4750D4",
     "Black": "#0D0D0D",
     "White": "#EDEDED",
     "Yellow":"#F5E82F",
     "Orange":"#ED9128",
     "Green":"#45A348"
}
BG_COLOR_OPTIONS=["Red","Blue", "Black", "White", "Yellow", "Orange", "Green"]

FONT_COLOR = {
     "Black" : "black",
     "White" : "white"
}
FG_COLOR_OPTIONS=["Black","White"]

LOGO = {
     "Poway 1" : "./Team_Logos_PNG/poway1.png",
     "Poway 2" : "./Team_Logos_PNG/poway2.png",
     "Lakeside": "./Team_Logos_PNG/lakeside1.png"
}
LOGO_OPTIONS=["Poway 1","Poway 2", "Lakeside"]

#do not touch.
GREETING_BANNER = """\n
Scoobyboard V1.0\n
git@github.com:cchaiya/scoobyboard.git\n
"""

SHUTDOWN_BANNER= """Are you sure you want to shutdown ?\n
Yes: enter <return>
No : enter <ESC>
"""

class LabelEntry(tk.Frame):

    def onlyNumbers(self, char):
        return char.isdigit()

    def __init__(self, parent, text, label=True,validate_num=False,
                     choices=None):
        super().__init__(parent)
        self.pack(fill=tk.X)

        lbl = tk.Label(self, text=text, width=14, anchor='w')
        lbl.pack(side=tk.LEFT, padx=5, pady=5)


        if choices != None:
            c = tk.StringVar()
            c.set(choices[0])
            drop =  tk.OptionMenu( self , c , *choices )
            drop.pack(side=tk.LEFT, fill=tk.X, padx=5)
            self.entry=drop
            self.choice = c;

        elif label:

            if (validate_num):
                vcmd = self.register(self.onlyNumbers)
                entry = tk.Entry(self,
                        validate="key",validatecommand=(vcmd,'%S'))
            else: entry = tk.Entry(self)
            entry.pack(side=tk.LEFT, fill=tk.X, padx=5)

            self.entry=entry


class Page(tk.Frame): 
    def _popupDestroy(self,event):
        self.quitPopup.destroy()

    def _popupQuit(self,event):
        os.system("sudo shutdown now")

    def quitPopUp(self):
        self.quitPopup = tk.Tk()
        self.quitPopup.title("Quit")
        label= tk.Label(self.quitPopup, text=SHUTDOWN_BANNER,font=("Arial",50),
                    bg='#f00', fg='#fff')
        label.pack(side="top", fill="x", pady=10)

        self.quitPopup.bind ('<Return>',self._popupQuit)
        self.quitPopup.bind ('<Escape>',self._popupDestroy)
        self.quitPopup.mainloop()


    def decrementCounter(self):
        if self.is_timer_running:
             self.timer_count = int(self.timer_count) -1

             if self.timer_count > 0:  ## time is not up
                self.root.after(1000, self.decrementCounter)  ## every second

             #convert count into min and second
             m, s = divmod(self.timer_count,60)
             #print ("count: %d, Min: %d, Sec: %d"%(self.timer_count,m,s))
             strx = "%d:%02d"%(m,s)
             self.timer.set(str(strx))

             if (self.timer_count ==0) :     ## time is up so exit
                self.is_timer_running=False
                self.timesUpPopUp()

    def pauseCounter(self):
        self.is_timer_running = False

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.myLift()


class Page1(Page):

    def bindKeys(self):
        self.bind_all('<Control-q>', lambda event: self.quitPressed())
        self.bind_all('<Escape>', lambda event: self.keyESCPressed())
        self.bind_all('<Return>',lambda event: self.keyEnterPressed())
        self.bind_all('<Control-T>', lambda event: self.shutDown())
        self.bind_all('<Right>', lambda event: self.keyRightPressed())
        self.bind_all('<Left>', lambda event: self.keyLeftPressed())
        self.bind_all('<Down>', lambda event: self.keyEnterPressed())
        self.bind_all('<Up>', lambda event: self.keyUpPressed())

    def myLift(self):
        self.bindKeys()

        #set focus
        self.entries[0].entry.focus()

        self.lift()

    def keyEnterPressed(self):

        # move focus to next label
        if (self.current_focus_index >= (len(self.entries)-1)):
            self.current_focus_index = 0
        else:
            self.current_focus_index +=1

        self.entries[self.current_focus_index].entry.focus()

    def keyUpPressed(self):

        # move focus to next label
        if (self.current_focus_index == 0):
            self.current_focus_index = len(self.entries)-1
        else:
            self.current_focus_index -=1

        self.entries[self.current_focus_index].entry.focus()

    def _nextLeftIndex(self, option_list, cur_option):
        i = option_list.index(cur_option)
        if (i == 0):
           i = len(option_list) -1 
        else:
           i -=1
        return i

    def keyLeftPressed(self):
        if (self.current_focus_index == HOME_BG_INDEX ):
            ind = self._nextLeftIndex(BG_COLOR_OPTIONS, self.home_bg_color.get())
            self.home_bg_color.set(BG_COLOR_OPTIONS[ind])
        elif (self.current_focus_index == HOME_FG_INDEX ):
            ind = self._nextLeftIndex(FG_COLOR_OPTIONS, self.home_fg_color.get())
            self.home_fg_color.set(FG_COLOR_OPTIONS[ind])
        elif(self.current_focus_index == HOME_LOGO_INDEX ):
            ind = self._nextLeftIndex(LOGO_OPTIONS, self.home_logo.get())
            self.home_logo.set(LOGO_OPTIONS[ind])
        elif(self.current_focus_index == VISITOR_BG_INDEX ):
            ind = self._nextLeftIndex(BG_COLOR_OPTIONS, self.visitor_choice.get())
            self.visitor_choice.set(BG_COLOR_OPTIONS[ind])
        elif(self.current_focus_index == VISITOR_FG_INDEX ):
            ind = self._nextLeftIndex(FG_COLOR_OPTIONS, self.visitor_font_color.get())
            self.visitor_font_color.set(FG_COLOR_OPTIONS[ind])
        elif(self.current_focus_index == VISITOR_LOGO_INDEX ):
            ind = self._nextLeftIndex(LOGO_OPTIONS, self.visitor_logo.get())
            self.visitor_logo.set(LOGO_OPTIONS[ind])
        else:
            print ("No choices")

    def _nextRightIndex(self, option_list, cur_option):
        i = option_list.index(cur_option)
        if (i == len(option_list)-1):
           i = 0
        else:
           i +=1
        return i

    def keyRightPressed(self):
        if (self.current_focus_index == HOME_BG_INDEX ):
            ind = self._nextRightIndex(BG_COLOR_OPTIONS, self.home_bg_color.get())
            self.home_bg_color.set(BG_COLOR_OPTIONS[ind])
        elif (self.current_focus_index == HOME_FG_INDEX ):
            ind = self._nextRightIndex(FG_COLOR_OPTIONS, self.home_fg_color.get())
            self.home_fg_color.set(FG_COLOR_OPTIONS[ind])
        elif(self.current_focus_index == HOME_LOGO_INDEX ):
            ind = self._nextRightIndex(LOGO_OPTIONS, self.home_logo.get())
            self.home_logo.set(LOGO_OPTIONS[ind])
        elif(self.current_focus_index == VISITOR_BG_INDEX ):
            ind = self._nextRightIndex(BG_COLOR_OPTIONS, self.visitor_choice.get())
            self.visitor_choice.set(BG_COLOR_OPTIONS[ind])
        elif(self.current_focus_index == VISITOR_FG_INDEX ):
            ind = self._nextRightIndex(FG_COLOR_OPTIONS, self.visitor_font_color.get())
            self.visitor_font_color.set(FG_COLOR_OPTIONS[ind])
        elif(self.current_focus_index == VISITOR_LOGO_INDEX ):
            ind = self._nextRightIndex(LOGO_OPTIONS, self.visitor_logo.get())
            self.visitor_logo.set(LOGO_OPTIONS[ind])
        else:
            print ("No choices")

    def keyESCPressed(self):
        self.page2.myLift(self)

    def quitPressed(self):
        self.quitPopUp()

    def setPage2(self, p2):
        self.page2 = p2;
    def shutDown(self):
        print("terminate")
        quit()

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.root = args[0]

        # current_focus_index = current focused entry.  Move to next by hitting
        # return key
        self.current_focus_index = 0

        # banner
        lbl = tk.Label(self, text=GREETING_BANNER, width=100,
                anchor='w', font=("Arial",30))
        lbl.pack(side=tk.TOP, padx=5, pady=0)

        field = "SETUP"
        LabelEntry(self, field, label=False)

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

        field = "Home Background"
        l = LabelEntry(self, field,  choices=BG_COLOR_OPTIONS)
        self.entries.append(l)
        self.home_bg_color = l.choice

        field = "Home Font Color"
        l = LabelEntry(self, field, choices=FG_COLOR_OPTIONS)
        self.entries.append(l)
        self.home_fg_color = l.choice

        field = "Home Team Logo"
        l = LabelEntry(self, field, choices=LOGO_OPTIONS)
        self.home_logo= l.choice
        self.entries.append(l)

        field = "Visitor Background"
        l = LabelEntry(self, field, choices=BG_COLOR_OPTIONS)
        self.entries.append(l)
        self.visitor_choice= l.choice

        field = "Visitor Font Color"
        l = LabelEntry(self, field, choices=FG_COLOR_OPTIONS)
        self.entries.append(l)
        self.visitor_font_color = l.choice

        field = "Visitor Logo"
        l = LabelEntry(self, field, choices=LOGO_OPTIONS)
        self.visitor_logo= l.choice
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

    def homeScoreUpPressed(self):
        print ("home score up pressed")
        self.score1 += 1
        self.fin.set(str(self.score1))
    def homeScoreDownPressed(self):
        print ("home score down pressed")
        if (self.score1 > 0):
            self.score1 -= 1
        self.fin.set(str(self.score1))
    def visitorScoreUpPressed(self):
        print ("visitor score up pressed")
        self.score2 += 1
        self.fin2.set(str(self.score2))
    def visitorScoreDownPressed(self):
        print ("visitor score down Pressed")
        if (self.score2 > 0):
            self.score2 -= 1
        self.fin2.set(str(self.score2))
    def quitPressed(self):
        print ("quit Pressed")
        self.quitPopUp()
    def timerPressed(self):
        print ("timer pressed")
        #toggle start and pause
        if (self.is_timer_running == True):
            self.pauseCounter()
        else :
            self.startCounter()
    def setPage1(self, p1):
        self.page1 = p1;
    def ShutDown(self):
        print("terminate")
        quit()


    def startCounter(self):
        if not self.is_timer_running:  ## avoid 2 button pushes
            self.is_timer_running=True
            self.decrementCounter()

    def _timesUpPopupDestroy(self,event):

        # increment chukker and reset timer before destroy popup
        if (self.chukker.get() < CHUCKER_MAX):
            self.chukker.set(str(self.chukker.get()+1))

            print ("new Chukker %d"%(self.chukker.get()))
            self.timer_min = INIT_MIN_IN_A_CHUKKER
            self.timer_sec =INIT_SEC_IN_A_CHUKKER
            self.timer_count= self.timer_min*60 +self.timer_sec

            strx = "%d:%02d"%(self.timer_min,self.timer_sec)
            self.timer.set(str(strx))

        self.popup.destroy()

    def _timesUpPopupCallBack(self,event):
        self._timesUpPopupDestroy(event)


    def timesUpPopUp(self):
        self.popup = tk.Tk()
        self.popup.title("timesup")
        label= tk.Label(self.popup, text="TIMES UP !", font=("Arial",50),
                    bg='#f00', fg='#fff')
        label.pack(side="top", fill="x", pady=0)
        self.popup.bind ('<Return>',self._timesUpPopupCallBack)
        self.popup.bind ('<Escape>',self._timesUpPopupCallBack)
        self.popup.mainloop()


    def decrementCounter(self):
        if self.is_timer_running:
             self.timer_count = int(self.timer_count) -1

             if self.timer_count > 0:  ## time is not up
                self.root.after(1000, self.decrementCounter)  ## every second

             #convert count into min and second
             m, s = divmod(self.timer_count,60)
             #print ("count: %d, Min: %d, Sec: %d"%(self.timer_count,m,s))
             strx = "%d:%02d"%(m,s)
             self.timer.set(str(strx))

             if (self.timer_count ==0) :     ## time is up so exit
                self.is_timer_running=False
                self.timesUpPopUp()

    def pauseCounter(self):
        self.is_timer_running = False

    def bindKeys(self):
        self.bind_all('<Escape>',lambda event: self.keyEscapePressed())
        self.bind('<KP_4>',lambda event: self.homeScoreUpPressed())
        self.bind('<KP_1>', lambda event: self.homeScoreDownPressed())
        self.bind('<KP_6>', lambda event: self.visitorScoreUpPressed())
        self.bind('<KP_3>', lambda event: self.visitorScoreDownPressed())
        self.bind('<space>', lambda event: self.timerPressed())
        self.bind('<Control-T>', lambda event: self.ShutDown())
        self.bind('<Control-q>', lambda event: self.quitPressed())

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

        self.home_bg_color = tk.StringVar()
        self.home_bg_color.set("Red")

        self.visitor_choice = tk.StringVar()
        self.visitor_choice.set("Blue")

        self.home_fg_color = tk.StringVar()
        self.home_fg_color.set("Black")


        self.visitor_font_color = tk.StringVar()
        self.visitor_font_color.set("Black")

        self.home_logo = tk.StringVar()
        self.home_logo.set("Poway 1")


        self.visitor_logo = tk.StringVar()
        self.visitor_logo.set("Poway 2")

        self.is_timer_running=False  ## timer is or is not running
    
        image = Image.open(LOGO[self.home_logo.get()])
        image=image.resize((300,300), Image.ANTIALIAS)
        self.my_img = ImageTk.PhotoImage(image)
        self.poway_logo = tk.Label(self,image=self.my_img)
        self.poway_logo.grid(row=0, column = 1, sticky ="ew", pady =0)
    
    
        self.home_label = tk.Label(self, textvariable=self.home_name, bg=COLOR_CODE[self.home_bg_color.get()], width= 12, height=1,fg=FONT_COLOR[self.home_fg_color.get()], font=("Arial",75))
        self.home_label.grid(row=0, column= 0, sticky ="nsew", pady=0)
    
    
        self.visitor_label = tk.Label(self, textvariable=self.visitor_name, bg=COLOR_CODE[self.visitor_choice.get()],width= 12, height=1, font=("Arial", 75), fg=FONT_COLOR[self.visitor_font_color.get()])
        self.visitor_label.grid(row=0, column=2, sticky="nsew", pady=0)
    
        self.home_score_label = tk. Label(self, textvariable=self.fin, bg=COLOR_CODE[self.home_bg_color.get()], height=1,  font=("Arial",450), fg=FONT_COLOR[self.home_fg_color.get()])
        self.home_score_label.grid(row=1, rowspan=3, column=0, sticky="nsew", pady=0)
    
        time_label = tk.Label(self, textvariable=self.timer,width = 4,  bg='grey', font=("Arial",190))
        time_label.grid(row=1, column=1, sticky="ew", pady=0)
    
        self.visitor_score_label = tk.Label(self, textvariable=self.fin2, bg=COLOR_CODE[self.visitor_choice.get()],height=1,  font=("Arial", 450), fg=FONT_COLOR[self.visitor_font_color.get()])
        self.visitor_score_label.grid(row=1, rowspan = 3, column=2, sticky="nsew",  pady=0)
    
        #game_time_label = tk.Label(self, text=self.timer, bg='grey', font=("Arial",100))
        #game_time_label.grid(row=1, column=1, sticky="ew", pady=8)
    
        chukker_label = tk.Label(self, textvariable = self.chukker, bg='grey', font=("Arial",125))
        chukker_label.grid(row=2, column=1, sticky="ew", pady=0)
    
        image = Image.open(LOGO[self.visitor_logo.get()])
        image=image.resize((300,300), Image.ANTIALIAS)
        self.visitor_img = ImageTk.PhotoImage(image)
        self.visitor_l = tk.Label(self,image=self.visitor_img)
        self.visitor_l.grid(row=3, column = 1, sticky ="ew", pady =0)
    
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

        strx = "%d:%02d"%(self.timer_min,self.timer_sec)
        self.timer.set(str(strx))


        self.home_bg_color.set( p1.home_bg_color.get())
        print ("home_bg_color = %s"%self.home_bg_color.get())
        self.home_label.config(bg=COLOR_CODE[self.home_bg_color.get()])
        self.home_score_label.config(bg=COLOR_CODE[self.home_bg_color.get()])

        self.visitor_choice.set( p1.visitor_choice.get())
        self.visitor_label.config(bg=COLOR_CODE[self.visitor_choice.get()])
        self.visitor_score_label.config(bg=COLOR_CODE[self.visitor_choice.get()])

        self.home_fg_color.set(p1.home_fg_color.get())
        self.home_label.config(fg=FONT_COLOR[self.home_fg_color.get()])
        self.home_score_label.config(fg=FONT_COLOR[self.home_fg_color.get()])


        self.visitor_font_color.set(p1.visitor_font_color.get())
        self.visitor_label.config(fg=FONT_COLOR[self.visitor_font_color.get()])
        self.visitor_score_label.config(fg=FONT_COLOR[self.visitor_font_color.get()])

        self.visitor_logo.set(p1.visitor_logo.get())
        image = Image.open(LOGO[self.visitor_logo.get()])
        image=image.resize((300,300), Image.ANTIALIAS)
        self.visitor_img = ImageTk.PhotoImage(image)
        self.visitor_l.configure(image=self.visitor_img)

        self.home_logo.set(p1.home_logo.get())
        image = Image.open(LOGO[self.home_logo.get()])
        image=image.resize((300,300), Image.ANTIALIAS)
        self.my_img = ImageTk.PhotoImage(image)
        self.poway_logo.configure(image=self.my_img)


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
    root.wm_attributes('-fullscreen','true')
    width = root.winfo_screenwidth()
    height =  root.winfo_screenheight()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
   # root.wm_geometry('800x800')   
    root.wm_geometry('%dx%d'%(width,height))
    root.mainloop()
