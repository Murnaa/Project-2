import PySimpleGUI as sg
import pyttsx3

layout = [
    [sg.Text("Enter Text : "), sg.InputText(key="-INPUT-")],
    [sg.Text("Voice Type" ), sg.Radio("Male Voice", "RADIO1", default=True, key="-MALE-"), sg.Radio("Female Voice", "RADIO1", key="-FEMALE-")],
    [sg.Button("Speak", key="-SPEAK-")]
]

window = sg.Window("Text to Speech App", layout)

engine = pyttsx3.init()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "-SPEAK-":
        text = values["-INPUT-"]
        if values["-MALE-"]:
            engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0")
        elif values["-FEMALE-"]:
            engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
        engine.say(text)
        engine.runAndWait()

window.close()
