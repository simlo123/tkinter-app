
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from tkinter.ttk import Frame, Label, Entry, Button
class linkMaker(Frame):
  
    def __init__(self):
        super().__init__()   
         
        self.initUI()
    

    def nowyLink(self, nazwa, link1, link2, cena, kupon1, kupon2, kupon3):
         
        if len(kupon2) == 0:
        	return "[{0}]({1}) - z kuponem {2} za {3}$([bezref]({4}))".format(nazwa, link1, kupon1, cena, link2)
        else:
        	if len(kupon3) == 0:
        		return "[{0}]({1}) - z kuponem {2} lub {3} za {4}$([bezref]({5}))".format(nazwa, link1, kupon1, kupon2, cena, link2)
        	else:
        		return "[{0}]({1}) - z kuponem {2} lub {3} lub {4} za {5}$([bezref]({6}))".format(nazwa, link1, kupon1, kupon2, kupon3, cena, link2)

    def cls(self):
    	entry1.delete(0,entry1.get())
    	entry2.delete(0,entry2.get())
    	entry3.delete(0,entry3.get())
    	entry4.delete(0,entry4.get())
    	entry5.delete(0,entry5.get())
    	entry6.delete(0,entry6.get())
    	entry7.delete(0,entry7.get())
    	entry8.delete(0,entry8.get())

    def initUI(self):
      
        self.master.title("app.")
        self.pack(fill=BOTH, expand=True)
        
        frame1 = Frame(self)
        frame1.pack(fill=X)
        
        lbl1 = Label(frame1, text="Nazwa", width=8)
        lbl1.pack(side=LEFT, padx=5, pady=5)           
       
        entry1 = Entry(frame1)
        entry1.pack(fill=X, padx=5, expand=True)
        
        frame2 = Frame(self)
        frame2.pack(fill=X)
        
        lbl2 = Label(frame2, text="Link 1", width=8)
        lbl2.pack(side=LEFT, padx=5, pady=5)        

        entry2 = Entry(frame2)
        entry2.pack(fill=X, padx=5, expand=True)
        
        frame3 = Frame(self)
        frame3.pack(fill=X)
        
        lbl3 = Label(frame3, text="Link 2", width=8)
        lbl3.pack(side=LEFT, padx=5, pady=5)        

        entry3 = Entry(frame3)
        entry3.pack(fill=X, padx=5, expand=True)

        frame4 = Frame(self)
        frame4.pack(fill=X)
        
        lbl4 = Label(frame4, text="Cena", width=8)
        lbl4.pack(side=LEFT, padx=5, pady=5)           
       
        entry4 = Entry(frame4)
        entry4.pack(fill=X, padx=5, expand=True)
         
        frame5 = Frame(self)
        frame5.pack(fill=X)
        
        lbl5 = Label(frame5, text="Kupon 1", width=8)
        lbl5.pack(side=LEFT, padx=5, pady=5)           
       
        entry5 = Entry(frame5)
        entry5.pack(fill=X, padx=5, expand=True)

        frame6 = Frame(self)
        frame6.pack(fill=X)
        
        lbl6 = Label(frame6, text="Kupon 2", width=8)
        lbl6.pack(side=LEFT, padx=5, pady=5)           
       
        entry6 = Entry(frame6)
        entry6.pack(fill=X, padx=5, expand=True)

        frame7 = Frame(self)
        frame7.pack(fill=X)
        
        lbl7 = Label(frame7, text="Kupon 3", width=8)
        lbl7.pack(side=LEFT, padx=5, pady=5)           
       
        entry7 = Entry(frame7)
        entry7.pack(fill=X, padx=5, expand=True)

        frame9 = Frame(self)
        frame9.pack(fill=X)
        
        lbl9 = Label(frame9, text="", width=8)
        lbl9.pack(side=LEFT, padx=5, pady=5)  

 		
        frame8 = Frame(self)
        frame8.pack(fill=X)
        
        lbl8 = Label(frame8, text="Link", width=8)
        lbl8.pack(side=LEFT, padx=5, pady=5)           
       
        entry8 = Entry(frame8)
        entry8.pack(fill=X, padx=5, expand=True)		
       	entry8.insert(0, '')

       	cButton = Button(self, text="Wyczyść", command= lambda: self.cls())
       	cButton.place(x=538, y=205)

        okButton = Button(self, text="OK", 
        	command=lambda: entry8.insert(0, self.nowyLink(entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get(), entry6.get(), entry7.get())))
        okButton.place(x=620, y=205)





def main():
  
    root = Tk()
    root.geometry("700x300+100+100")
    app = linkMaker()
    root.mainloop()  

if __name__ == '__main__':
    main()  