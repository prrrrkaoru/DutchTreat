import tkinter 
from PIL import Image, ImageTk

class Treat():
    def __init__(self, master):
        self.master = master
        self.sv_list = []
        self.entry_list = []
        self.name_labels = [] 
        self.new_entries = [] 
        self.yen_labels = []  
        self.amount_entries = []

        self.createWidgets()
    
    def createWidgets(self):
        self.im = ImageTk.PhotoImage(file="../data/title.png")

        self.frame = tkinter.Frame(
            self.master,
            width=1000,
            height=400
        )
        self.frame.pack()

        self.image = tkinter.Canvas(
            self.frame,
            width=800,
            height=400
        )
        self.image.pack()
        self.image.create_image(400, 200, image=self.im)

        self.ex = tkinter.Label(
            self.master,
            text='名前を入力してください'
        )
        self.ex.pack()

        self.button1 = tkinter.Button(
            self.master,
            text="メンバーを追加",
            command=self.Add
        )
        self.button1.pack(side=tkinter.LEFT, padx=5)

        self.button2 = tkinter.Button(
            self.master,
            text="メンバーを確定",
            command=self.Money
        )
        self.button2.pack(side=tkinter.LEFT, padx=5)

        self.Add()

    def Add(self):
        self.sv = tkinter.StringVar()
        self.sv_list.append(self.sv)

        self.entry = tkinter.Entry(
            self.master,
            width=30,
            bd=3,
            textvariable=self.sv
        )
        self.entry.pack()
        self.entry_list.append(self.entry)

    def Money(self):
        self.ex.destroy()
        self.button1.destroy()
        self.button2.pack_forget()

        total_sum = 0
        amounts = []

        for self.entry in self.amount_entries:
            self.amount = int(self.entry.get())
            total_sum += amount
            amounts.append(amount)
        
        for self.entry in self.entry_list:
            self.entry.destroy()

        for self.sv in self.sv_list:
            self.frame = tkinter.Frame(self.master)
            self.frame.pack()

            self.name_label = tkinter.Label(
                self.frame,
                text=self.sv.get() + 'さんが'
            )
            self.name_label.pack()
            self.name_labels.append(self.name_label)

            self.new_entry = tkinter.Entry(
                self.frame,
                width=10,
                bd=3
            )
            self.new_entry.pack()
            self.new_entries.append(self.new_entry)

            self.yen_label = tkinter.Label(
                self.frame,
                text='円払いました\n--------------------------------'
            )
            self.yen_label.pack()
            self.yen_labels.append(self.yen_label)


        self.button2.config(
            text='お会計',
            command=self.Bill
        )
        self.button2.pack()

    def Bill(self):
        zipped = zip(self.sv_list, self.new_entries)

        self.total3 = 0
        self.count = len(self.new_entries)

        for self.entry in self.new_entries:
            self.total1 = self.entry.get()
            self.total2 = int(self.total1)
            self.total3 += self.total2

        self.base = self.total3/self.count

        self.total4 = tkinter.Label(
            self.frame,
            text='総額は'+str(self.total3)+'円です\n一人当たり'+str(self.base)+'円です'
        )
        self.total4.pack()

        for self.sv, self.entry in zip(self.sv_list, self.new_entries):
            self.difference = self.base - int(self.entry.get())
            self.order = tkinter.Label(
                self.frame,
                text=self.sv.get()+'さんの差額は'+str(self.difference)+'円です'
            )
            self.order.pack()
        



        self.button2.config(
            text='会計終了',
            command=self.master.destroy
        )
        self.button2.pack()
        for self.label in self.name_labels:
            self.label.destroy()
        for self.entry in self.new_entries:
            self.entry.destroy()
        for self.label in self.yen_labels:
            self.label.destroy()

if __name__ == '__main__':
    app = tkinter.Tk()
    treat = Treat(app)
    app.mainloop()
