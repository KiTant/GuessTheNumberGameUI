import random
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

# Set the appearance and theme of the application
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set up the main window properties
        self.title("Guess The Number Game")
        self.geometry("600x250")
        self.minsize(600, 250)
        self.maxsize(1000, 250)
        # Initialize the UI components
        self._initialize_components()

    def _initialize_components(self):
        # Entry for minimum number
        self.min_entry = ctk.CTkEntry(self, placeholder_text="Enter the minimum number", width=200)
        self.min_entry.pack(pady=5, fill="x")

        # Entry for maximum number
        self.max_entry = ctk.CTkEntry(self, placeholder_text="Enter the maximum number", width=200)
        self.max_entry.pack(pady=5, fill="x")

        # Entry for player's number
        self.player_entry = ctk.CTkEntry(self, placeholder_text="Enter your number", width=200)
        self.player_entry.pack(pady=5, fill="x")

        # Button to start the game
        self.play_button = ctk.CTkButton(self, text="Play!", command=self.play_game)
        self.play_button.pack(pady=5, fill="x")

        # Label to display the game status
        self.game_status_label = ctk.CTkLabel(self, text="Game status: Nothing to show here",
                                              font=ctk.CTkFont(family="Arial", size=25, weight="bold"),
                                              text_color="#1aab91")
        self.game_status_label.pack(pady=5, fill="x")

    def play_game(self):
        # Getting Values
        min_val = self.min_entry.get()
        max_val = self.max_entry.get()
        player_val = self.player_entry.get()

        # Checking values
        if not min_val or not max_val or not player_val:
            CTkMessagebox(title="Game status (Error 1)",
                          message="It seems that you forgot to enter some number(s).",
                          icon="cancel", option_1="Ok", sound=True)
            return

        if not min_val.isdigit() or not max_val.isdigit() or not player_val.isdigit():
            CTkMessagebox(title="Game status (Error 2)",
                          message="It seems that some entered string is not a number.",
                          icon="cancel", option_1="Ok", sound=True)
            return

        min_val, max_val, player_val = int(min_val), int(max_val), int(player_val)

        if min_val >= max_val:
            CTkMessagebox(title="Game status (Error 3)",
                          message="It seems that the minimum value is higher than the maximum or equal to it.",
                          icon="cancel", option_1="Ok", sound=True)
            return

        if not (min_val <= player_val <= max_val):
            CTkMessagebox(title="Game status (Error 4)",
                          message="It seems that you have entered an incorrect value in your number.",
                          icon="cancel", option_1="Ok", sound=True)
            return

        if 10**26 <= min_val <= player_val <= max_val:
            CTkMessagebox(title="Game status (Error 3)",
                          message="This numbers VERY high",
                          icon="cancel", option_1="Ok", sound=True)
            return

        # Check if player guessed the number
        random_number = random.randint(min_val, max_val)
        if random_number == player_val:
            self.update_status(f"Game status: You guessed the number! Bot chose: {random_number}")
        else:
            self.update_status(f"Game status: You didn't guess the number :( Bot chose: {random_number}")

    def update_status(self, message):
        self.game_status_label.configure(text=message, text_color="#00ffff", font=ctk.CTkFont(family="Arial", size=14))

if __name__ == "__main__":
    app = App()
    app.mainloop()
