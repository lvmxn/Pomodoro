import customtkinter as ctk
import winsound


def start():
    global time, typer, flag_stop, flag_first, work_time, short_time, long_time
    time = 25 * 60
    typer = 1
    flag_stop = True
    flag_first = True
    work_time = 25
    short_time = 5
    long_time = 30

def reset():
    global time, typer, flag_first, flag_stop
    flag_stop = True
    value_work = textbox_work.get()
    value_short = textbox_short.get()
    value_long = textbox_long.get()
    if typer % 8 == 0:
        if value_long == "":
            time = long_time * 60
        else:
            time = int(value_long) * 60
    elif typer % 2 == 0:
        if value_short == "":
            time = short_time * 60
        else:
            time = int(value_short) * 60
    else:
        if value_work == "":
            time = work_time * 60
        else:
            time = int(value_work) * 60
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
            winsound.PlaySound(
                "resources\\end.wav", winsound.SND_FILENAME | winsound.SND_ASYNC
            )
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


def show_main():
    settings_frame.pack_forget()
    main_frame.pack(fill="both", expand=True)
    reset()


def show_settings():
    main_frame.pack_forget()
    settings_frame.pack(fill="both", expand=True)


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Pomodoro Timer")
root.geometry("500x400")

main_frame = ctk.CTkFrame(root)
settings_frame = ctk.CTkFrame(root)

main_frame.pack(fill="both", expand=True)

start()

label_main = ctk.CTkLabel(main_frame, text="Pomodoro", font=("Arial", 40))
label_main.pack(pady=20)

seg_button_mode = ctk.CTkSegmentedButton(
    main_frame,
    height=40,
    values=["work", "short break", "long break"],
    command=swith_mode,
)
seg_button_mode.pack(pady=20, padx=150, fill="x")
seg_button_mode.set("work")

label_time = ctk.CTkLabel(main_frame, text=f"{time//60}:{time%60}0", font=("Arial", 70))
label_time.pack(pady=20)


button_frame = ctk.CTkFrame(main_frame)
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

button_frame2 = ctk.CTkFrame(main_frame)
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

button_settings = ctk.CTkButton(
    button_frame2,
    text="settings",
    font=("Arial", 20),
    command=show_settings,
    width=100,
    height=20,
)
button_settings.pack(side="left", padx=5)

label_settings = ctk.CTkLabel(settings_frame, text="Settings", font=("Arial", 40))
label_settings.pack(pady=20)

textbox_frame = ctk.CTkFrame(settings_frame)
textbox_frame.pack(pady=10)

textbox1_frame = ctk.CTkFrame(textbox_frame)
textbox1_frame.pack(side="left", padx=5)

textbox_work = ctk.CTkEntry(textbox1_frame, placeholder_text="default 25")
textbox_work.pack(side="bottom", pady=5)

label_work = ctk.CTkLabel(textbox1_frame, text="work", font=("Arial", 15))
label_work.pack(side="top", pady=5)

textbox2_frame = ctk.CTkFrame(textbox_frame)
textbox2_frame.pack(side="left", padx=5)

textbox_short = ctk.CTkEntry(textbox2_frame, placeholder_text="default 5")
textbox_short.pack(side="bottom", pady=5)

label_short = ctk.CTkLabel(textbox2_frame, text="short break", font=("Arial", 15))
label_short.pack(side="top", pady=5)


textbox3_frame = ctk.CTkFrame(textbox_frame)
textbox3_frame.pack(side="left", padx=5)

textbox_long = ctk.CTkEntry(textbox3_frame, placeholder_text="default 30")
textbox_long.pack(side="bottom", pady=5)

label_long = ctk.CTkLabel(textbox3_frame, text="long break", font=("Arial", 15))
label_long.pack(side="top", pady=5)

button_main = ctk.CTkButton(
    settings_frame,
    text="back",
    font=("Arial", 20),
    command=show_main,
    width=100,
    height=20,
)
button_main.pack(pady=10)

tick()

root.mainloop()
