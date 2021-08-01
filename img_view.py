import PySimpleGUI as sg
import os.path

from PySimpleGUI.PySimpleGUI import WIN_CLOSED

file_list_colum = [
    [
        sg.Text("Image Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(values=[], enable_events=True,
                   size=(40, 20), key="-FILE LIST-")
    ],
]

image_viewer_colum = [
    [sg.Text("choose an image from the list on the left")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]

layout = [
    [sg.Text('Mylayout')],
    [sg.Column(file_list_colum),sg.VSeparator(),sg.Column(image_viewer_colum)],
    [sg.Button("OK")],
]

window = sg.Window("image_viewer", layout)

while True:
    event, values = window.read()
    if event == "OK" or event == WIN_CLOSED:
        break
window.close()
