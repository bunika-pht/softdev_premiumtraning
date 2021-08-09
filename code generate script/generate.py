
from typing import Text
import PySimpleGUI as sg
import os.path
from PySimpleGUI.PySimpleGUI import T, WIN_CLOSED



class Code_generate():
    Layout = [
        [sg.Button("generate code", font=("Helvetica"))],
        [sg.Output(size=(100, 10), key='-CODE-')]
    ]

    def A(model, parameter):
        return f'moedl{model} : configh >> {parameter} '

generate = Code_generate
window = sg.Window("image_viewer",generate.Layout)
while True:
    event, values = window.read()
    if event == "OK" or event == WIN_CLOSED:
        break

window.close()
