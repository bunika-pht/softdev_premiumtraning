from typing import Text
import PySimpleGUI as sg
import os.path

from PySimpleGUI.PySimpleGUI import WIN_CLOSED
head_text = 20
content_text = 15
SYMBOL_UP =    '▲'
SYMBOL_DOWN =  '▼'
class Model_tranning():

    file_list_colum = [
        [
            sg.Text("Import CVS File"),
            sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
            sg.FolderBrowse(),
        ],
        [
            sg.Text("Data spilt : Test size "),
            sg.Input(key='-TEST SIZE-', enable_events=True, size=(20, 1)),
            # sg.Button("Add", key="-ADD TRAIN SIZE-"),
        ],
        [
            sg.Listbox(values=[], enable_events=True,
                       size=(40, content_text), key="-FILE LIST-")
        ],
        [
            sg.Text("Class list")
        ],

        [
            sg.Listbox(values=[], enable_events=True,
                       size=(40, 5), key="-CLASS LIST-")
        ],

    ]
    image_viewer_colum = [
        [sg.Text("choose an image from the list on the left")],
        [sg.Text(size=(40, 1), key="-TOUT1-")],
        [sg.Image(key="-IMAGE1-")],
    ]

    Layout_InserDataset = [
        [sg.Text('Mylayout')],
        [sg.Column(file_list_colum)],
        [sg.Button("Back", key="-BACK-"), sg.Button("Next", key="-NEXT-")],
    ]

    Layout = [
        [sg.Text("Create Model",auto_size_text=True,
                 font=("Helvetica", head_text))]    
        ]
    
pp = Model_tranning()
window = sg.Window("image_viewer", pp.Layout_InserDataset)
while True:
    event, values = window.read()
    if event == "OK" or event == WIN_CLOSED:
        break

window.close()
