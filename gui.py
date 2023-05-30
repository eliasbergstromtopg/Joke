from tkinter import *
import jokehandler

jokehand = jokehandler.Jokehandler("https://v2.jokeapi.dev/joke/Any?type=single")

root = Tk()
root.title("Jokes")

#Fixar storlek på fönster
root.geometry("1000x400")


#Skapar textfält
textbox = Text(root, height=10, width=100, font="Helvetica", fg="green")
#Skapar label
header = Label(root, text="Dagens Skämt!")
header.config(font=("Helvetica", 14))


def clickButton():
    textbox.delete("1.0", "end")
    t_joke = jokehand.get_joke()
    textbox.insert(INSERT, t_joke)

button_getjoke = Button(text="Hämta Skämt", padx=6, pady=6, command=clickButton)
button_avsluta = Button(root, text="Avsluta", padx=6 , pady=6, command=root.destroy)


header.pack()
textbox.pack()
button_getjoke.pack()
button_avsluta.pack()


root.mainloop()