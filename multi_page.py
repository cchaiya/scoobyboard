import tkinter as tk
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       test_label = tk.Label(self, text='HOME TEAM NAME', bg='blue', font=("Arial", 50))
       test_label.pack(side="top",fill="both", expand=True)

       test_label2 = tk.Label(self, text='OPPONENT TEAM NAME', bg='green', font=("Arial",50))
       test_label2.pack(side="top", fill="both", expand=True)

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       home_label = tk.Label(self, text='HOME', bg='blue', font=("Arial",50))
       home_label.pack(side="top", fill="both", expand=True)

       home_score_label = tk. Label(self, text='score', bg='blue', font=("Arial",50))
       home_score_label.pack(side="top", fill="both", expand=True)

       time_label = tk.Label(self, text="Time", bg='blue', font=("Arial",50))
       time_label.pack(side="top", fill="both", expand =True)

       game_time_label = tk.Label(self, text='4:23', bg='grey', font=("Arial",50))
       game_time_label.pack(side="top", fill="both", expand =True)

       quarter_label = tk.Label(self, text='3rd', bg='grey', font=("Arial",50))
       quarter_label.pack(side="top", fill="both", expand =True)

       visitor_label = tk.Label(self, text='Visitor', bg='green', font=("Arial", 50))
       visitor_label.pack(side="top", fill="both", expand=True)

       visitor_score_label = tk.Label(self, text='score', bg='green', font=("Arial", 50))
       visitor_score_label.pack(side="top", fill="both", expand=True)
class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)        

        b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)        

        b1.pack(side="left")
        b2.pack(side="left")        

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("800x800")
    root.mainloop()
