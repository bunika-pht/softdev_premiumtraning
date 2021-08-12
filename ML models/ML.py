
from typing import Text
import PySimpleGUI as sg
import os.path

from PySimpleGUI.PySimpleGUI import WIN_CLOSED

SYMBOL_UP = '▲'
SYMBOL_DOWN = '▼'


head_text = 30
content_text = 10
sg.theme('Reddit')


class Code_generate():
    Layout = [
        [sg.Button("generate code", font=("Helvetica"))],
        [sg.Output(size=(265, 10), key='-CODE-')],
    ]


class Model_tranning():

    def collapse(layout, key):
        return sg.pin(sg.Column(layout, key=key))

    MODEL_1 = [
        [sg.Text("this is parameter model1")],
    ]
    MODEL_2 = [
        [sg.Text("this is parameter model2")],
    ]
    MODEL_3 = [
        [sg.Text("this is parameter model3")],
    ]
    MODEL_4 = [
        [sg.Text("this is parameter model4")],
    ]
    MODEL_5 = [
        [sg.Text("this is parameter model5")],
    ]

    list_model = [
        [
            sg.Text("Import CVS File"),
            sg.In(size=(300, 1), enable_events=True, key="-FOLDER-"),
            sg.FolderBrowse(),
        ],
        [
            sg.Text("Data spilt : Test size "),
            sg.Input(key='-TEST SIZE-', enable_events=True, size=(300, 1)),
            # sg.Button("Add", key="-ADD TRAIN SIZE-"),
        ],
        [
            sg.Checkbox("Data Validation")
        ],
        [
            sg.Text("n split"),
            sg.Input(key='-N SPLIT-',enable_events=True,size=(30,1))
        ],
        [
            sg.Text("Select Model"), sg.InputCombo(('Linear Model', 'SVM', 'Nearest Neighbor ',
                                                   'Decision Trees', 'Neural network'), size=(300, 1)),
        ],
        [collapse(MODEL_1, '-M1-')
         ],
        [collapse(MODEL_2, '-M2-')
         ],
        [collapse(MODEL_3, '-M3-')
         ],
        [collapse(MODEL_4, '-M4-')
         ],
        [collapse(MODEL_5, '-M5-')
         ],
        [
            sg.Text("Class list From Csv")
        ],

        [
            sg.Listbox(values=[], enable_events=True,
                       size=(300, 5), key="-CLASS LIST-")
        ],

    ]

    Layout = [
        [sg.Text('Mylayout')],
        [sg.Column(list_model)],
        [sg.Button("Back", key="-BACK-"),
         sg.Button("Train Model", key="-TRAIN-")],
        Code_generate.Layout,
    ]
    Frame_layout1 = [
        [sg.Text("confusion metrix", size=(70, 10), key="-TRAINM-")],
        [sg.Text("accuracy", key="-AC TRAIN-")],
    ]
    Frame_layout2 = [

        [sg.Text("confusion metrix", size=(70, 10), key="-TESTM-")],
        [sg.Text("accuracy", key="-AC TEST-")]

    ]
    train_column = [
        [sg.Frame('Train set', Frame_layout1, font='Any 12',size=(700,100))]
    ]

    test_column = [
        [sg.Frame('Test set', Frame_layout2, font='Any 12',size=(700,100))]


    ]
    Layout_Confusion_Matrix = [
        [sg.Text("Result", font=("Helvetica", head_text))],
        [sg.Text("Model Description"), sg.Text(key="-MD-")],
        [sg.Column([[sg.Column(train_column,element_justification='left'), sg.Column(test_column,element_justification='right')]],size=(2000,700),element_justification='center')],
        [sg.Button("Save Model", key="-SAVE MD-")]
    ]



class Prediction_Model():

    RESULT_LAYOUT = [
        [sg.Text("Result : Accuracy : Class prediction" , size=(40, 10), key="-RESULT-")],
        [sg.Text("%", key="-AC TEST-")]
    ]
    
    RESULT_LAYOUT1 = [
        [sg.Text("Result : Accuracy : Class prediction" , size=(40, 10), key="-RESULT1-")],
        [sg.Text("%", key="-AC TEST1-")]
    ]
    
    IMAGE_VIEW = [
            [sg.Text("View",font=("Helvetica", content_text))],
            [sg.Image(key="-PREDICT IMG-",size=(1400,800))],
    ]

    DATASET_CONFIG = [
        [sg.Text("Image file  "),
         sg.In(size=(30, 1), enable_events=True, key="-IMG FILE-"),
         sg.FilesBrowse()],

        [sg.Text("Data config"),
         sg.In(size=(30, 1), enable_events=True, key="-CONFIG FILE-"),
         sg.FileBrowse()],

        [sg.Text("Model file   "),
         sg.In(size=(30, 1), enable_events=True, key="-MODEL FILE-"),
         sg.FileBrowse()],

        [sg.Text("File List")],
        [sg.Listbox(values=[], enable_events=True, size=(50, content_text), key="-FILE LIST-")],
        [sg.Frame('Result', RESULT_LAYOUT, font='Any 12',size=(50,1))],
        [sg.Button("Predict", key="-PREDICT-", size=(50,1))],
    ]

    CAMERA_CONFIG =[
        [sg.Text('Camera'),sg.InputCombo(("USB CAMERA 3.0","Webcam"),size=(70,1))],
        [sg.Text("Data config"),
         sg.In(size=(30, 1), enable_events=True, key="-CONFIG FILE1-"),
         sg.FileBrowse()],
        [sg.Text("Model file   "),
         sg.In(size=(30, 1), enable_events=True, key="-MODEL FILE1-"),
         sg.FileBrowse()],
        [sg.Text("File List")],
        [sg.Listbox(values=[], enable_events=True,size=(50, content_text), key="-FILE LIST1-")],
        [sg.Frame('Result', RESULT_LAYOUT1, font='Any 12',size=(50,1))],
        [sg.Button("Predict", key="-PREDICT1-", size=(50,1))],
    ]

    DATA_IN_LAYOUT = [
        [sg.Column(DATASET_CONFIG)],
    ]

    CAMERA_IN_LAYOUT = [
        [sg.Column(CAMERA_CONFIG)],
    ]

    PAGE_LAYOUT = [
        [sg.Text("Model prediction",font=("Helvetica", head_text))],
        [sg.Column(IMAGE_VIEW),
        sg.VSeperator(),
        sg.TabGroup([[sg.Tab('Dataset Input', DATA_IN_LAYOUT),
        sg.Tab('Camera Input', CAMERA_IN_LAYOUT)]] , size=(400,800))],
        Code_generate.Layout,
    ]



PL = Prediction_Model()
window = sg.Window("AI.EXE", PL.PAGE_LAYOUT,resizable=True,finalize=True)
window.maximize()
window.TKroot.minsize(550,200)
# window['-PP1-'].expand(expand_x=True, expand_y=True)
# window['-PP2-'].expand(expand_x=True, expand_y=True)
# window['-PP3-'].expand(expand_x=True, expand_y=True)
while True:
    event, values = window.read()
    if event == "OK" or event == WIN_CLOSED:
        break

window.close()
