import tkinter as tk
from tkinter import filedialog, messagebox
import os

class GameHomeScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        master.title("Game Home Screen")
        master.geometry("500x400")
        master.configure(bg="white")
        self.pack(expand=True, fill="both")
        self.create_widgets()
        self.bind_keys()
        self.current_index = 0
        self.update_focus()

    def create_widgets(self):
        self.buttons = []

        self.grid_columnconfigure((0, 1), weight=1, uniform="col")
        self.grid_rowconfigure((0, 1), weight=1, uniform="row")

        # Button style base
        self.button_config = {
            "width": 10,
            "height": 4,
            "font": ("Arial", 18, "bold"),
            "borderwidth": 2,
            "relief": "solid",
            "highlightthickness": 0
        }

        # Create buttons
        self.load_button = tk.Button(self, text="LOAD", command=self.load_game, **self.button_config)
        self.load_button.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.buttons.append(self.load_button)

        self.save_button = tk.Button(self, text="SAVE", command=self.save_game, **self.button_config)
        self.save_button.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.buttons.append(self.save_button)

        self.info_button = tk.Button(self, text="INFO", command=self.show_info, **self.button_config)
        self.info_button.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        self.buttons.append(self.info_button)

        self.exit_button = tk.Button(self, text="EXIT", command=self.master.destroy, **self.button_config)
        self.exit_button.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")
        self.buttons.append(self.exit_button)

        # Status label
        self.status_label = tk.Label(self, text="", bg="white", fg="green", font=("Arial", 10))
        self.status_label.grid(row=2, column=0, columnspan=2, pady=10)

    def bind_keys(self):
        self.master.bind("<Up>", self.navigate_up)
        self.master.bind("<Down>", self.navigate_down)
        self.master.bind("<Left>", self.navigate_left)
        self.master.bind("<Right>", self.navigate_right)
        self.master.bind("<Return>", self.activate_button)
        self.master.bind("<KP_Enter>", self.activate_button)

    def update_focus(self):
        # Reset all buttons to white with black text
        for btn in self.buttons:
            btn.configure(bg="white", fg="black")

        # Highlight selected button: black with white text
        self.buttons[self.current_index].configure(bg="black", fg="white")
        self.buttons[self.current_index].focus_set()

    def navigate_up(self, event):
        if self.current_index >= 2:
            self.current_index -= 2
            self.update_focus()

    def navigate_down(self, event):
        if self.current_index <= 1:
            self.current_index += 2
            self.update_focus()

    def navigate_left(self, event):
        if self.current_index % 2 == 1:
            self.current_index -= 1
            self.update_focus()

    def navigate_right(self, event):
        if self.current_index % 2 == 0:
            self.current_index += 1
            self.update_focus()

    def activate_button(self, event):
        self.buttons[self.current_index].invoke()

    def load_game(self):
        filename = filedialog.askopenfilename(initialdir=".", title="Select save file", filetypes=(("Save files", "*.sav"), ("All files", "*.*")))
        if filename and os.path.exists(filename):
            self.status_label.config(text=f"Game loaded from: {filename}")
        else:
            self.status_label.config(text="No valid save file selected.")

    def save_game(self):
        filename = filedialog.asksaveasfilename(initialdir=".", title="Save game as", defaultextension=".sav", filetypes=(("Save files", "*.sav"), ("All files", "*.*")))
        if filename:
            with open(filename, 'w') as file:
                file.write("example_game_data")
            self.status_label.config(text=f"Game saved to: {filename}")
        else:
            self.status_label.config(text="Save canceled.")

    def show_info(self):
        messagebox.showinfo("Game Info", "Adventure Game v1.0\nCreated by YourName\nExplore the world and save your progress!")

if __name__ == "__main__":
    root = tk.Tk()
    app = GameHomeScreen(master=root)
    app.mainloop()
