import customtkinter, random
from plyer import notification

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Guess The Number Game")
        self.geometry(f"{1100}x{580}")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.resizable(width=False, height=False)
        self.MinEntry = customtkinter.CTkEntry(self, placeholder_text="Enter the minimum number", width=200)
        self.MinEntry.grid(row=0, column=0, padx=(0, 150))
        self.MaxEntry = customtkinter.CTkEntry(self, placeholder_text="Enter the maximum number", width=200)
        self.MaxEntry.grid(row=0, column=1, padx=(0, 150))
        self.PlrEntry = customtkinter.CTkEntry(self, placeholder_text="Enter your number", width=200)
        self.PlrEntry.grid(row=1, column=0, padx=(400, 0))
        self.PlayButton = customtkinter.CTkButton(self, text="Play!", command=self.PlayGame)
        self.PlayButton.grid(row=2, column=0, padx=(400, 0))
        self.CreateNotification("Welcome to the Guess The Number Game", "Hi", 1)

    def CreateNotification(self, message, title, duration):
        notification.notify(message=message, title=title, app_name="Guess The Number Game", timeout=duration)

    def PlayGame(self):
        if len(self.MinEntry.get()) > 0 and len(self.MaxEntry.get()) > 0 and len(self.PlrEntry.get()) > 0:
            if self.MinEntry.get().isdigit() and self.MaxEntry.get().isdigit() and self.PlrEntry.get().isdigit():
                if int(self.MinEntry.get()) < int(self.MaxEntry.get()):
                    if int(self.PlrEntry.get()) >= int(self.MinEntry.get()) and int(self.PlrEntry.get()) <= int(self.MaxEntry.get()):
                        self.random_number = random.randint(int(self.MinEntry.get()), int(self.MaxEntry.get()))
                        if self.random_number == int(self.PlrEntry.get()):
                            self.CreateNotification("You guessed the number!", "Game info", 1)
                        else:
                            self.CreateNotification("You didn't guessed the number :(", "Game info", 1)
                    else:
                        self.CreateNotification("It seems that you have entered an incorrect value in your number.", "Error 4", 1)
                else:
                    self.CreateNotification("It seems that the minimum value is higher than the maximum.", "Error 3", 1)
            else:
                self.CreateNotification("It seems that some entered string is not a number.", "Error 2", 1)
        else:
            self.CreateNotification("It seems that you forgot to enter something.", "Error 1", 1)

if __name__ == "__main__":
    app = App()
    app.mainloop()