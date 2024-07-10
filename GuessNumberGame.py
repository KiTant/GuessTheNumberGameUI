import random
import customtkinter as ctk

# Set the appearance and theme of the application
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set up the main window properties
        self.title("Guess The Number Game")
        self.geometry("1100x250")
        self.resizable(False, False)

        # Initialize the UI components
        self._initialize_components()

    def _initialize_components(self):
        # Entry for minimum number
        self.min_entry = ctk.CTkEntry(self, placeholder_text="Enter the minimum number", width=200)
        self.min_entry.pack(padx=100, pady=10)

        # Entry for maximum number
        self.max_entry = ctk.CTkEntry(self, placeholder_text="Enter the maximum number", width=200)
        self.max_entry.pack(padx=100, pady=10)

        # Entry for player's number
        self.player_entry = ctk.CTkEntry(self, placeholder_text="Enter your number", width=200)
        self.player_entry.pack(padx=400, pady=10)

        # Button to start the game
        self.play_button = ctk.CTkButton(self, text="Play!", command=self.play_game)
        self.play_button.pack(padx=400, pady=10)

        # Frame to display the game status
        self.status_frame = ctk.CTkFrame(self, width=500, height=50)
        self.status_frame.pack()

        # Label to display the game status
        self.game_status_label = ctk.CTkLabel(self.status_frame, text="Game status: Nothing to show here",
                                              font=ctk.CTkFont(family="Arial", size=25, weight="bold"), text_color="#1aab91")
        self.game_status_label.pack()

    def play_game(self):
        min_val = self.min_entry.get()
        max_val = self.max_entry.get()
        player_val = self.player_entry.get()

        if not min_val or not max_val or not player_val:
            self.update_status("Game status (Error 1): It seems that you forgot to enter something.", error=True)
            return

        if not min_val.isdigit() or not max_val.isdigit() or not player_val.isdigit():
            self.update_status("Game status (Error 2): It seems that some entered string is not a number.", error=True)
            return

        min_val, max_val, player_val = int(min_val), int(max_val), int(player_val)

        if min_val >= max_val:
            self.update_status("Game status (Error 3): It seems that the minimum value is higher than the maximum.", error=True)
            return

        if not (min_val <= player_val <= max_val):
            self.update_status("Game status (Error 4): It seems that you have entered an incorrect value in your number.", error=True)
            return

        random_number = random.randint(min_val, max_val)
        if random_number == player_val:
            self.update_status(f"Game status: You guessed the number! Bot chose: {random_number}", success=True)
        else:
            self.update_status(f"Game status: You didn't guess the number :( Bot chose: {random_number}", success=True)

    def update_status(self, message, error=False, success=False):
        color = "#ff0000" if error else "#00ffff"
        font_size = 14 if error else 25
        self.game_status_label.configure(text=message, text_color=color, font=ctk.CTkFont(family="Arial", size=font_size))

if __name__ == "__main__":
    app = App()
    app.mainloop()
