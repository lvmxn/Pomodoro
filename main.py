import customtkinter as ctk


def start():
    global time, typer, flag_stop, flag_first
    time = 25 * 60
    typer = 1
    flag_stop = False
    flag_first = True


start()


def reset():
    global time, typer, flag_first
    if typer % 8 == 0:
        time = 30 * 60
    elif typer % 2 == 0:
        time = 5 * 60
    else:
        time = 25 * 60
    button_start.configure(command=tick, state="normal")
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
    if flag_first and not flag_stop:
        button_start.configure(command=None, state="disable")
        button_stop.configure(command=pause, state="normal")
        flag_first = not flag_first
    if flag_stop:
        flag_stop = not flag_stop
    elif time <= 0:
        typer += 1
        reset()
    else:
        time -= 1
        time_sec = time % 60
        time_min = time // 60
        if time_sec < 10:
            time_sec = "0" + str(time_sec)
        if time_min < 10:
            time_min = "0" + str(time_min)
        label_time.configure(text=f"{time_min}:{time_sec}")
        root.after(1, tick)


def pause():
    global flag_stop, flag_first
    flag_stop = not flag_stop
    flag_first = not flag_first
    button_start.configure(command=tick, state="normal")
    button_stop.configure(command=None, state="disable")


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Pomodoro Timer")
root.geometry("600x600")

label_main = ctk.CTkLabel(root, text="Pomodoro", font=("Arial", 40))
label_main.pack(pady=20)

label_time = ctk.CTkLabel(root, text=f"{time//60}:{time%60}0", font=("Arial", 40))
label_time.pack(pady=20)


button_frame = ctk.CTkFrame(root)
button_frame.pack(pady=20)

button_start = ctk.CTkButton(
    button_frame,
    text="Start",
    font=("Arial", 30),
    command=tick,
    fg_color="purple",
    width=150,
    height=40,
)
button_start.pack(side="left", padx=5)

button_stop = ctk.CTkButton(
    button_frame,
    text="Stop",
    font=("Arial", 30),
    command=None,
    fg_color="purple",
    width=150,
    height=40,
)
button_stop.pack(side="left", padx=5)

button_reset = ctk.CTkButton(
    button_frame,
    text="Reset",
    font=("Arial", 30),
    command=reset,
    fg_color="purple",
    width=150,
    height=40,
)
button_reset.pack(side="left", padx=5)

root.mainloop()
