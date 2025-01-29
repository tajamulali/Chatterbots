from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk


class GigiBot:
    def __init__(self,root):
        self.root = root
        self.root.title("GigiBot")
        self.root.geometry("600x600+0+0")
        self.root.bind('<Return>',self.enter_func)


        main_frame = Frame(self.root,bd=4,bg='powder blue',width=500)
        main_frame.pack()

        img_chat = Image.open('images/chat.png')
        img_chat = img_chat.resize((200,70),Image.LANCZOS)
        self.picture = ImageTk.PhotoImage(img_chat)

        title_lbl = Label(main_frame,bd=3,relief=RAISED,anchor=('nw'),width=600,compound=LEFT ,image=self.picture,text='CHAT WITH ME',font=('arial',30,'bold'),fg='green',bg='white')
        title_lbl.pack(side=TOP)

        self.scroll_y = ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text = Text(main_frame,width=50,height=18,bd=3,relief=RAISED,font=('arial,14'),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()


        btn_frame = Frame(self.root,bd=4,bg='white',width=600)
        btn_frame.pack()

        label = Label(btn_frame,text="Say Something",font=('arial',12,'bold'),fg='green',bg='white')
        label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        self.entry=StringVar()
        self.entry1 = ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=('Times new roman',13,'italic'))
        self.entry1.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        self.send = Button(btn_frame,text="Send>>",command=self.send,font=('arial',8,'bold'),width=8,bg='powder blue')
        self.send.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        self.clear = Button(btn_frame,text="Clear Data",command=self.clear,font=('arial',8,'bold'),width=8,bg='red',fg='white')
        self.clear.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        self.msg=''
        self.label1 = Label(btn_frame,text=self.msg,font=('arial',12,'bold'),fg='skyblue',bg='white')
        self.label1.grid(row=1,column=1,padx=5,pady=5,sticky=W)



    # _________________Function Declaration___________________________

    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')
    
    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')


    def send(self):
        send = '\t\t'+'You: '+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)

        if (self.entry.get()==''):
            self.msg='Please enter some input'
            self.label1.config(text=self.msg,fg='skyblue')
        else:
            self.msg=''
            self.label1.config(text=self.msg,fg='skyblue')

        if(self.entry.get()=='hi'):
            self.text.insert(END,'\n\n'+'Gigi: hello')




if __name__ == '__main__':
    root = Tk()
    obj = GigiBot(root)
    root.mainloop()