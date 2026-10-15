import tkinter as tk
import time
import random

def start_display(lyrics_timeline, start_time):
    # 1. Initialize the invisible window
    root = tk.Tk()
    root.overrideredirect(True)  # Removes borders
    root.attributes("-topmost", True)  # Forces it over all other windows
    root.configure(bg='black')
    root.wm_attributes("-transparentcolor", "black")  # Makes background invisible

    # 2. Position it on the bottom left (Adjust the - 45 if it's too high/low)
    screen_height = root.winfo_screenheight()
    y_position = screen_height - 45
    root.geometry(f"1000x40+100+{y_position}")

    # 3. Create the text label
    label = tk.Label(root, text="", font=("Segoe UI", 14, "bold"), bg="black")
    label.pack(anchor="w")

    # Tkinter uses standard color names instead of ANSI codes
    gui_colors = ["cyan", "lime", "yellow", "magenta", "orange"]

    # State tracker so Python knows where it is in the song
    state = {"line_index": 0, "is_typing": False}

    # -- THE GUI TYPEWRITER --
    def type_letter(text, char_index):
        if char_index < len(text):
            current_text = label.cget("text")
            label.config(text=current_text + text[char_index])
            # .after() replaces time.sleep() for the typewriter delay (40ms)
            root.after(40, type_letter, text, char_index + 1)
        else:
            state["is_typing"] = False

    # -- THE GUI STOPWATCH --
    def check_time():
        if state["line_index"] < len(lyrics_timeline):
            target_time, text = lyrics_timeline[state["line_index"]]
            elapsed_time = time.time() - start_time

            # If it's time for the next lyric and we aren't currently typing one
            if elapsed_time >= target_time and not state["is_typing"]:
                state["is_typing"] = True
                # Pick random color and wipe the old text
                label.config(text="", fg=random.choice(gui_colors))
                # Start typing the new text
                type_letter(text, 0)
                # Move to the next line in the timeline
                state["line_index"] += 1

        # .after() replaces your while loop micro-nap (checks clock every 10ms)
        root.after(10, check_time)

    # Start the continuous clock-checking loop
    check_time()

    # Keep the window open
    root.mainloop()