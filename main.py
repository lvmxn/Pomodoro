import customtkinter as ctk


def start():
    global time, typer, flag_stop, flag_first
    time = 25 * 60
    typer = 1
    flag_stop = True
    flag_first = True


start()


def reset():
    global time, typer, flag_first, flag_stop
    flag_stop = True
    if typer % 8 == 0:
        time = 30 * 60
    elif typer % 2 == 0:
        time = 5 * 60
    else:
        time = 25 * 60
    button_start.configure(command=pause, state="normal")
    button_stop.configure(command=None, state="disable")
    time_sec = time % 60
    time_min = time // 60
    if time_sec < 10:
        time_sec = "0" + str(time_sec)
    if time_min < 10:
        time_min = "0" + str(time_min)
    label_time.configure(text=f"{time_min}:{time_sec}")
    flag_first = True


def tick():
    global time, typer, flag_stop, flag_first
    if not flag_stop:
        if flag_first:
            button_start.configure(command=None, state="disable")
            button_stop.configure(command=pause, state="normal")
            flag_first = False
        if time <= 0:
            typer += 1
            reset()
            root.after(1, tick)
        else:
            time -= 1
            time_sec = time % 60
            time_min = time // 60
            if time_sec < 10:
                time_sec = "0" + str(time_sec)
            if time_min < 10:
                time_min = "0" + str(time_min)
            label_time.configure(text=f"{time_min}:{time_sec}")
            root.after(1000, tick)
    else:
        root.after(1, tick)


def pause():
    global flag_stop, flag_first
    flag_stop = not flag_stop
    flag_first = True
    button_start.configure(command=pause, state="normal")
    button_stop.configure(command=None, state="disable")


def swith_mode(value):
    global time, typer, flag_first, flag_stop
    if value == "long break":
        while typer % 8 != 0:
            typer += 1
    elif value == "short break":
        while typer % 2 != 0 or typer % 8 == 0:
            typer += 1
    else:
        while typer % 2 == 0:
            typer += 1
    reset()


def reset_cycle():
    global typer
    typer = 1
    seg_button_mode.set("work")
    reset()


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Pomodoro Timer")
root.geometry("500x400")

label_main = ctk.CTkLabel(root, text="Pomodoro", font=("Arial", 40))
label_main.pack(pady=20)

seg_button_mode = ctk.CTkSegmentedButton(
    root, height=40, values=["work", "short break", "long break"], command=swith_mode
)
seg_button_mode.pack(pady=20, padx=150, fill="x")
seg_button_mode.set("work")

label_time = ctk.CTkLabel(root, text=f"{time//60}:{time%60}0", font=("Arial", 70))
label_time.pack(pady=20)


button_frame = ctk.CTkFrame(root)
button_frame.pack(pady=10)

button_start = ctk.CTkButton(
    button_frame,
    text="Start",
    font=("Arial", 30),
    command=pause,
    width=150,
    height=40,
)
button_start.pack(side="left", padx=5)

button_stop = ctk.CTkButton(
    button_frame,
    text="Stop",
    font=("Arial", 30),
    command=None,
    width=150,
    height=40,
)
button_stop.pack(side="left", padx=5)

button_reset = ctk.CTkButton(
    button_frame,
    text="Reset",
    font=("Arial", 30),
    command=reset,
    width=150,
    height=40,
)
button_reset.pack(side="left", padx=5)

button_frame2 = ctk.CTkFrame(root)
button_frame2.pack(pady=10)

button_reset_cycle = ctk.CTkButton(
    button_frame2,
    text="Reset cycle",
    font=("Arial", 20),
    command=reset_cycle,
    width=100,
    height=20,
)
button_reset_cycle.pack(side="left", padx=5)
tick()
root.mainloop()
