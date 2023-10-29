import tkinter as tk
import random


words = ["start", "begin", "introduce", "initiate", "commence", "ommencement day",
        "Graduation day", "set off", "kick off", "embark on", "count", "abel", "countless",
        "priceless", "equipment", "tube", "decode", "digestive""solution", "motivation", "decoration",
        "entertainment", "unity", "penalty", "reality", "safety", "poverty", "goodness", "badness",
        "sickness", "awarness", "importance", "differance", "apperance", "significance", "helth",
        "growth", "death", "length", "wealth", "tourism", "racism", "mechanism", "sexism",
        "capitalism", "actor", "artist", "carpenter", "musician", "physician", "assistant"
        "revision", "decision", "argvment", "tournament",]


def show_output():
        random_words = random.choice(words)
        output = random_words
        output_lable.config(text=output)
        output_lable.config(font="Verdana 45")
        output_lable.config(bg="HotPink")


app = tk.Tk()
app.title('จำได้รึเปล่าจ๊ะ')
app.minsize(width= 650, height=400)

title_lable = tk.Label(app, text='Meaning of this word is...', fg="DeepSkyBlue2", font="Fixedsys 20")
title_lable.pack(pady=20)

random_buttom = tk.Button(app, text='Go!!!',command=show_output)
random_buttom.pack(pady=20)

output_lable = tk.Label(app)
output_lable.pack(pady=20)

app.mainloop()