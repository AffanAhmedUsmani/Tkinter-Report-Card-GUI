

from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import pandas as pd

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1500x800")
window.configure(bg="#000000")


canvas = Canvas(
    window,
    bg="#000000",
    height=800,
    width=1500,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    299.0,
    79.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0
)
entry_1.place(
    x=192.5,
    y=63.0,
    width=213.0,
    height=31.0
)

canvas.create_text(
    61.0,
    67.0,
    anchor="nw",
    text="Enrollment No ",
    fill="#FFFFFF",
    font=("Inter", 16 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    299.0,
    130.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0
)
entry_2.place(
    x=192.5,
    y=114.0,
    width=213.0,
    height=31.0
)

canvas.create_text(
    61.0,
    121.0,
    anchor="nw",
    text="Student Name ",
    fill="#FFFFFF",
    font=("Inter Bold", 16 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    299.0,
    184.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0
)
entry_3.place(
    x=192.5,
    y=168.0,
    width=213.0,
    height=31.0
)

canvas.create_text(
    61.0,
    175.0,
    anchor="nw",
    text="Department ",
    fill="#FFFFFF",
    font=("Inter Bold", 16 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    299.0,
    238.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0
)
entry_4.place(
    x=192.5,
    y=222.0,
    width=213.0,
    height=31.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    563.5,
    359.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0
)
entry_5.place(
    x=447.0,
    y=340.0,
    width=233.0,
    height=36.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    177.5,
    359.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0
)
entry_6.place(
    x=61.0,
    y=340.0,
    width=233.0,
    height=36.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    563.5,
    422.5,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0
)
entry_7.place(
    x=447.5,
    y=403.0,
    width=232.0,
    height=37.0
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    177.5,
    422.5,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0
)
entry_8.place(
    x=61.0,
    y=403.0,
    width=233.0,
    height=37.0
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    563.5,
    485.5,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0
)
entry_9.place(
    x=446.5,
    y=467.0,
    width=234.0,
    height=35.0
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    177.5,
    485.5,
    image=entry_image_10
)
entry_10 = Entry(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0
)
entry_10.place(
    x=61.0,
    y=467.0,
    width=233.0,
    height=35.0
)

entry_image_11 = PhotoImage(
    file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(
    563.5,
    548.5,
    image=entry_image_11
)
entry_11 = Entry(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0
)
entry_11.place(
    x=447.5,
    y=529.0,
    width=232.0,
    height=37.0
)

entry_image_12 = PhotoImage(
    file=relative_to_assets("entry_12.png"))
entry_bg_12 = canvas.create_image(
    177.5,
    548.5,
    image=entry_image_12
)
entry_12 = Entry(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0
)
entry_12.place(
    x=61.0,
    y=529.0,
    width=233.0,
    height=37.0
)

entry_image_13 = PhotoImage(
    file=relative_to_assets("entry_13.png"))
entry_bg_13 = canvas.create_image(
    563.5,
    612.0,
    image=entry_image_13
)
entry_13 = Entry(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0
)
entry_13.place(
    x=447.0,
    y=593.0,
    width=233.0,
    height=36.0
)

entry_image_14 = PhotoImage(
    file=relative_to_assets("entry_14.png"))
entry_bg_14 = canvas.create_image(
    177.5,
    612.0,
    image=entry_image_14
)
entry_14 = Entry(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0
)
entry_14.place(
    x=61.0,
    y=593.0,
    width=233.0,
    height=36.0
)

canvas.create_text(
    61.0,
    229.0,
    anchor="nw",
    text="Section ",
    fill="#FFFFFF",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    61.0,
    290.0,
    anchor="nw",
    text="Enter Subject Name and Marks ",
    fill="#FFFFFF",
    font=("Inter Bold", 24 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    1123.0,
    400.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: generateresult(),
    relief="flat"
)
button_1.place(
    x=241.0,
    y=666.0,
    width=277.0,
    height=60.0
)

student_details = ["Enrollment", "Student Name", "Department", "Section"]
input_details = []


def generateresult():
    input_details.append(entry_1.get())
    input_details.append(entry_2.get())
    input_details.append(entry_3.get())
    input_details.append(entry_4.get())
    input_details.append(entry_5.get())
    student_details.append(entry_6.get())
    input_details.append(entry_7.get())
    student_details.append(entry_8.get())
    input_details.append(entry_9.get())
    student_details.append(entry_10.get())
    input_details.append(entry_11.get())
    student_details.append(entry_12.get())
    input_details.append(entry_13.get())
    student_details.append(entry_14.get())
    student_details.append("percentage")
    student_details.append("Grade")
    temp = 0
    for i in range(4, 9):
        temp = temp + int(input_details[i])
    temp = temp/500
    temp = temp * 100
    input_details.append(temp)
    if temp > 80:
        input_details.append("A")
    elif temp > 70:
        input_details.append("B")
    elif temp > 60:
        input_details.append("C")
    elif temp > 50:
        input_details.append("D")
    else:
        input_details.append("fail")

    df = pd.DataFrame(list(zip(student_details, input_details)),
                      columns=['info', 'inputs'])

    df.to_excel("result{}.xlsx".format(entry_1.get()))


window.resizable(False, False)
window.mainloop()
