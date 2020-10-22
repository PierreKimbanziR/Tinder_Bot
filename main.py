from tkinter import *
from tkinter import messagebox
from tinderbot import AutoTinder
from tkinter import font

class Interface():

    def __init__(self, root):
        self.WIDTH = 400
        self.HEIGHT = 150
        self.FONT = font.Font(family="Serif")
        self.TITLE_FONT = font.Font(family="Serif", weight ="bold", size =15)
        self.canvas = Canvas(root, width=self.WIDTH, height=self.HEIGHT)
        self.frame = Frame(root, bg='#fd267d')

        self.title = Label(self.frame, text='Find love today', bg ='#fd267d', fg='white', font =self.TITLE_FONT)

        self.label_mail = Label(self.frame, text='Email', bg="#fd267d", fg='white', font = self.FONT)
        self.label_password = Label(self.frame, text='Password', bg="#fd267d", fg='white', font=self.FONT)


        self.input_email = Entry(self.frame)
        self.input_password = Entry(self.frame)
        self.b = Button(self.frame, text="Submit",font = self.FONT, command=self.launcher)


    def let_canvas(self):
        self.canvas.grid()

    def let_frame(self):
        self.frame.place(relwidth=1, relheight=1)

    def let_title(self):
        self.title.grid(row=2, column=1)

    def let_labels(self):
        self.label_mail.grid(row=4, column=1)
        self.label_password.grid(row=5, column=1)

    def let_input_email(self):
        self.input_email.grid(row=4, column=2)
        self.input_password.grid(row=5, column=2)

    def let_button(self):
        self.b.grid(row=7, column=1)

    def create_ui(self):
        self.let_canvas()
        self.let_frame()
        self.let_title()
        self.let_labels()
        self.let_input_email()
        self.let_button()


    def launcher(self):
        bot = AutoTinder(self.input_email.get(), self.input_password.get())
        return bot.tinder()

def main():
    root = Tk()
    bot_ui = Interface(root)
    bot_ui.create_ui()
    root.mainloop()

if __name__ == "__main__":
    main()