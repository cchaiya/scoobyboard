from tkinter import *


class CountDownTimer():
    def __init__(self, root, init_min, init_sec):
        self.root=root
        self.font = ("Atrial",24)

        self.min = IntVar()
        self.min.set(init_min)

        self.sec = IntVar()
        self.sec.set(init_sec)

        self.is_running=False  ## timer is or is not running
        self.count=IntVar()

        # count is in second .. convert init_min and init_sec into second
        self.count.set(init_min*60+init_sec) # initialized the count 

        #count_tf=Entry(root, width=3, font =self.font, textvariable=self.count)
        #count_tf.grid(row=1, column=0, columnspan=2, sticky="ew")

        min_tf=Entry(root, width=3, font =self.font, textvariable=self.min)
        #min_tf.grid(row=5, column=0, columnspan=1, sticky="ew")
        min_tf.place(x=40,y=5)

        colon_tf=Label(root,width=3,font=self.font,text=":  ")
        colon_tf.place(x=80,y=5)

        sec_tf=Entry(root, width=3, font =self.font, textvariable=self.sec)
        sec_tf.place(x=120,y=5)

        Button(root, text="Start", fg="blue", width=15,
                            command=self.startit).place(x=0,y=50)
        Button(root, text="Pause", fg="red", width=15,
                            command=self.pauseit).place(x=100,y=50)
        Button(self.root, text="Quit", bg="orange",
                            command=self.root.quit).place(x=80,y=100)

    def startit(self):
        if not self.is_running:  ## avoid 2 button pushes
            self.is_running=True
            self.count.set( self.min.get() * 60 + self.sec.get())
            self.decrement_counter()

    def decrement_counter(self):
        if self.is_running:
             c=self.count.get() -1
             self.count.set(c)
             if c > 0:  ## time is not up
                 self.root.after(1000, self.decrement_counter)  ## every second
             else:     ## time is up so exit
                 self.is_running=False
                 Label(root, text="Time Is Up", font=('DejaVuSansMono', 14, "bold"),
                 bg="red").grid(row=5, column=0, columnspan=2, sticky="ew")

             #convert count into min and second
             m, s = divmod(c,60)
             self.min.set(m)
             self.sec.set(s)

    def pauseit(self):
        self.is_running = False

root = Tk()
TT=CountDownTimer(root,1,2)
root.mainloop()
