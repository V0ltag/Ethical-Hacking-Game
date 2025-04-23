### main.py

import tkinter as tk
from gamegui import GameGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = GameGUI(root)
    root.mainloop()
