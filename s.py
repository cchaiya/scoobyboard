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
        self.lift()


class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)


       self.entries = []
       field = "Home TEAM NAME"
       self.entries.append(LabelEntry(self, field))

       field = "Visitor TEAM NAME"
       self.entries.append(LabelEntry(self, field))


#       for field in 'Version', 'Database Name', 'CSV File':
#           if field == 'CSV File':
#               button = tk.Button(text="Browse", command=self.callback)
#               entries.append(LabelEntry(frame, field, button))
#           else:
#               entries.append(LabelEntry(frame, field))

#       test_label = tk.Label(self, text='HOME TEAM NAME', bg='blue', font=("Arial", 50))
#       test_label.pack(side="top",fill="both", expand=True)
#
#       test_label2 = tk.Label(self, text='OPPONENT TEAM NAME', bg='green', font=("Arial",50))
#       test_label2.pack(side="top", fill="both", expand=True)
#

class Page2(Page):
   def myClick(self):
        inputkey = self.key.get()
        print("1" + inputkey)
        if inputkey=="w":
           print("3")
           self.score1 += 1
           self.fin.set(str(self.score1))
        elif inputkey=="s":
           print("4")
           self.score1 -= 1
           self.fin.set(str(self.score1))
        elif inputkey =="i":
           print("6")
           self.score2 += 1
           self.fin2.set(str(self.score2))
        elif inputkey =="k":
           print("7")
           self.score2 -= 1
           self.fin2.set(str(self.score2))
        elif inputkey=="q":
           print("quit")
           quit()
        else:
           print("5")
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       self.fin = tk.StringVar()
       self.fin2 = tk.StringVar()

       self.fin.set("0")
       self.fin2.set("0")
       self.score1 = 0
       self.score2 = 0
       self.home_name = tk.StringVar()
       self.visitor_name =tk.StringVar()


       image = Image.open("poway2.png")
       image=image.resize((150,150), Image.ANTIALIAS)
       self.my_img = ImageTk.PhotoImage(image)
       poway_logo = tk.Label(self,image=self.my_img)
       poway_logo.pack(side="top", fill="both", expand=True)


       home_label = tk.Label(self, textvariable=self.home_name, bg='blue', font=("Arial",50))
       home_label.pack(side="top", fill="both", expand=True)

       home_score_label = tk. Label(self, textvariable=self.fin, bg='blue', font=("Arial",50))
       home_score_label.pack(side="top", fill="both", expand=True)

       time_label = tk.Label(self, text="Time", bg='grey', font=("Arial",50))
       time_label.pack(side="top", fill="both", expand =True)

       game_time_label = tk.Label(self, text='4:23', bg='grey', font=("Arial",50))
       game_time_label.pack(side="top", fill="both", expand =True)

       quarter_label = tk.Label(self, text='3rd', bg='grey', font=("Arial",50))
       quarter_label.pack(side="top", fill="both", expand =True)

       visitor_label = tk.Label(self, textvariable=self.visitor_name, bg='green', font=("Arial", 50))
       visitor_label.pack(side="top", fill="both", expand=True)

       visitor_score_label = tk.Label(self, textvariable=self.fin2, bg='green', font=("Arial", 50))
       visitor_score_label.pack(side="top", fill="both", expand=True)

       self.key = tk.Entry()
       self.key.pack(side="bottom", fill="both", expand=False)

       myButton = tk.Button(self, text=" ", command=self.myClick)
       myButton.pack(side="top", fill="both", expand=True)

   def my_lift(self,p1):
       print("here")
       s = p1.entries[1].entry.get()
       print("entry0 %s"%s)
       self.visitor_name.set(str(s))
       a = p1.entries[0].entry.get()
       self.home_name.set(str(a))

       self.lift()
class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self,p1)


        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)        

        b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Page 2", command=partial(p2.my_lift,p1))
        b1.pack(side="left")
        b2.pack(side="left")        

        image = Image.open("poway1.png")
        image=image.resize((150,150), Image.ANTIALIAS)
        my_img = ImageTk.PhotoImage(image)
        poway_logo = tk.Label(buttonframe,image=my_img)
        poway_logo.pack(side="top", fill="both", expand=True)

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("800x800")
    root.mainloop()
