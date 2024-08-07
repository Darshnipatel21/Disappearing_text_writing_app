from tkinter import *
from threading import Timer


FONT_NAME = "Courier "


class DisappearingTextWritingApp:

    def __init__(self, window):
        self.window = window
        self.window.config(padx=10, pady=10, background="#FFCBCB")
        self.window.title('Disappearing text writing App')
        self.createWidgets()

    def createWidgets(self):
        Intro_frame = Frame(self.window, highlightbackground="#102C57", highlightcolor="gray80",
                            highlightthickness=1,
                            bd=0, bg='#FFCBCB')
        Intro_frame.grid(row=0, sticky="nsew")

        self.intro = Label(Intro_frame,
                           text=f"Disappearing Text Writing App", justify="center",
                           font=(FONT_NAME, 20, "bold"),
                           foreground="#102C57", background="#FFCBCB", width=50)
        self.intro.grid(column=1, row=1, columnspan=20)
        self.intro.grid_configure(padx=10, pady=5)

        self.intro = Label(Intro_frame,
                           text=f"Don’t stop writing, or all progress will be lost.", justify="center",
                           font=(FONT_NAME, 10, "italic"),
                           foreground="#102C57", background="#FFCBCB", width=50)
        self.intro.grid(column=1, row=2, columnspan=20)
        self.intro.grid_configure(padx=10, pady=5)

        Para_frame = Frame(self.window, highlightbackground="#102C57", highlightcolor="#102C57",
                           highlightthickness=1,
                           bd=0, bg='#FFCBCB')
        Para_frame.grid(row=2, sticky="nsew")
        Para_frame.grid_configure(pady=10)

        self.write = Text(Para_frame, font=(FONT_NAME, 13, "normal"), border="0", foreground="#003C43",
                          background="#FFCBCB", width=100, height=20)
        self.write.grid(column=1, row=3, columnspan=10)
        self.write.grid_configure(padx=5, pady=5)
        self.write.bind("<KeyPress>", self.on_key_press)

        self.reset_btn = Button(Para_frame, text='Reset', fg="#FFCBCB", bg="#003C43", font=FONT_NAME, border=0,
                           command=self.user_inactive, width=40)
        self.reset_btn.grid(column=1, row=5, columnspan=5)
        self.reset_btn.grid_configure(padx=5, pady=10)

        self.save_btn = Button(Para_frame, text='Save',fg="#FFCBCB", bg="#003C43", font=FONT_NAME, border=0,
                          command=self.save_text, width=40)
        self.save_btn.grid(column=6, row=5, columnspan=20)
        self.save_btn.grid_configure(padx=5, pady=10)

        self.timer_countdown = 5
        self.timer = None

        self.start_timer()

    def start_timer(self):
        self.timer = Timer(self.timer_countdown,self.user_inactive)
        self.timer.start()

    def on_key_press(self, event):
        self.reset_timer()

    def reset_timer(self):
        if self.timer is not None:
            self.timer.cancel()
        self.start_timer()

    def user_inactive(self):
        self.write.delete(1.0, END)

    def save_text(self):
        user_text = self.write.get(1.0, END)
        with open("Last Disappeared Text. txt", 'w') as file:
            file.write(f"{user_text}")



