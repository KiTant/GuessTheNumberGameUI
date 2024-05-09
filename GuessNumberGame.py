import customtkinter, random

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Guess The Number Game")
        self.geometry(f"{1100}x{250}")
        self.resizable(width=False, height=False)
        self.MinEntry = customtkinter.CTkEntry(self, placeholder_text="Enter the minimum number", width=200)
        self.MinEntry.pack(padx=100, pady=10)
        self.MaxEntry = customtkinter.CTkEntry(self, placeholder_text="Enter the maximum number", width=200)
        self.MaxEntry.pack(padx=100, pady=10)
        self.PlrEntry = customtkinter.CTkEntry(self, placeholder_text="Enter your number", width=200)
        self.PlrEntry.pack(padx=400, pady=10)
        self.PlayButton = customtkinter.CTkButton(self, text="Play!", command=self.PlayGame)
        self.PlayButton.pack(padx=400, pady=10)
        self.frame = customtkinter.CTkFrame(master=self, width=500, height=50)
        self.frame.pack()
        self.game_status_label = customtkinter.CTkLabel(self.frame, text=f"Game status: Nothing to show here", font=customtkinter.CTkFont(family="Arial", size=25, weight="bold"), text_color="#1aab91")
        self.game_status_label.pack()

    def PlayGame(self):
        if len(self.MinEntry.get()) > 0 and len(self.MaxEntry.get()) > 0 and len(self.PlrEntry.get()) > 0:
            if self.MinEntry.get().isdigit() and self.MaxEntry.get().isdigit() and self.PlrEntry.get().isdigit():
                if int(self.MinEntry.get()) < int(self.MaxEntry.get()):
                    if int(self.PlrEntry.get()) >= int(self.MinEntry.get()) and int(self.PlrEntry.get()) <= int(self.MaxEntry.get()):
                        self.random_number = random.randint(int(self.MinEntry.get()), int(self.MaxEntry.get()))
                        if self.random_number == int(self.PlrEntry.get()):
                            self.game_status_label.configure(text="Game status: You guessed the number!", text_color="#00ffff")
                        else:
                            self.game_status_label.configure(text="Game status: You didn't guessed the number :(", text_color="#00ffff")
                    else:
                        self.game_status_label.configure(text="Game status (Error 4): It seems that you have entered an incorrect value in your number.", text_color="#ff0000", font=customtkinter.CTkFont(family="Arial", size=14))
                else:
                    self.game_status_label.configure(text="Game status (Error 3): It seems that the minimum value is higher than the maximum.", text_color="#ff0000", font=customtkinter.CTkFont(family="Arial", size=14))
            else:
                self.game_status_label.configure(text="Game status (Error 2): It seems that some entered string is not a number.", text_color="#ff0000", font=customtkinter.CTkFont(family="Arial", size=14))
        else:
            self.game_status_label.configure(text="Game status (Error 1): It seems that you forgot to enter something.", text_color="#ff0000", font=customtkinter.CTkFont(family="Arial", size=14))

if __name__ == "__main__":
    app = App()
    app.mainloop()
