import tkinter as tk
from tkinter import messagebox
import pygame
from game import Game
from mission import Mission
import random

class GameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Neo-Data Heist")
        self.root.configure(bg="black")

        pygame.mixer.init()

        self.player_name = ""
        self.current_mission = None

        self.title_label = tk.Label(root, text="Neo-Data Heist", fg="lime", bg="black", font=("Consolas", 24, "bold"))
        self.title_label.pack(pady=10)

        self.name_label = tk.Label(root, text="Enter your hacker alias:", fg="white", bg="black", font=("Consolas", 12))
        self.name_label.pack()

        self.name_entry = tk.Entry(root, font=("Consolas", 12))
        self.name_entry.pack(pady=5)

        self.start_button = tk.Button(root, text="Start Game", command=self.start_game, bg="gray", fg="white", font=("Consolas", 12))
        self.start_button.pack(pady=10)

        self.text_area = tk.Text(root, height=15, width=60, bg="black", fg="lime", font=("Consolas", 10))
        self.text_area.pack(pady=10)

        self.options_frame = tk.Frame(root, bg="black")
        self.options_frame.pack()

        self.difficulty_label = tk.Label(root, text="Select Difficulty:", fg="white", bg="black", font=("Consolas", 12))
        self.difficulty_label.pack(pady=5)

        self.difficulty_var = tk.StringVar(value="Medium")
        self.easy_button = tk.Radiobutton(root, text="Easy", variable=self.difficulty_var, value="Easy", bg="black", fg="white")
        self.medium_button = tk.Radiobutton(root, text="Medium", variable=self.difficulty_var, value="Medium", bg="black", fg="white")
        self.hard_button = tk.Radiobutton(root, text="Hard", variable=self.difficulty_var, value="Hard", bg="black", fg="white")
        self.easy_button.pack()
        self.medium_button.pack()
        self.hard_button.pack()

    def display(self, message):
        self.text_area.insert(tk.END, message + "\n")
        self.text_area.see(tk.END)

    def start_game(self):
        self.player_name = self.name_entry.get()
        if not self.player_name:
            messagebox.showwarning("Input Error", "Please enter a hacker alias.")
            return

        self.name_label.pack_forget()
        self.name_entry.pack_forget()
        self.start_button.pack_forget()
        self.difficulty_label.pack_forget()
        self.easy_button.pack_forget()
        self.medium_button.pack_forget()
        self.hard_button.pack_forget()

        self.display(f"Welcome to Neo-Data Heist, {self.player_name}!")
        self.display("Your goal: Complete cyber missions to become a legend in the net.")
        self.launch_mission()

    def launch_mission(self):
        missions = [
            Mission("Hack the Bank", "Steal the vault password and escape undetected.", 5000, ["Encryption", "Stealth"], "hacking"),
            Mission("Corporate Espionage", "Infiltrate rival corp to steal prototype blueprints.", 7000, ["Social Engineering", "Stealth"], "stealth"),
            Mission("Encryption Puzzle", "Crack the encoded message for the next clue.", 3000, [], "puzzle"),
            Mission("Trace Hacker", "Identify and locate a blackhat's IP address.", 6000, ["IP Tracking", "OSINT"], "trace"),
            Mission("Bypass AI Firewall", "Penetrate next-gen AI security systems.", 9000, ["Malware Analysis", "Reverse Engineering"], "advanced"),
            Mission("Drone Hijack", "Override the defense drones of a corporate HQ.", 8500, ["Wireless Hacking", "Signal Jamming"], "hijack"),
            Mission("Neural Net Infiltration", "Upload a virus to a neural data archive.", 9500, ["Deep Learning", "Binary Analysis"], "neural")
        ]
        self.current_mission = random.choice(missions)
        self.display(self.current_mission.display_details())
        self.display_mission_choices()

    def display_mission_choices(self):
        for widget in self.options_frame.winfo_children():
            widget.destroy()

        if self.current_mission:
            options = self.current_mission.get_choices()
            for option in options:
                btn = tk.Button(self.options_frame, text=option, command=lambda opt=option: self.submit_choice(opt), bg="gray", fg="white", font=("Consolas", 12))
                btn.pack(pady=2)

    def submit_choice(self, choice):
        player_skills = ["Encryption", "Stealth", "IP Tracking", "OSINT", "Malware Analysis", "Reverse Engineering", "Social Engineering", "Wireless Hacking", "Signal Jamming", "Deep Learning", "Binary Analysis"]
        result, message = self.current_mission.evaluate_choice(choice, player_skills)
        self.display(message)

        if result:
            pygame.mixer.music.load("sounds/mission_success.wav")
            pygame.mixer.music.play()
            self.display("MISSION SUCCESS!")
        else:
            pygame.mixer.music.load("sounds/mission_failed.wav")
            pygame.mixer.music.play()
            self.display("MISSION FAILED!")

        self.root.after(3000, self.launch_mission)
