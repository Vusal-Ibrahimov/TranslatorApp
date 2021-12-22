from tkinter import *
from tkinter import ttk
import googletrans
import textblob

language = googletrans.LANGUAGES
languagev = list(language.values())

pencere = Tk()
pencere.geometry("500x600")
pencere.config(bg="blue")
pencere.title("Translate")


def translate():
    global language
    text_ =text1.get(1.0,END)
    combo2=diller2.get()
    if text_:
        soz=textblob.TextBlob(text_)
        dil = soz.detect_language()
        for i,j in language.items():
            if j == combo2:
                olke_qisaltmasi = i
        soz = soz.translate(from_lang=dil, to=olke_qisaltmasi)
        text2.delete(1.0, END)
        text2.insert(END, soz)
            


image1 = PhotoImage(file = "google_translate_logo.png")
pencere.iconphoto(False,image1)

diller1 = ttk.Combobox(pencere,values=languagev,width=30,height=8 )
diller1.place(x=150,y=20)

text1 =Text(pencere,wrap=WORD,width=60,height=10)
text1.place(x=7,y=50)

diller2 = ttk.Combobox(pencere,values=languagev,width=30,height=8 )
diller2.place(x=150,y=310)

text2 = Text(pencere,wrap=WORD,width=60,height=10)
text2.place(x=7,y=340)

button1 = Button(pencere,text="Translate",font="Verdana 8 italic bold",width=20,height=3,bg="yellow",fg="red",command=translate)
button1.place(x=160,y=240)

pencere.mainloop()