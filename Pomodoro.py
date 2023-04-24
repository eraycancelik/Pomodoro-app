import tkinter
import platform
from tkinter import *

root = tkinter.Tk()
root.title("Focus with Pomodoro")
root.geometry("300x300")
root.resizable(width=False, height=False)
all_bg = "#1e1d1d"
all_fg = "white"
button_fg = "#F2F2F2"
button_bg = "#014F36"
highlightcolor = "#01FCAC"
throughcolor = "#018057"
thickness = 1
scalewidth = 8
scaleLenght = 225
scaleCursorWork = "based_arrow_down"
scaleCursorBreak = "based_arrow_up"
root.config(bg=all_bg)
totalpomo = 0


def runOnWin():
    iconPhoto = PhotoImage(file="icons/pomo2.png")
    root.iconphoto(False, iconPhoto)
    global totalpomo

    def prep():
        my_label.grid(row=2, column=1, pady=0, padx=15, ipadx=0, ipady=40, sticky=tkinter.NS)
        allsession.grid(row=1, column=1, pady=10, padx=50, sticky=tkinter.NSEW)
        global totalpomo
        totalpomo += 1
        allsession.config(text="   Number of Pomodoros: {}".format(totalpomo))
        my_button.destroy()
        countdown(pomodoro_time)

    def finish():
        root.attributes('-topmost', True)
        root.lift()

        my_label.config(text="  Break Time is\n Over", font=("Calibra", 25))
        my_label.grid(row=2, column=1, padx=(5, 0), pady=(20, 0), ipadx=0, ipady=0, sticky=tkinter.NS)

        lastbutton = tkinter.Button(text="New Pomodoro", font=('Calibra', 15), foreground=button_fg, bg=button_bg,
                                    command=lambda: [prep(), lastbutton.grid_remove(), exitbutton.grid_remove()])
        lastbutton.grid(row=3, column=1, padx=(24, 0), pady=(40, 0), ipadx=20, ipady=0, sticky=tkinter.NS)

        exitbutton = tkinter.Button(text="Finish", font=('Calibra', 15), foreground=button_fg, bg=button_bg,
                                    command=lambda: [root.destroy()])
        exitbutton.grid(row=4, column=1, padx=(25, 0), pady=(9, 0), ipadx=64, ipady=0, sticky=tkinter.NS)

    def countdown(count):
        root.attributes('-topmost', False)
        root.lift()
        if count > 0:

            mins, secs = divmod(count, 60)
            timer = ' {:02d}:{:02d}'.format(mins, secs)
            my_label["text"] = timer
            my_label.config(font="Calibra 56")
            my_label.grid(row=2, pady=30, column=1, ipady=40, ipadx=0, sticky=tkinter.N)
            root.after(1000, countdown, count - 1)
        else:
            root.attributes('-topmost', True)
            root.lift()
            my_label.config(text="Finished", font="Calibra 40")
            my_label.grid(pady=(10, 0), padx=(25, 0), sticky=tkinter.NS)
            my2_button = tkinter.Button(root, text="Take a break", font=('Calibra', 15), foreground=button_fg,
                                        bg=button_bg,
                                        command=lambda: [breaktimecounter(break_time), my2_button.grid_remove()])
            my2_button.grid(row=3, column=1, padx=(25, 0), ipadx=30, sticky=tkinter.NS)

    def breaktimecounter(breaktime):
        root.attributes('-topmost', False)
        root.lift()

        if breaktime > 0:
            mins, secs = divmod(breaktime, 60)
            timer = ' {:02d}:{:02d}'.format(mins, secs)
            my_label["text"] = timer
            my_label.config(font="Calibra 56")
            my_label.grid(pady=(32, 0), padx=(2, 0), sticky=tkinter.N)
            root.after(1000, breaktimecounter, breaktime - 1)
        else:
            finish()

    def scaleDestroy():
        work_time_label.destroy()
        work_time_scale.destroy()
        break_time_label.destroy()
        break_time_scale.destroy()

    def getTime():
        global pomodoro_time
        global break_time
        pomodoro_time = int(work_time_scale.get())*60
        break_time = int(break_time_scale.get())*60

    allsession = tkinter.Label(root, text="Number of Pomodoros: {}".format(totalpomo),
                               font=("@Kozuka Mincho Pro L", 10, "bold"), bg=all_bg, fg=all_fg)
    allsession.grid(row=1, column=1, pady=10, padx=(30, 0), sticky=tkinter.NSEW)
    my_label = tkinter.Label(root, text="Get Ready to Focus!", font=("Myriad Pro", 20), bg=all_bg, fg=all_fg)
    my_label.grid(row=2, column=1, pady=0, padx=(40, 0), ipadx=0, ipady=5, sticky=tkinter.NS)

    work_time_scale = tkinter.Scale(root, from_=1, to=60, highlightthickness=thickness,
                                    highlightbackground=highlightcolor,
                                    cursor=scaleCursorWork, troughcolor=throughcolor, orient=tkinter.HORIZONTAL,
                                    length=scaleLenght,
                                    borderwidth=0, width=scalewidth, bg=all_bg, fg=all_fg)
    work_time_scale.grid(row=3, column=1, padx=(35, 0), pady=(20, 2), sticky=tkinter.N)
    work_time_label = tkinter.Label(root, text="Working session (minutes)", bg=all_bg, fg=all_fg)
    work_time_label.grid(row=4, column=1, padx=(35, 0), pady=(0, 10), sticky=tkinter.NSEW)
    break_time_scale = tkinter.Scale(root, from_=1, to=30, highlightthickness=thickness,
                                     highlightbackground=highlightcolor,
                                     cursor=scaleCursorBreak, troughcolor=throughcolor, orient=tkinter.HORIZONTAL,
                                     length=scaleLenght,
                                     borderwidth=0, width=scalewidth, bg=all_bg, fg=all_fg)
    break_time_scale.grid(row=5, column=1, padx=(35, 0), pady=(0, 2), sticky=tkinter.NS)
    break_time_label = tkinter.Label(root, text="Recharge time (minutes)", bg=all_bg, fg=all_fg)
    break_time_label.grid(row=6, column=1, padx=(35, 0), sticky=tkinter.NSEW)
    my_button = tkinter.Button(text="Start", font=('Calibra', 15), foreground=button_fg, bg=button_bg,
                               command=lambda: [getTime(), prep(), my_button.pack_forget(), scaleDestroy()])
    my_button.grid(row=7, column=1, pady=(15, 0), padx=(30, 0), ipadx=60, ipady=0, sticky=tkinter.NS)
    global pomodoro_time
    global break_time
    root.mainloop()


def runOnLinux():
    global totalpomo

    def prep():
        my_label.grid(row=2, column=1, pady=0, padx=15, ipadx=0, ipady=40, sticky=tkinter.NS)
        allsession.grid(row=1, column=1, pady=10, padx=50, sticky=tkinter.NSEW)
        global totalpomo
        totalpomo += 1
        allsession.config(text="   Number of Pomodoros: {}".format(totalpomo))
        my_button.destroy()
        countdown(pomodoro_time)

    def finish():
        root.attributes('-topmost', True)
        root.lift()

        my_label.config(text="  Break Time\nis Over", font=("Papyrus", 25))
        my_label.grid(row=2, column=1, padx=(0, 10), pady=(20, 0), ipadx=0, ipady=0, sticky=tkinter.NS)

        lastbutton = tkinter.Button(text="New Pomodoro", font=('Papyrus', 15), foreground=button_fg, bg=button_bg,
                                    command=lambda: [prep(), lastbutton.grid_remove(), exitbutton.grid_remove()])
        lastbutton.grid(row=3, column=1, padx=(2, 0), pady=(50, 0), ipadx=5, ipady=0, sticky=tkinter.NS)

        exitbutton = tkinter.Button(text="Finish", font=('Papyrus', 15), foreground=button_fg, bg=button_bg,
                                    command=lambda: [root.destroy()])
        exitbutton.grid(row=4, column=1, padx=(3, 0), pady=(9, 0), ipadx=49, ipady=0, sticky=tkinter.NS)

    def countdown(count):
        root.attributes('-topmost', False)
        root.lift()
        if count > 0:

            mins, secs = divmod(count, 60)
            timer = ' {:02d}:{:02d}'.format(mins, secs)
            my_label["text"] = timer
            my_label.config(font="Calibra 56")
            my_label.grid(row=2, pady=30, padx=(0, 25), column=1, ipady=40, ipadx=0, sticky=tkinter.N)
            root.after(1000, countdown, count - 1)
        else:
            root.attributes('-topmost', True)
            root.lift()

            my_label.config(text="Finished", font="Papyrus 40")
            my_label.grid(pady=10, padx=10, sticky=tkinter.NS)
            my2_button = tkinter.Button(root, text="Take a break", font=('Papyrus', 15), foreground=button_fg, bg=button_bg,
                                        command=lambda: [breaktimecounter(break_time), my2_button.grid_remove()])
            my2_button.grid(row=3, column=1, padx=0, pady=0, ipadx=20, ipady=0, sticky=tkinter.NS)

    def breaktimecounter(breaktime):
        root.attributes('-topmost', False)
        root.lift()

        if breaktime > 0:
            mins, secs = divmod(breaktime, 60)
            timer = ' {:02d}:{:02d}'.format(mins, secs)
            my_label["text"] = timer
            my_label.config(font="Papyrus 56")
            my_label.grid(pady=30, padx=(0, 20), sticky=tkinter.NS)
            root.after(1000, breaktimecounter, breaktime - 1)
        else:
            finish()

    def scaleDestroy():
        work_time_label.destroy()
        work_time_scale.destroy()
        break_time_label.destroy()
        break_time_scale.destroy()

    allsession = tkinter.Label(root, text="Number of Pomodoros: {}".format(totalpomo),
                               font=("@Kozuka Mincho Pro L", 10, "bold"), bg=all_bg, fg=all_fg)
    allsession.grid(row=1, column=1, pady=10, padx=50, sticky=tkinter.NSEW)
    my_label = tkinter.Label(root, text="Get Ready to Focus!", font=("Myriad Pro", 20), bg=all_bg, fg=all_fg)
    my_label.grid(row=2, column=1, pady=0, padx=15, ipadx=0, ipady=5, sticky=tkinter.NS)

    work_time_scale = tkinter.Scale(root, from_=1, to=60, highlightthickness=1, highlightbackground=highlightcolor,
                                    cursor=scaleCursorWork, troughcolor=throughcolor, orient=tkinter.HORIZONTAL,
                                    length=250,
                                    borderwidth=0, width=scalewidth, bg=all_bg, fg=all_fg)
    work_time_scale.grid(row=3, column=1, pady=(20, 2), sticky=tkinter.NS)
    work_time_label = tkinter.Label(root, text="Working session (minutes):", bg=all_bg, fg=all_fg)
    work_time_label.grid(row=4, column=1, pady=(0, 10), padx=(0, 20), sticky=tkinter.NSEW)
    break_time_scale = tkinter.Scale(root, from_=1, to=30, highlightthickness=1,
                                     highlightbackground=highlightcolor,
                                     cursor=scaleCursorBreak, troughcolor=throughcolor, orient=tkinter.HORIZONTAL,
                                     length=250,
                                     borderwidth=0, width=scalewidth, bg=all_bg, fg=all_fg)
    break_time_scale.grid(row=5, column=1, pady=(0, 2), sticky=tkinter.NS)
    break_time_label = tkinter.Label(root, text="Recharge time (minutes):", bg=all_bg, fg=all_fg)
    break_time_label.grid(row=6, column=1, sticky=tkinter.NSEW)

    def getTime():
        global pomodoro_time
        global break_time
        pomodoro_time = int(work_time_scale.get())*60
        break_time = int(break_time_scale.get())*60

    my_button = tkinter.Button(text="Start", font=('Calibra', 15), foreground=button_fg, bg=button_bg,
                               command=lambda: [getTime(), prep(), my_button.pack_forget(), scaleDestroy()])
    my_button.grid(row=7, column=1, pady=(15, 0), padx=30, ipadx=60, ipady=0, sticky=tkinter.NS)
    global pomodoro_time
    global break_time
    root.mainloop()


def runPomodoro():
    if platform.platform()[0] == "L":
        runOnLinux()
    else:
        runOnWin()


runPomodoro()
