from tkinter import *
import time


project=Tk()
project.title("Symulacja automatu skończonego")
window= Canvas(project)
window.configure(width=600,height=420)
window.configure(bg='black')
winWidth = window.winfo_reqwidth()
winwHeight = window.winfo_reqheight()
posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(window.winfo_screenheight() / 2 - winwHeight / 2)
project.geometry("+{}+{}".format(posRight, posDown))


#Rysowanie diagramu przejsc
window.create_oval(150,50,250,150, outline='white')
window.create_line(50, 100, 130, 100, arrow=LAST, arrowshape=[5,5,5],fill='white')
window.create_text(90, 90, text='START',fill='white')
window.create_line(250, 75, 400, 75, arrow=LAST, arrowshape=[5,5,5],fill='white')
window.create_line(250, 110, 400, 110, arrow=FIRST, arrowshape=[5,5,5],fill='white')
window.create_oval(400,50,500,150,outline='white')
window.create_line(180,150,180,250, arrow=LAST, arrowshape=[5,5,5],fill='white')
window.create_line(220,150,220,250, arrow=FIRST, arrowshape=[5,5,5],fill='white')
window.create_oval(150,250,250,350,outline='white')
window.create_line(250,270,400,270, arrow=LAST, arrowshape=[5,5,5],fill='white')
window.create_line(250,310,400,310, arrow=FIRST, arrowshape=[5,5,5],fill='white')
window.create_oval(400,250,500,350,outline='white')
window.create_line(430,150,430,250,arrow=FIRST, arrowshape=[5,5,5],fill='white')
window.create_line(470,150,470,250,arrow=LAST, arrowshape=[5,5,5],fill='white')
window.create_text(325,65,text='0',fill='white')
window.create_text(325,120,text='1',fill='white')
window.create_text(325,260,text='1',fill='white')
window.create_text(325,320,text='1',fill='white')
window.create_text(170,200,text='1',fill='white')
window.create_text(230,200,text='0',fill='white')
window.create_text(200, 100, text='qo', fill='red')
window.create_text(420,200,text='0',fill='white')
window.create_text(480,200,text='0',fill='white')
window.create_text(200, 100, text='qo',fill='white')
window.create_text(450, 100, text='q1',fill='white')
window.create_text(200, 300, text='q2',fill='white')
window.create_text(450, 300, text='q3',fill='white')
window.create_oval(160,60,240,140,outline='white')
window.pack()


#Fragment, ktory ma za zadanie pokazac, ktory jest aktualnie stan oraz sprawdzac poprawnosc lancucha
entry1 = Entry (window)
entry1.config(bg='green')
window.create_window(320, 370, window=entry1)

def delete_text(self):
        if self.text_id:
            self.__canvas.delete(self.text_id)
            self.text_id = None
def wypisywanie():
    
    napis=entry1.get()
    curstate="q0"
    symbols=['0','1']
    diagram="q0"

    deltafun={
    "q0": ["q1","q2"],
    "q1": ["q3","q0"],
    "q2": ["q0","q3"],
    "q3": ["q1","q2"]
    }

    for symb in napis:
        time.sleep(1)
        window.update()
        window.create_text(200, 100, text='qo',fill='white')
        window.create_text(450, 100, text='q1',fill='white')
        window.create_text(200, 300, text='q2',fill='white')
        window.create_text(450, 300, text='q3',fill='white')
        window.update()

        if symb in symbols:
            curstate=deltafun[curstate][int(symb)]
            if(curstate=="q0"):
                window.create_text(200, 100, text='qo', fill='red')
            elif(curstate=="q1"):
                window.create_text(450, 100, text='q1', fill='red')
            elif(curstate=="q2"):
                window.create_text(200, 300, text='q2', fill='red')
            elif(curstate=="q3"):
                window.create_text(450, 300, text='q3', fill='red')
            window.update()
        else:
            x1=window.create_text(325,150,text="Symbol nie nalezy do alfabetu",fill='white')
            window.after(3000,window.delete,x1)
            break

    if(curstate=="q0" and symb in symbols):
       x2=window.create_text(325,170,text='Automat zaakceptowal ciag',fill='white')
       window.after(3000,window.delete,x2)
    else:
        x3=window.create_text(325,170,text="Automat odrzucil ciag",fill='white')
        window.after(3000,window.delete,x3)       
         
    entry1.delete(0, END)

button1 = Button(text='Rozpocznij', command=wypisywanie)
window.create_window(320, 400, window=button1)
window.pack()
window.mainloop()


